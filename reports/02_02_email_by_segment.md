# Questions 5 and 8: Which Email for Which Customers?

## Questions

5. **Did the Mens version of the e-mail campaign perform different than the Womens version of the e-mail campaign, across various customer segments?**
8. **Which audience would you target the Mens version to, and the Womens version to, given the results of the test? What data do you have to support your recommendation?**

These are quoted from the original challenge. The [segment effects report](02_01_segment_effects.md) tested each segment against no email and mostly pooled the two emails. This report compares the emails directly.

## Approach

**The criteria were [committed and pushed](https://github.com/flora29058486/email-campaign-targeting/commit/3e7dc48) before the analysis was run, but the analysis is exploratory:** it is not in the analysis plan, and some segment results had already been seen. The code is in [`notebooks/02_02_email_by_segment.ipynb`](../notebooks/02_02_email_by_segment.ipynb).

- **Data:** all 64,000 customers. There is no train-test split, because no rule is learned from the data.
- **Question 5:** does the Mens email's lead over the Womens email change across the six segment splits of stage 02? Each is an OLS interaction with HC3 standard errors. A split counts as different if Holm p < 0.05 across six tests.
- **Question 8:** customers form three audiences that do not overlap: bought men's only, women's only, or both. The Mens email, the winner on average, is the default. **An audience switches to the Womens email only if the Womens lead has Holm p < 0.05 across three tests,** so that noise alone does not change the recommendation.
- **Two reference values:** an email against no email is compared with the **$0.02 break-even** (worth sending if the lower end of the 95% interval is above it, under a 40% margin and $0.008 per email). One email against the other is compared with **zero**, because their costs cancel out.
- **If the Womens email must be used,** it is recommended only where it is worth sending.

## Answers

**Question 5: no difference across segments was shown for spend.** The Mens email's lead did not change significantly in any of the six splits. This does not mean the lead is the same everywhere: the tests could reliably detect only changes of about $1.09 to $1.67 between two segments, or $0.46 per spend level, against an average lead of $0.35. Visits did differ by past purchases, but that is descriptive only.

**Question 8: send the Mens email to all three audiences by default. If the Womens email must be used, send it to customers who bought only women's merchandise.** The Mens email is worth sending in each audience. The Womens email is worth sending only among women's-only buyers, where neither email was shown better. Among buyers of both lines the Mens email was better, but that result is fragile. Stage 06 tests these recommendations under other margins and costs.

## Question 5: change in the Mens email's lead (spend)

| Segment split | Change in lead | 95% CI | CI corrected for six tests | Holm p | Verdict |
| --- | ---: | --- | --- | ---: | --- |
| Bought men's: yes vs no | +$0.66 | $0.04 to $1.27 | -$0.17 to $1.48 | 0.22 | Not shown |
| Recency: 1-3 vs 4-12 months | +$0.53 | -$0.18 to $1.24 | -$0.42 to $1.48 | 0.71 | Not shown |
| Past-year spend, per level | +$0.19 | -$0.07 to $0.45 | -$0.16 to $0.54 | 0.71 | Not shown |
| Bought women's: yes vs no | -$0.11 | -$0.74 to $0.52 | -$0.96 to $0.74 | 1.00 | Not shown |
| Web or Multichannel vs Phone | +$0.02 | -$0.60 to $0.63 | -$0.81 to $0.85 | 1.00 | Not shown |
| Zip code: Urban vs Rural | -$0.17 | -$1.12 to $0.77 | -$1.44 to $1.09 | 1.00 | Not shown |

**The first row's uncorrected interval excludes zero, but the result is not significant once six tests are taken into account.** With six true nulls, a p-value as small as its 0.037 would appear about one time in five if the tests were independent. The smallest reliably detectable change was about $1.09 to $1.67, or $0.46 per spend level.

## Question 8: each email by audience (spend)

| Audience | Mens vs no email (95% CI) | Category | Womens vs no email (95% CI) | Category |
| --- | --- | --- | --- | --- |
| Men's only | +$0.68 ($0.25 to $1.12) | Worth sending | +$0.28 (-$0.12 to $0.68) | Uncertain |
| Women's only | +$0.62 ($0.27 to $0.96) | Worth sending | +$0.63 ($0.30 to $0.97) | Worth sending |
| Both | +$1.82 ($0.49 to $3.16) | Worth sending | +$0.16 (-$0.81 to $1.14) | Uncertain |

| Audience | Mens minus Womens (95% CI) | Holm p | Email to send |
| --- | --- | ---: | --- |
| Men's only | +$0.40 (-$0.07 to $0.88) | 0.19 | Mens, by default |
| Women's only | -$0.02 (-$0.42 to $0.39) | 0.94 | Mens, by default |
| Both | +$1.66 ($0.33 to $2.99) | 0.043 | Mens, shown better |

**The result for buyers of both lines says which email suits them, not that they respond more than other customers.** It does not answer question 3, which asks whom to email first.

## Visits and conversion (descriptive)

| Change in the Mens email's lead | Visits, points (95% CI) | Conversion, points (95% CI) |
| --- | --- | --- |
| Bought men's: yes vs no | +6.32 (4.90 to 7.74) | +0.56 (0.17 to 0.95) |
| Bought women's: yes vs no | -4.86 (-6.26 to -3.46) | -0.31 (-0.69 to 0.08) |

**Visits follow the match between the email and past purchases more clearly than spend does.** The intervals for the other four splits include zero on both metrics. These metrics are uncorrected and decide neither question.

## Checks added after the results were seen

- **Worth sending:** all four categories hold with intervals corrected for six comparisons. The Mens email among buyers of both lines holds narrowly (lower end $0.028 against $0.02).
- **The one significant lead is fragile.** It rests on 53 buyers with the Mens email and 31 with the Womens email. A permutation test agrees with it, but without the single largest Mens purchase Holm p rises to about 0.075, and with all nine tests corrected as one family it is 0.13.

## Limitations

- **Exploratory:** segment results had been seen before the criteria were set, so confirmation needs new data.
- **Low power:** "not shown" mostly reflects wide intervals, and a significant result from so few buyers is likely to be overstated.
- **Overlapping splits:** the six question 5 splits share customers, so they are not independent evidence.
- **As in earlier stages:** effects are of assignment rather than reading, outcomes cover two weeks, spend may be capped at $499, and the data is from 2008.
