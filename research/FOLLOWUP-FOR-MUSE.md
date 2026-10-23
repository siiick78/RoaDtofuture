# Follow-up for Muse: corrections to empresas-h1b.csv

Paste everything below into the session that produced the report. Work on branch `research/h1b-empresas`.
Do not open a pull request.

---

Please correct the H-1B employer data. Do not change any count that is already correct, and show
your work for each change.

## 1. Salary errors (fix or explain each one)
The CSV has salary values that are almost certainly unit errors. Recheck each row against the raw DOL
file, look at WAGE_UNIT_OF_PAY and the original WAGE_RATE_OF_PAY_FROM / _TO values, and correct the
annualization.

| Employer | SOC | Current max | Note |
|---|---|---:|---|
| Citigroup | 13-2051 | 309,250,240 | likely unit error |
| Goldman Sachs | 13-2051 | 416,000,000 | likely unit error |
| Goldman Sachs | 15-2051 | 1,320,000 | check |
| Goldman Sachs | 11-3031 | 950,000 | check |
| Anthropic | 15-2051 | 850,000 | check |
| Anthropic | 13-2051 | median = max = 500,000 | check; a median equal to the max is suspicious |

Also recheck the medians of every row. The report's text said Citigroup pays about $105,000–$130,000,
but the CSV median for Citigroup 13-2051 is 175,000. Use the corrected data and update the report
so the text matches the CSV.

## 2. City and state typos
- Visa: "Foster Cty, CA" should be "Foster City, CA" (check the raw data).
- Databricks: "San Antonio, FL" is probably "San Antonio, TX". Check the raw WORKSITE_STATE. If the
  state is FL in the raw file, keep it and flag it. Do not guess.
- Recount Florida worksite rows after the fix. Report the old and new numbers.

## 3. Consistent sponsorship rule
Apply one rule to every employer, and state it in the report.
- Citigroup: its own CSV row quotes a mirror exclusion ("You will not require sponsorship for U.S. work
  authorization now or anytime in the future"). Currently it is marked as passing. Decide with the same
  rule used for JPMorgan and say why.
- Bank of America and Morgan Stanley: both have exclusions in summer or professional programs. Use the
  same treatment for both.
- American Express: the CSV quotes a mirror that says "may provide visa sponsorship for certain
  positions". Classify it under the same rule and say whether a mirror counts as evidence.
- PayPal: "Must be legally authorized to work" is common boilerplate. Decide whether it counts as an
  exclusion and apply the rule.

## 4. Remitly E-Verify
The CSV marks Remitly as "verificado" for E-Verify. That is based on Remitly's own posting, not on an
E-Verify lookup. Change the field to "autodeclarado" and keep the source in the notes.

## 5. Employer count
The CSV has 21 employers. Bitso and dLocal have zero LCA rows, so they are missing from the CSV. Add
them as rows with zeros, or list them separately in the report, so the count of 23 requested employers
is accounted for.

## 6. Output
- Regenerate `research/empresas-h1b.csv` with the corrections.
- Update `research/empresas-h1b.md` so every number and quote matches the CSV.
- Add a short changelog at the top of the report: what changed, and why.
- Commit to `research/h1b-empresas` and push.

Finish with: rows corrected, rows still unresolved and why, and any count that changed.
