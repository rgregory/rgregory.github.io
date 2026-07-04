---
type: note
date: "2026-05-17"
tags: [note, legal, business-law, tax, s-corporation, business-entities]
status: active
created: "2026-05-17"
---

# S-Corporation — Pros and Cons

See [[02-Areas/Learning/Self-Study/Legal-US/Business-Law/2026-05-17 — What Is an S-Corporation|What Is an S-Corporation]] for the full overview.

## Advantages

### 1. Self-Employment Tax Savings (Primary Advantage)
Owner-employees split income into salary + distributions. Only salary is subject to payroll/SE taxes. Distributions escape the ~15.3% SE tax entirely. At meaningful profit levels ($50k+), savings routinely run $5,000–$25,000/year.

### 2. Pass-Through Taxation
No double taxation. Income is taxed once at the individual level. Contrast with C-Corp, where the entity pays corporate tax and shareholders pay again on dividends.

### 3. Personal Liability Protection
S-Corp status (or underlying LLC/Corp) shields personal assets from business debts and lawsuits — same as any corporation or LLC. The business is a separate legal person.

### 4. Credibility and Longevity
Corporations persist beyond ownership changes. An S-Corp can be transferred, sold, or restructured more cleanly than a sole proprietorship or simple LLC. Can be attractive to investors, vendors, or enterprise clients.

### 5. Deductibility of Fringe Benefits (partial)
Owner-employees who own ≤2% of stock can receive employer-paid fringe benefits tax-free. For >2% shareholders, some benefits (health insurance, HSA contributions) are included in W-2 wages but still deductible at the business level.

### 6. Built-in Loss Passthrough
Business losses pass through to owner's personal return, potentially offsetting other income (subject to basis and at-risk rules). Useful in early loss years.

---

## Disadvantages

### 1. Compliance Overhead (Primary Disadvantage)
S-Corps require:
- Separate federal tax return (Form 1120-S)
- Quarterly payroll filings (Form 941)
- Annual W-2 / W-3
- State-level equivalents
- Typically requires a payroll service and a CPA experienced in pass-through entities
- **Cost**: $1,500–$3,500/year in additional professional fees above sole prop / single-member LLC baseline

### 2. Reasonable Compensation Scrutiny
The IRS actively audits S-Corps where owner salaries appear unreasonably low relative to distributions. If flagged, the IRS can reclassify distributions as wages — triggering back taxes, penalties, and interest. Maintaining defensible salary documentation is ongoing work.

### 3. Rigid Eligibility Rules
- 100 shareholder cap (limits equity-based fundraising)
- One class of stock (no preferred shares — makes VC funding nearly impossible; most VC-funded companies must convert to C-Corp)
- No non-resident alien shareholders
- No corporate shareholders

These rules make S-Corps unsuitable for high-growth startups seeking institutional capital.

### 4. State Tax Treatment Varies
Some states don't recognize S-Corp federal election — they tax the entity as a C-Corp at the state level anyway (e.g., California imposes a 1.5% franchise tax on S-Corp net income, minimum $800/year). The federal benefit may be partially or fully offset at the state level depending on domicile.

### 5. Fringe Benefit Limitations for >2% Shareholders
Major shareholders (>2%) cannot receive certain tax-free fringe benefits (group-term life insurance, dependent care assistance, qualified transportation) that C-Corp employees can receive tax-free. These are included in W-2 wages instead.

### 6. Inflexibility in Profit Allocation
All shareholders must receive income in proportion to their ownership percentage. Unlike a partnership or multi-member LLC, you cannot allocate profits/losses disproportionately to different members. This limits creative equity structuring.

### 7. Basis Tracking Complexity
Shareholders must track their "basis" (investment in the company) to determine how much loss they can deduct and whether distributions are taxable. Basis calculations become complex over time, especially with debt, loans, and accumulated losses.

---

## Decision Framework: When to Elect S-Corp vs. Stay LLC

| Scenario | Recommendation |
|---|---|
| Net profit < $40–50k/year | Stay as default LLC. Compliance costs exceed tax savings. |
| Net profit $50–200k/year | Strong candidate for S-Corp election. Savings typically $5k–$20k/year. |
| Net profit > $200k/year | S-Corp saves significantly; get professional guidance on reasonable compensation. |
| Seeking VC / institutional investment | Stay C-Corp. S-Corp eligibility rules incompatible with startup equity structures. |
| Multiple owners with unequal economics | Consider partnership/LLC — S-Corp's equal-allocation rule is a constraint. |
| Business in a state that ignores S-Corp | Run state-specific numbers; federal benefit may be neutralized. |
| Solo consultant / freelancer | Classic S-Corp use case if net income is sufficient. |

---

## The Hidden Trade-Off: Flexibility vs. Tax Efficiency

S-Corp is essentially a **tax optimization vehicle** that trades flexibility for savings. The constraints (shareholder limits, one class of stock, reasonable compensation) are the price of the SE tax arbitrage. Understanding this trade-off is the core analytical frame.

The IRS designed Subchapter S to give small, domestically-owned businesses C-Corp legal protection without C-Corp double taxation — but with guardrails preventing abuse. Every disadvantage above is a guardrail.

## Connections

- [[02-Areas/Learning/Self-Study/Legal-US/Business-Law/2026-05-17 — What Is an S-Corporation|What Is an S-Corporation]] — overview, mechanics, formation
- [[MOC/Legal-US]] — business law context
- [[MOC/Economics]] — incentive design, tax arbitrage mechanics
- Related concept: [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design]] — Subchapter S is a mechanism: desired behavior (small domestic business formation) incentivized via tax structure, with constraints to prevent gaming
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Goodhart's Law|Goodhart's Law]] — "reasonable compensation" rule is a direct Goodhart response: once salary became a tax-minimization target, IRS added the behavioral governor
