#!/usr/bin/env python3
"""Render supplied finite values as a static accessible SVG; no interpolation."""
import argparse
import json
import math
import textwrap
from pathlib import Path
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
COLORS = ('#2463a6', '#a65c19', '#7251a1', '#237668')

def validate(data):
    if data.get('kind') not in ('bar', 'line'):
        raise ValueError('kind must be bar or line')
    for key in ('title', 'unit', 'period', 'source'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(key + ' must be a nonempty string')
    if len(data['title']) > 90 or len(data['unit']) > 30 or len(data['period']) > 50:
        raise ValueError('shorten title/unit/period for legibility; retain full context in source')
    labels, series = data.get('labels'), data.get('series')
    if not isinstance(labels, list) or not labels or not all(isinstance(x, str) and x.strip() for x in labels):
        raise ValueError('labels must be nonempty strings')
    if any(len(x) > 24 for x in labels):
        raise ValueError('shorten category labels to 24 characters and supply a full-label mapping separately')
    if len(set(labels)) != len(labels):
        raise ValueError('labels must be unique')
    if not isinstance(series, list) or not 1 <= len(series) <= 4:
        raise ValueError('provide 1 to 4 comparable series')
    if len(labels) > 30:
        raise ValueError('split charts above 30 categories for legibility')
    names = set()
    for item in series:
        if not isinstance(item, dict) or not isinstance(item.get('name'), str) or not item['name'].strip():
            raise ValueError('series name required')
        if len(item['name']) > 22:
            raise ValueError('shorten series names to 22 characters for legibility')
        if item['name'] in names:
            raise ValueError('series names must be unique')
        names.add(item['name'])
        values = item.get('values')
        if not isinstance(values, list) or len(values) != len(labels):
            raise ValueError('each series must align with labels')
        for x in values:
            if x is not None and (isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)):
                raise ValueError('values must be finite numbers or null')
    return labels, series

def percentage_change(actual, baseline):
    """Zero/missing baseline has no percentage; negative baseline is disclosed."""
    if actual is None or baseline is None or baseline == 0:
        return None
    return (actual - baseline) / abs(baseline) * 100

def render(data):
    labels, series = validate(data)
    # Keep round-trip numeric text readable rather than rounding the exact table.
    exact_width = max(len(str(x)) for item in series for x in item['values'])
    cell_width = max(180, exact_width * 8 + 24)
    width = max(800, 90 * len(labels), 275 + len(series) * cell_width)
    left, right, top, bottom = 95, width - 35, 120, 380
    table_start = 485
    source_lines = textwrap.wrap('Source: ' + data['source'], width=max(60, (width-60)//8))
    height = table_start + 28 * (len(labels) + 1) + 65 + 20*len(source_lines)
    root = ET.Element(f'{{{NS}}}svg', {'viewBox': f'0 0 {width} {height}', 'width': str(width), 'height': str(height), 'role': 'img', 'aria-labelledby': 'title description'})
    def add(tag, **attrs):
        return ET.SubElement(root, f'{{{NS}}}{tag}', {k.replace('_','-'): str(v) for k,v in attrs.items()})
    ET.SubElement(root, f'{{{NS}}}title', {'id':'title'}).text = data['title']
    ET.SubElement(root, f'{{{NS}}}desc', {'id':'description'}).text = 'Exact values below. Missing observations are gaps; zero is an observed value. Source: ' + data['source']
    add('rect', x=0, y=0, width=width, height=height, fill='white')
    def text(x,y,value,**attrs):
        style = dict(fill='#182735', font_family='Arial, sans-serif', font_size=14)
        style.update(attrs)
        add('text', x=x, y=y, **style).text = str(value)
    text(30,35,data['title'],font_weight='bold')
    text(30,62,f"{data['period']} • {data['unit']} • {data['kind']}")
    for j,item in enumerate(series):
        add('rect',x=30+j*190,y=82,width=13,height=13,fill=COLORS[j])
        text(49+j*190,94,item['name'])
    observed = [x for item in series for x in item['values'] if x is not None]
    lo, hi = min([0]+observed), max([0]+observed)
    if lo == hi: lo,hi = -1,1
    span = hi - lo
    if not math.isfinite(span): raise ValueError('numeric range exceeds finite chart scale')
    def y(value): return bottom - (value-lo)/span*(bottom-top)
    for i in range(5):
        value = lo + span*(i/4)
        add('line',x1=left,y1=y(value),x2=right,y2=y(value),stroke='#dde4eb')
        text(left-10,y(value)+5,f'{value:g}',text_anchor='end')
    add('line',x1=left,y1=y(0),x2=right,y2=y(0),stroke='#445566',stroke_width=2)
    step = (right-left)/len(labels)
    for i,label in enumerate(labels):
        cx = left + step*(i+.5)
        # Long category labels remain exact in the table.
        text(cx,bottom+26,label if len(label)<=14 else label[:12]+'…',text_anchor='middle')
    if not observed:
        text((left+right)/2,235,'No observed data',text_anchor='middle')
    for j,item in enumerate(series):
        previous = None
        for i,value in enumerate(item['values']):
            cx = left + step*(i+.5)
            if value is None:
                previous = None
                continue
            if data['kind']=='bar':
                bw = min(48,step*.76/len(series))
                bx = cx - bw*len(series)/2 + j*bw
                rect = add('rect',x=bx,y=min(y(value),y(0)),width=bw*.9,height=abs(y(value)-y(0)),fill=COLORS[j],data_series=item['name'],data_value=value)
                ET.SubElement(rect,f'{{{NS}}}title').text=f'{labels[i]} • {item["name"]}: {value} {data["unit"]}'
                if value==0: add('circle',cx=bx+bw*.45,cy=y(0),r=3,fill=COLORS[j])
            else:
                if previous is not None:
                    add('line',x1=previous[0],y1=previous[1],x2=cx,y2=y(value),stroke=COLORS[j],stroke_width=2,data_series=item['name'])
                add('circle',cx=cx,cy=y(value),r=4,fill=COLORS[j],data_series=item['name'],data_value=value)
                previous=(cx,y(value))
    text(30,445,'Exact supplied values • missing ≠ zero • colors identify series, not favorable performance')
    text(30,table_start,'Category',font_weight='bold')
    col = (width-240)/len(series)
    for j,item in enumerate(series):text(240+j*col,table_start,item['name'],font_weight='bold')
    for i,label in enumerate(labels):
        ty = table_start+28*(i+1)
        text(30,ty,label)
        for j,item in enumerate(series):
            value=item['values'][i]
            text(240+j*col,ty,'missing' if value is None else str(value))
    for i,line in enumerate(source_lines):
        text(30,height-25-20*(len(source_lines)-1-i),line)
    return ET.tostring(root,encoding='unicode')+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path);parser.add_argument('output',type=Path)
    args=parser.parse_args()
    try:
        data=json.loads(args.input.read_text())
        svg=render(data)
    except (ValueError,TypeError,KeyError,OSError) as error:
        parser.exit(2,f'Chart input error: {error}\n')
    args.output.write_text(svg)

if __name__=='__main__': main()
