# Decision Memo: Whom to Email in the Next Campaign

*For a marketing team planning its next email campaign. November 2026. Based on a randomized experiment of 64,000 customers ([Hillstrom, 2008](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html)). The full evidence is in the [technical report](technical_report.md), and the eight original questions are answered in [challenge answers](challenge_answers.md).*

## Decision

**Send the Mens email as widely as the budget allows, and choose customers at random when the number is limited.**

1. **By default, send the Mens email.** It is worth sending to all customers and to each of the three past-purchase audiences.
2. **If only 10,000 customers can be emailed,** send the Mens email to 10,000 drawn at random. **If 10,000 must be left out,** avoid it if possible; otherwise leave out 10,000 drawn at random.
3. **If the Womens email must be used, send it only to customers who bought only women's merchandise.**
4. **Do not adopt model-based targeting yet.** Test it against random selection first, as described under "Next step".

## Why

- **The Mens email pays.** It raised spend by $0.77 per customer over two weeks (95% CI $0.49 to $1.05). At a 40% margin and $0.008 per email, it needs only $0.02 to cover its cost.
- **No targeting method was shown to choose better customers than random selection,** by a test set before the results were seen. On held-out customers, a two-feature rule beat a random 10,000 by $0.12 per customer (95% CI -$1.25 to $1.43), and an uplift model using all seven features by $0.11 (-$1.15 to $1.32). The segment that looked best in training gained $2.27 per customer there, but only $1.37 on held-out data.
- **The Womens email was never shown better than the Mens email.** Among customers who bought only women's merchandise, the two added about the same (Womens $0.63, Mens $0.62 per customer), and both were worth sending. In the other two audiences, the Womens email was at best uncertain under every margin and cost tested.

## What it is worth

- **Emailing a random 10,000 customers earns about $3,000 in profit over two weeks** (95% CI $1,861 to $4,138) at the base case, and between $1,309 and $4,609 across the 16 margin and cost combinations tested. Leaving out a random 10,000 gives up the same amount.
- **The Mens email stays worth sending to customers in general while each email costs less than about $0.15 at a 30% margin, or $0.29 at a 60% margin,** at least 18 times the assumed $0.008. If costs rise above that, revisit the decision.

## Risks and limits

- **The figures describe the average effect, not a forecast for one campaign.** Any one random 10,000 will differ.
- **"Not shown" does not mean "no difference".** The held-out test could detect only gaps of about $1.76 to $1.89 per customer, more than twice the email's average effect. Targeting may help, but this data cannot show it.
- **The data is from 2008 and covers two weeks.** Unsubscribes, email fatigue and long-term value are not measured, and the margin and cost are assumptions.
- **Without a random holdout, results mislead.** In a simulation built from this data, comparing emailed with non-emailed customers, when the emailed were chosen as likely buyers, overstated the effect by up to 69%.

## Next step

**Keep a random no-email group in every campaign, and test targeting against random selection before relying on it.** Randomly assign eligible customers to three groups:

1. No email.
2. The Mens email to a random share of the group.
3. The same share, chosen by an uplift model, which also picks the email.

**Groups 2 and 3 cost the same, so the difference in their incremental profit per customer is the value of targeting.** Size the test from the smallest gain that would pay for building and maintaining a model, not from the gaps seen here, which are within noise.
