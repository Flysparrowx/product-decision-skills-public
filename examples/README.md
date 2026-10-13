# Three independent examples

All inputs are synthetic. These are sanitized outputs from earlier independent installed-skill model executions, reused for this draft. The CPO and Microgroup prompts contain their complete supplied facts; BI uses supplied.json. They are not new model runs or a full regression. Current packaging checks compare the skill bytes with the earlier executed candidate and separately verify copying and local scripts.

| Skill | Supplied prompt / input | Prior model output |
|---|---|---|
| CPO | [prompt](cpo/prompt.txt) | [decision brief](cpo/output.md) |
| Microgroup | [prompt](microgroup/prompt.txt) | [context pack](microgroup/output.md) |
| BI | [prompt](bi/prompt.txt), [input](bi/supplied.json) | [output](bi/output.md), [chart](bi/chart.svg) |

CPO retains email reminders pending evidence for SMS. Microgroup preserves the contradictory app-booking observation and returns insufficient evidence. BI preserves supplied 10/null/0/−2 observations, a missing-data gap and one final connecting segment. Earlier executions used an isolated Codex CLI installation; host behavior may differ elsewhere.
