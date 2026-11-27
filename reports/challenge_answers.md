# Answers to the Challenge Questions

The [MineThatData E-Mail Analytics and Data Mining Challenge](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html) (Kevin Hillstrom, 2008) asked eight questions about its email experiment. They are quoted verbatim below, each followed by this project's answer and the reports behind it. **Amounts are incremental spend per customer over the two weeks after the campaign, and profit assumes a 40% margin and $0.008 per email,** a base case that [stage 06](06_01_profit_sensitivity.md) varies. The full argument is in the [technical report](technical_report.md).

## 1. Which campaign performed better?

> Which e-mail campaign performed the best, the Mens version, or the Womens version?

**The Mens email.** It raised spend by $0.35 per customer more than the Womens email (95% CI $0.03 to $0.66, Holm p = 0.031), and it also led on visits and conversion. **Its lead on spend is significant but imprecisely estimated.**

Source: [average effects](01_01_average_effects.md).

## 2. How much did each campaign add?

> How much incremental sales per customer did the Mens version of the e-mail campaign drive? How much incremental sales per customer did the Womens version of the e-mail campaign drive?

**About $0.77 per customer for the Mens email (95% CI $0.49 to $1.05) and $0.42 for the Womens email ($0.17 to $0.68),** over the two weeks after the campaign. Customers with no email spent $0.65 on average.

Source: [average effects](01_01_average_effects.md).

## 3. Whom to email if only 10,000 can be

> If you could only send an e-mail campaign to the best 10,000 customers, which customers would receive the e-mail campaign? Why?

**Send the Mens email to 10,000 customers drawn at random from all 64,000.**

- **The Mens email did best on average:** +$0.77 per customer (95% CI $0.49 to $1.05), against a break-even of $0.02 at the base case.
- **No list was shown to choose better customers.** A list would replace random selection only if it passed a threshold set before testing. On held-out data, the segment rule beat a random 10,000 by $0.12 per customer (-$1.25 to $1.43) and [the uplift model](04_01_uplift_models.md) by $0.11 (-$1.15 to $1.32). In a check added later, against the test-half average, both gaps rise to $0.51, and both intervals still include zero.
- **This does not mean that all customers respond equally,** only that this data could not identify the best 10,000.
- **It pays:** under every margin and cost tested in [stage 06](06_01_profit_sensitivity.md), this earns a profit, about $3,000 over two weeks at the base case.

Sources: [targeting rule](03_01_targeting_rule.md), [uplift models](04_01_uplift_models.md), [profit and sensitivity](06_01_profit_sensitivity.md).

## 4. Whom to suppress if 10,000 must be left out

> If you had to eliminate 10,000 customers from receiving an e-mail campaign, which customers would you suppress from the campaign? Why?

**Avoid suppressing if possible. If 10,000 customers must be suppressed, choose them at random.**

- **Suppressing costs money.** Suppressing a random 10,000 from the Mens email would give up about $7,700 in sales and $3,000 in profit (95% CI $1,900 to $4,100) over two weeks at the base case, and an estimated $1,300 or more under every margin and cost tested in [stage 06](06_01_profit_sensitivity.md).
- **No list was shown to give up less.** No list passed the same threshold: compared with a random 10,000, the segment rule's list gave up $0.56 less per customer (-$1.03 to $2.27) and [the uplift model's](04_01_uplift_models.md) $0.45 less (-$0.91 to $1.90). A later check showed that most of these gaps came from that one random draw: against the test-half average, they are $0.22 and -$0.01, and both intervals still include zero.
- **This rests on the average effect:** on the test half, six of seven customer cells are uncertain.

Sources: [targeting rule](03_01_targeting_rule.md), [uplift models](04_01_uplift_models.md), [profit and sensitivity](06_01_profit_sensitivity.md).

## 5. Did the comparison differ by segment?

> Did the Mens version of the e-mail campaign perform different than the Womens version of the e-mail campaign, across various customer segments?

**Not shown for spend.** The Mens email's lead did not differ significantly across any of six segment splits after correction. The largest change, between customers who had and had not bought men's merchandise, was +$0.66 (Holm p = 0.22). **This does not mean the lead is the same everywhere:** the tests could reliably detect only changes of about $1.09 to $1.67 between two segments. Visits differed by past purchases, but that is descriptive only. This analysis is exploratory, with criteria committed before it was run.

Source: [email by segment](02_02_email_by_segment.md).

## 6. Did the results differ by metric?

> Did the campaigns perform different when measured across different metrics, like Visitors, Conversion, and Total Spend?

**The Mens email leads on all three:** by $0.35 per customer in spend, 3.14 percentage points in visits and 0.37 points in conversion. **By segment the metrics differ:** [visits vary with past purchases, while no difference was shown for spend](02_02_email_by_segment.md). Visits and conversion are supporting evidence, because they are not corrected for multiple testing.

Sources: [average effects](01_01_average_effects.md), [email by segment](02_02_email_by_segment.md).

## 7. Anomalies

> Did you observe any anomalies, or odd findings?

**Yes, three:**

- Spend stops at exactly $499 for 12 buyers, which may indicate a cap.
- No customer under $200 of past-year spend bought both men's and women's merchandise.
- 6,562 rows exactly repeat an earlier row.

**The causes of the first two are unknown.** The repeated rows are kept, because without a customer ID they cannot be told apart from different customers with the same values. Checks of the random assignment found no evidence of a problem.

Sources: [EDA summary](00_01_eda_summary.md), [experiment validity](00_02_experiment_validity.md).

## 8. Which audience for each email

> Which audience would you target the Mens version to, and the Womens version to, given the results of the test? What data do you have to support your recommendation?

**Send the Mens email to all three past-purchase audiences by default. If the Womens email must be used, limit it to customers who bought only women's merchandise.**

| Past purchases | Mens email (95% CI) | Womens email (95% CI) | Mens minus Womens (95% CI) |
| --- | --- | --- | --- |
| Men's only | **+$0.68 ($0.25 to $1.12)** | +$0.28 (-$0.12 to $0.68) | +$0.40 (-$0.07 to $0.88) |
| Women's only | **+$0.62 ($0.27 to $0.96)** | **+$0.63 ($0.30 to $0.97)** | -$0.02 (-$0.42 to $0.39) |
| Both lines | **+$1.82 ($0.49 to $3.16)** | +$0.16 (-$0.81 to $1.14) | +$1.66 ($0.33 to $2.99) |

*Bold: worth sending at the base case, meaning the lower end of the interval is above the $0.02 break-even.*

- **The Mens email is worth sending in each audience,** in at least 14 of the 16 margin and cost combinations of [stage 06](06_01_profit_sensitivity.md).
- **It beat the Womens email only among buyers of both lines,** a fragile exploratory result: it rests on 53 and 31 buyers.
- **Among women's-only buyers, the Womens email is also worth sending** (15 of 16 combinations), and neither email was shown better. In the other two audiences, it was never worth sending.

Sources: [email by segment](02_02_email_by_segment.md), [profit and sensitivity](06_01_profit_sensitivity.md).
