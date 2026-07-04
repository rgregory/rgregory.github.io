---
type: note
date: "2026-04-28"
tags: [auction-theory, mechanism-design, game-theory, economics, incentive-compatibility]
status: filed
area: "[[02-Areas/Learning/Self-Study/Economics]]"
created: "2026-04-28"
---

# Auction Theory

Auction theory is the economic study of mechanisms for allocating goods when the seller doesn't know buyers' valuations in advance. It's the practical face of mechanism design: instead of asking "what game will produce truth-telling?", auctions ask "what game will extract maximum revenue *and* allocate efficiently to the buyer who values the item most?"

The elegance of auction theory lies in its counterintuitive core: different auction formats (English, Dutch, first-price sealed-bid, second-price sealed-bid) that *seem* structurally different produce equivalent outcomes — unless you account for information and risk.

---

## Standard Auction Formats

### English (Ascending Bid) Auction

Auctioneer starts at a low price and gradually raises it. Buyers drop out as prices rise. Last bidder wins at the price they beat the second-to-last bidder at.

**Incentive structure**: Buyers bid truthfully (up to their valuation). If your valuation is $50, you keep bidding as long as price is below $50 and stop when it hits $50. You have no incentive to bid higher (you lose money) or lower (you lose the item if you're the highest-value buyer).

**Outcome**: Winner pays approximately the second-highest valuation. This is not coincidence — it's by design of the mechanism.

### Dutch (Descending Bid) Auction

Auctioneer starts at a high price and gradually lowers it. First bidder to accept wins at the current price.

**Incentive structure**: Each buyer faces a timing decision: accept now or wait for a lower price? A bidder with valuation $50 must decide whether the risk of someone else accepting first is worth waiting for a lower price. The optimal strategy involves probabilistic mixing: higher-valuation buyers should bid earlier on average.

**Outcome**: Strategically equivalent to first-price sealed-bid (see below), despite the different structure. The Dutch auction equilibrium produces the same expected prices and revenue as first-price sealed-bid.

### First-Price Sealed-Bid Auction

Each buyer submits a bid privately. Highest bidder wins and pays what they bid.

**Incentive structure**: No incentive to bid truthfully. If your valuation is $50 and you think the highest competitor will bid $30, bidding $49 wins and leaves you with $1 surplus. But bidding $51 wins for $1 surplus... wait, that's the same. The key: you want to bid just barely above the second-highest bid, but you don't know what it will be. So you shade your bid: bid less than your valuation, reflecting the risk that you overbid and waste surplus.

**Outcome**: Sellers earn less revenue than in English auctions (because winners shade their bids), but the item still goes to the highest-valuation buyer.

### Vickrey (Second-Price Sealed-Bid) Auction

Each buyer submits a bid privately. Highest bidder wins and pays what the *second*-highest bidder bid.

**Incentive structure**: Truth-telling is a *dominant strategy*. If your valuation is $50:
- If you bid $50 and win, you pay the second price (some amount ≤ $50), so you make non-negative surplus
- If you bid $50 and lose, someone else valued it more than $50 — that's fine, you were going to lose anyway
- If you bid higher than $50 and win, you pay more than your valuation — you lose money
- If you bid lower than $50, you might lose when you should have won (the second price was below $50)

Therefore: bidding truthfully is optimal regardless of what others bid.

**Historical significance**: Vickrey discovered this in 1961. The mechanism became famous precisely because dominant-strategy truth-telling seemed to violate the intuition that auctions involve strategic shading. It doesn't — the mechanism design makes honesty dominant.

**Outcome**: Seller revenue equivalent to English auction in private-value environments (buyer valuations are independent). Allocatively efficient: item goes to highest-valuation buyer.

---

## Revenue Equivalence Theorem

**Vickrey-Clarke-Groves (VCG) Insight**: Under mild conditions (private values, risk neutrality, bidders know their own valuations), the English, Dutch, first-price sealed-bid, and second-price sealed-bid auctions all produce *expected* revenue. The auction format doesn't matter for revenue if you condition on the equilibrium allocation.

**Why?** Because the expected payment is determined by the allocation rule and the monotonicity of bidding strategies. If higher-valuation bidders always win, then the expected payment from the winner is determined by the distribution of second-highest valuations — regardless of the mechanism.

**Caveats**:
- Risk aversion breaks equivalence: risk-averse bidders bid higher in first-price auctions (more certain outcomes) than Dutch or second-price auctions
- Common values (where bidders' valuations are interdependent, e.g., an oil field) break equivalence: different formats produce different information revelation and thus different prices
- Endogenous entry (bidders decide whether to participate) breaks equivalence: different formats attract different numbers of bidders

---

## Bidding Strategies and Equilibrium

### Dominant Strategies

In a second-price auction, truthful bidding is dominant: optimal regardless of others' bids.

In first-price and Dutch auctions, there is no dominant strategy — your optimal bid depends on your belief about others' valuations.

### Symmetric Equilibria

When bidders are ex-ante identical (same distribution of valuations), equilibrium bidding is often symmetric: all bidders follow the same strategy function $\beta(v)$, where $\beta$ is increasing in valuation $v$.

In equilibrium, if your valuation is $v$, you bid $\beta(v)$. The probability you win is the probability your valuation is the highest. Expected payoff is strictly decreasing in your bid: bidding higher increases win probability but decreases surplus if you win.

For first-price auctions with uniformly distributed valuations on $[0, 1]$, the symmetric equilibrium bid function is:

$$\beta(v) = \frac{n-1}{n} v$$

where $n$ is the number of bidders. You shade your bid by a factor proportional to how much competition there is.

---

## Optimal Auction Design

**Myerson (1981)**: What auction format maximizes the seller's expected revenue?

The answer: the **revelation principle** tells us that any outcome achievable by any mechanism is achievable by a truthful mechanism. So the optimal auction must induce truth-telling.

**Myerson's optimal auction**:
1. Ask each bidder for their valuation
2. Allocate to the highest bidder *if and only if* their valuation exceeds a reserve price
3. The winner pays the reserve price if it's higher than the second-highest bid, otherwise pays the second-highest bid

**Intuition**: Reserve prices screen out low-valuation bidders and force high-valuation bidders to reveal their true valuations in order to win. The optimal reserve price balances allocation efficiency (giving the item to the highest bidder) against extraction of surplus (sellers want to extract payment close to buyers' valuations).

**Seller's Revenue Optimization**: The seller faces a trade-off:
- Too low a reserve: you're allocating efficiently but leaving money on the table (high-valuation buyers would pay more)
- Too high a reserve: you're extracting from high bidders but sometimes failing to sell at all (lower expected revenue)

The optimal reserve depends on the distribution of valuations. If you expect very high valuations, set a high reserve. If you expect low valuations, set a low reserve.

---

## Case Study: FCC Spectrum Auctions

The U.S. Federal Communications Commission auctioned radio spectrum (licenses to use specific frequency bands) in the 1990s. This is a watershed moment in applied mechanism design.

**Background**: Spectrum had previously been allocated through comparative hearings (regulators decided who got licenses) or random lotteries. Both produced inefficiency: politically connected firms got licenses they didn't value most, and random allocation was clearly wasteful.

**The mechanism (Milgrom-Wilson design)**:
- Simultaneous ascending (SMRA): multiple items auctioned in parallel; bidders bid on multiple items in rounds; prices rise with each round until all bidders stop bidding
- Designed to handle complementarities: adjacent frequency bands are more valuable together (national coverage is better than scattered bands)
- Prevents the "exposure problem" where a bidder bids on bands A and B separately, wins A, then loses B and has to keep A even though they only value it in combination with B

**Outcomes**:
- First auction (1994): $617 million raised for 99 spectrum licenses
- Revealed that valuations were very high (licenses were undervalued in prior estimates)
- Subsequent auctions raised billions; the U.S. Treasury collected over $20 billion in spectrum auction revenue over decades
- Allocative efficiency: licenses went to firms that valued them most (firms that could build networks using them most productively)

**Mechanism design lesson**: The choice of auction format (simultaneous ascending vs. sealed-bid, with or without reserves, with or without activity rules) *directly* determined the revenue and allocation. The same spectrum, under a worse mechanism, would have raised far less and might have been allocated to firms that couldn't use it effectively.

---

## Complications and Extensions

### Common Values and the Winner's Curse

In auctions where the good's value is not idiosyncratic to the buyer (e.g., an oil field, a business acquisition), valuations are correlated: if one bidder thinks the oil field is valuable, likely other bidders think so too.

**The winner's curse**: The winning bidder pays their bid, but the item's true value (revealed later) often turns out to be lower than the winning bid. Why? Because the winner only wins when they bid highest — and the highest bid is an optimistic signal about the item's value. But when the item's value is revealed, the optimism is partly disproven.

**Rational bidders account for this**: They shade their bids to account for the fact that winning signals they were the most optimistic, and perhaps too optimistic. But inexperienced bidders might not account for the winner's curse and overbid.

**Empirical example**: Oil field auctions in the U.S. showed the winner's curse in action. Firms would win bids at prices that, in hindsight, were above the fields' productive value. Over time, firms learned to shade more aggressively.

### Multi-Unit Auctions

Many practical auctions involve multiple identical (or differentiated) items: Treasury bills, spectrum licenses, airline slots, etc.

**Challenges**:
- Bidder demand curves: a bidder might want 1 item at $50 but 2 items only if the second is cheaper (decreasing willingness to pay)
- Reduction from multi-unit to single-unit: sometimes you can reduce multi-unit auctions to single-unit analysis by treating bundles as separate goods
- Combinatorial auctions: when items are complements or substitutes, the space of possible bundles explodes

**Design**: The simultaneous ascending auction (used for spectrum) is one answer; another is the Vickrey-Clarke-Groves (VCG) auction generalized to multiple items, which is truthful but sometimes produces losses for the seller.

### Strategic Bidding and Collusion

If the same bidders participate in many auctions (e.g., construction firms bidding repeatedly on public contracts), they might form implicit or explicit cartels to suppress competition.

**Antitrust angle**: Bid-rigging (explicit collusion) is illegal. But detecting it in data is hard. Auctions are high-stakes settings where rational firms might be tempted to collude rather than compete.

**Mechanism design for collusion prevention**: Some auction designs are more robust to collusion than others. Sealed-bid auctions with no communication are harder to rig than English auctions (where bidders can observe rivals' behavior and implicitly signal). But no format is collusion-proof if bidders can communicate.

---

## Connections to Mechanism Design Foundations

Auctions are the clearest applied instance of mechanism design: you're designing an institution (the auction rules) to elicit information (valuations) and allocate a good to the agent who values it most, while extracting revenue.

The mechanisms that work best (second-price, optimal with reserve) share a key property: **incentive compatibility** — agents' dominant strategy is to reveal their true type (valuation). See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] for the formal framework (IC/IR constraints, revelation principle, VCG mechanisms).

**Truth-telling as dominant strategy** is precisely what Vickrey designed for in the second-price auction. It's also what Myerson's revenue-optimal auction ensures. The mechanism's design choice directly determines whether bidders have incentive to be honest.

**Contrast to other applications**: See [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]] (where stability matters more than revenue) and [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Shapley Value|Shapley Value]] (where fairness axioms determine allocation) to understand how mechanism design adapts to different objectives.

---

## Key Insights

1. **Revenue equivalence is not magical**: Different auction formats produce equivalent revenue because the allocation rule (highest bidder wins) determines the expected payment. The format matters for risk aversion, information revelation, and collusion resistance.

2. **Mechanism design is applied**: The FCC spectrum auction showed that clever mechanism design can extract billions of dollars and improve allocation. This isn't theoretical — it's a direct application of game-theoretic reasoning to real institutions.

3. **Bidding strategies depend on format**: First-price auctions induce bid shading (you bid less than your valuation); second-price auctions induce truth-telling; English auctions induce a dynamic process where you learn others' valuations over time.

4. **Seller's revenue depends on information**: If the seller doesn't know valuations, they must design mechanisms that elicit truthful information. The mechanism that elicits information best also extracts the most revenue.

5. **Auction design matters for fairness and efficiency**: Spectrum licenses, school seats, organ donations — wherever auctions are used to allocate scarce goods, the mechanism choice affects both who gets what and how much they pay. This has real distributional consequences.

---

## Sources

- **Milgrom — Putting Auction Theory to Work (2004)** — The bridge between theory and FCC spectrum auction practice; accessible with technical depth
- **Myerson — Optimal Auction Design (1981)** — The foundational paper on revenue-optimal auction design
- **Vickrey — Counterspeculation, Auctions, and Competitive Sealed Bids (1961)** — The original second-price auction paper
- **Osborne, Game Theory** — Auction chapters cover theory and strategy

---

## Connections

- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Game Theory and Economics|Game Theory and Economics]] — Parent context; auctions as a key application of mechanism design
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Mechanism Design Foundations|Mechanism Design Foundations]] — The formal framework (incentive compatibility, revelation principle, dominant strategies) that auctions instantiate
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Matching Markets|Matching Markets]] — Complementary mechanism design application: two-sided matching instead of single-good allocation
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Shapley Value|Shapley Value]] — Fair division in coalitional games; connects to auction theory's fairness concerns (who deserves to win? how should surplus be split?)
- [[02-Areas/Learning/Self-Study/Economics/2026-04-28 — Nash Equilibrium Formal Definition|Nash Equilibrium: Formal Definition & Core Examples]] — Equilibrium analysis of bidding strategies in auctions
- [[02-Areas/Learning/Self-Study/Economics/2026-04-16 — Goodhart's Law|Goodhart's Law]] — Auction design failure mode: if you optimize for revenue, you might design a mechanism that works in equilibrium but not in practice (bidders game the system in unanticipated ways)
