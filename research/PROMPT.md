# Research prompt: verified H-1B sponsor list

Paste everything below the line into a NEW session that has network access.
Before starting, allow these domains in Network access: `dol.gov`, `uscis.gov`, `ice.gov`,
`e-verify.gov`, and the career-site domains listed in `research/SOURCES.md`.

---

You are a research analyst. Your job is to verify, using official sources, which employers
actually sponsor H-1B visas for the candidate profile below. Work rigorously. If you cannot
verify a fact, mark it NOT VERIFIED. Do not invent, estimate, or fill gaps. Write the output in Spanish.

## Candidate profile (use only to filter; never copy personal identifiers into any file)
- F-1 student in Miami, Florida.
- Program: MBA in Artificial Intelligence, Atlantis University, CIP code 11.0102.
  Start: September 9, 2026. End: September 9, 2028.
- Plan: OPT after the program, STEM OPT if the CIP code qualifies, first H-1B lottery March 2029.
- Experience: university admissions, student records, accounts payable, technical support, sales.
- Languages: Spanish (native), English (professional).
- Target roles: financial analyst, risk analyst, compliance analyst (AML/KYC), data analyst,
  financial operations analyst, at banks, payments companies, fintechs, or AI companies.
- Location: Miami/Florida, or remote within the US.

## Official sources, in this order
1. **DOL OFLC LCA Disclosure Data**, fiscal years FY2024, FY2025, FY2026.
   Start at https://www.dol.gov/agencies/eta/foreign-labor/performance and download each year's file.
2. **USCIS H-1B Employer Data Hub** (uscis.gov). Use it for I-129 approvals and initial employment by employer.
3. **E-Verify** (e-verify.gov). Confirm the employer participates. If no public lookup exists for that employer, mark it "not verifiable".
4. **DHS STEM Designated Degree Program List**, latest version, from ice.gov. Check whether CIP 11.0102 is listed. Also note any 52.xxxx business codes for comparison.
5. **Each employer's careers site.** Read relevant postings for sponsorship language ("sponsorship", "visa", "work authorization", "will not sponsor"), and check for internship or early-career programs.

Blogs, aggregators, and "visa sponsor" websites (for example MigrateMate, MyVisaJobs, Ellis, h1bdata) are NOT valid sources.
You may use them only as leads, and you must label them as leads.

## Employers to check (starting list, not exhaustive)
- Banks and finance: Citigroup, JPMorgan Chase, Bank of America, Wells Fargo, Goldman Sachs, Morgan Stanley, Capital One, American Express.
- Payments and fintech: Visa, Mastercard, PayPal, Stripe, Affirm, Remitly, dLocal, Bitso.
- AI and data: Databricks, Snowflake, Palantir, OpenAI, Anthropic.
- Universities in Miami (cap-exempt): University of Miami, Florida International University.
- Add any other employer with a Miami or Florida worksite that appears in the LCA data for the target roles. Record how you found it.

## Steps for each employer
1. Filter the LCA data by legal name and variants (for example "Citigroup Global Markets" and "Citibank N.A."). List every variant you used.
2. Count certified LCAs in FY2024, FY2025, and FY2026 for these SOC codes:
   - 13-2051 Financial analysts
   - 13-1111 Management analysts
   - 15-2051 Data / BI analysts
   - 13-2054 Financial risk specialists (if present)
   - 13-1041 Compliance officers
   - 11-3031 Financial managers / administrative operations (if present)
3. From the same rows, record: job title, worksite city, offered annual wage (minimum, median, maximum), and whether the worksite is in Florida.
4. Check I-129 approvals and initial-employment counts for the latest year on the USCIS Employer Data Hub.
5. Confirm E-Verify participation.
6. Check the careers site. Copy any sponsorship language word for word, with the URL and the date you checked.
7. Note whether the employer offers internships or early-career roles open to F-1 students (CPT/OPT), with the URL.

## Inclusion rule
An employer goes in the final list only if it meets all four conditions:
(a) it has certified LCAs in FY2024–FY2026 for at least one target SOC code;
(b) it has documented wages in those LCAs;
(c) it is confirmed in E-Verify, or no public lookup exists and that is marked as such;
(d) its careers site does not exclude sponsorship for similar roles, or it states sponsorship explicitly.
Employers that fail go in a separate section, each with the exact reason.

## Rules
- Do NOT include SEVIS numbers, dates of birth, addresses, phone numbers, or email addresses in any output.
- Do NOT say an employer "guarantees" sponsorship or STEM OPT. Cap exemption does not guarantee that a role qualifies as a specialty occupation.
- Do NOT present aggregator figures as DOL figures.
- If a source fails (403, DNS error, timeout), do NOT substitute another source. Record in the report the source name, URL, exact error, and date. Then continue with the other sources.
- Do NOT publish to GitHub Pages. Do NOT open a pull request.

## Deliverables
1. `research/empresas-h1b.csv` with these columns:
   empresa | nombres_legales_usados | SOC | LCA_FY2024 | LCA_FY2025 | LCA_FY2026 | titulo_puesto | ciudad | salario_min | salario_mediana | salario_max | I129_ultimo_año | empleo_inicial | E-Verify (verificado / no_verificable / no) | URL_carreras | lenguaje_patrocinio (cita textual) | practicas_F1 | nivel_confianza | fuente_DOL | fecha_consulta
2. `research/empresas-h1b.md`, in Spanish, with:
   - A five-line summary.
   - A table of employers that passed, ordered by strength of evidence.
   - A section listing excluded employers and the exact reason for each.
   - A section listing sources that failed, with URL, error, and date.
   - A section on CIP 11.0102: whether it appears on the STEM list, with the link and the list's date.
   - A section on the current H-1B lottery rules (wage-level weighting, fees), with links and dates.
3. Commit both files to branch `research/h1b-empresas`, created from `main`, and push. Do not open a pull request.

Finish your reply with: how many employers passed, how many are not verifiable, which official sources you could not open, and whether CIP 11.0102 appears on the STEM list.
