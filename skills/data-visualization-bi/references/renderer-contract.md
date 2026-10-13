# Local chart renderer

Python 3, no packages, network, private service or installation required. From this skill directory:

```sh
python3 scripts/render_chart.py supplied-data.json chart.svg
```

Input is JSON with `kind` (`bar` or `line`), nonempty `title`, `unit`, `period`, `source`, unique category `labels` and 1–4 named `series`, each with aligned `values`. Values are finite numbers or `null`. Example syntax, with synthetic data for teaching only:

```json
{"kind":"line","title":"Synthetic example","unit":"USD","period":"Q1","source":"explicit synthetic fixture","labels":["Jan","Feb","Mar"],"series":[{"name":"Operating profit","values":[0,null,-10]}]}
```

Validate comparability before rendering: entity/scope, observation period, currency/unit/scale, accounting basis, tax, actual/plan status and version. A common unit is required; do not put a cash stock on a flow axis or invent profit from incomparable revenue/cost. Calendar periods must already be aligned: insert null for missing expected periods, never interpolate. Supplied order is preserved. The renderer does not validate accounting semantics, aggregate raw records or calculate a profit stage.

The chart includes a zero reference, signed negative bars, breaks line segments at null, marks observed zero, provides exact values and a source label. All-null is an empty state, distinct from all-zero. Colors identify series; favorable/unfavorable judgment requires a supplied rule. A zero/missing comparison base has no percentage change; negative-base percentage uses absolute baseline and must be disclosed rather than implying ordinary growth. Use the exact values alongside any rounding.

Ceilings: 30 categories and 4 comparable series. Maximum character counts are title 90, unit 30, period 50, category label 24 and series name 22. Longer fields are rejected with shortening guidance. Preserve qualifiers in the source text and provide a separate full-label mapping when abbreviating; do not remove accounting scope or uncertainty to fit. Source text wraps automatically.

Static grouped bar or line only, no mixed bar/line, filters, stacked/waterfall/pie/map, automatic date inference or statistical modelling. Split dense views, or use a verified available tool. Keep an SVG scrollable at native width rather than shrinking unreadably. Visual inspection is still required. XML text is escaped by the serializer. A completed SVG is an actual chart; it does not establish that an interactive dashboard was implemented or tested.
