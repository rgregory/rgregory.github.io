---
type: note
date: "2026-05-17"
tags: [note, legal, business-law, tax, s-corporation, business-entities]
status: active
created: "2026-05-17"
---

# What Is an S-Corporation

## Definition

An S-Corporation (S-Corp) is not a distinct legal entity type — it is a **federal tax election** made by an existing corporation or LLC. The "S" refers to Subchapter S of the Internal Revenue Code. Any qualifying corporation files IRS Form 2553 to elect S-Corp status; after that, the entity retains its state-level legal form (typically a C-Corp or LLC) but is taxed differently.

The key legal reality: S-Corp status is invisible to state governments. The state sees a corporation or LLC. Only the IRS sees an S-Corp.

## How It Differs from Other Structures

| Structure | Legal Form | Tax Treatment | Liability Shield |
|---|---|---|---|
| Sole Proprietorship | None (owner = business) | Schedule C (pass-through) | None |
| Single-member LLC | LLC | Schedule C (default pass-through) | Yes |
| Partnership / Multi-member LLC | LLC or Partnership | Schedule K-1 (pass-through) | Yes |
| C-Corporation | Corporation | Corporate tax + dividend tax (double taxation) | Yes |
| **S-Corporation** | Corporation or LLC + IRS election | Pass-through (like partnership) | Yes |

### vs. C-Corporation
- C-Corp pays corporate income tax (~21% federal), then shareholders pay tax again on dividends — **double taxation**
- S-Corp eliminates the corporate layer: profits flow directly to shareholders' personal returns, taxed once

### vs. LLC (default)
- Single-member LLC default: all net income is subject to **self-employment (SE) tax** (~15.3% on first ~$170k, 2.9% above)
- S-Corp election allows the owner-employee to split income into: (1) reasonable salary (subject to payroll taxes) and (2) distributions (NOT subject to SE tax)
- The distribution portion escapes SE tax entirely — this is the primary financial motivation

### vs. Partnership
- Both use pass-through taxation
- S-Corp adds the salary/distribution split advantage over general partnerships
- S-Corp has stricter eligibility rules (see below)

## Eligibility Requirements (IRS Rules)

To qualify for S-Corp election, the entity must:

1. **Be a domestic corporation** — no foreign corporations
2. **Have only allowable shareholders** — individuals, certain trusts, and estates; no partnerships, corporations, or non-resident alien shareholders
3. **Have 100 or fewer shareholders**
4. **Have only one class of stock** — all shares must have identical distribution and liquidation rights (though voting rights may differ)
5. **File Form 2553** — must be filed by March 15 of the tax year it applies to (or within 75 days of formation for new entities)

## The Self-Employment Tax Arbitrage (Core Mechanic)

This is why most small business owners elect S-Corp status.

**Scenario**: Business owner generates $200,000 in net profit.

| Structure | SE Tax Exposure | Approximate SE Tax Owed |
|---|---|---|
| Sole Proprietor / Single-member LLC | 100% of profit | ~$28,000 |
| S-Corp (salary $80k, distribution $120k) | Only the $80k salary | ~$12,000 |

**Savings**: ~$16,000/year in this example.

**The constraint**: The IRS requires owner-employees to pay themselves a **"reasonable compensation"** salary. You cannot set salary to $0 and take everything as distributions. The IRS scrutinizes this. "Reasonable" = what you'd pay someone to do your job in the open market.

## Formation Path

1. Form a corporation (or LLC) at the state level
2. Obtain an EIN (Employer Identification Number)
3. File IRS Form 2553 (Election by a Small Business Corporation)
4. Set up payroll for owner-employee salary
5. File quarterly payroll taxes (Form 941), annual payroll forms (W-2, W-3)
6. File annual S-Corp return (Form 1120-S) + Schedule K-1 to each shareholder

## Key Tax Forms

| Form | Purpose |
|---|---|
| Form 2553 | One-time S-Corp election |
| Form 1120-S | Annual S-Corp income tax return |
| Schedule K-1 | Each shareholder's share of income/loss (attached to personal return) |
| Form 941 | Quarterly payroll tax deposits |
| W-2 | Owner-employee annual wage statement |

## Common Misconceptions

- **"S-Corp is a legal entity"** — No. It's a tax classification. The legal entity is the underlying corporation or LLC.
- **"S-Corps pay no taxes"** — Income passes through to owners who pay personal income tax. Some states also levy a franchise tax or minimum tax on S-Corps.
- **"You can set salary to $1 to minimize taxes"** — No. IRS "reasonable compensation" doctrine. Penalties apply for unreasonably low salaries.
- **"Any business can elect S-Corp"** — Eligibility rules disqualify non-resident alien owners, corporations-as-shareholders, and entities with more than one class of stock.

## When It Typically Makes Financial Sense

The break-even point for S-Corp election is generally around **$40,000–$50,000 in net profit**, because the compliance costs (payroll service, separate tax return, accountant fees) typically run $1,500–$3,000/year. Below that threshold, the SE tax savings don't outweigh the overhead.

Above ~$50k net profit, the savings compound year over year.

## Connections

- [[MOC/Legal-US]] — US legal system; business law fits under Contract Law and regulatory frameworks
- [[MOC/Economics]] — Tax arbitrage is a mechanism design / incentive structure problem; connects to Goodhart's Law (IRS reasonable compensation rule as a behavioral governor)
- Related concept: [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design]] — the IRS "reasonable compensation" rule is a direct example of mechanism design constraining strategic behavior
