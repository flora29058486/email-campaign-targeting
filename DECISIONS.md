# Decision Log

A dated record of the analytical decisions in this project, including ideas I dropped and mistakes I corrected.

> This log was compiled on November 3, 2026 from my working conversations with Claude, an AI assistant that wrote most of the code and report drafts. Each entry records what was actually discussed, who raised the point, and what I decided. I reviewed every entry.

## 2026-11-01

### Zero spend and repeated rows are kept
- **Context:** 99.1% of customers spent nothing, and 6,562 rows exactly repeat an earlier row. There is no customer ID.
- **Decision: keep all 64,000 rows.** Zero spend means no purchase, not missing data. Analyzing buyers only would compare groups after the email may have changed who buys, which breaks the randomization.
- **Follow-up:** I asked whether the repeated rows were the same customers or different customers with identical values. Claude ran a shuffle test: shuffling each column independently produced almost the same number of repeats, so chance alone can explain them. I decided not to add this test to the repo.

### A $499 cap is flagged as an anomaly
- **Context:** spend stops at exactly $499 for 12 buyers, with nothing above it.
- **Decision: report it as an unexplained pattern.** I judged it worth recording as an observation. The data cannot show whether it is a cap or a price, so the reports do not claim either.

### My claim that log spend was still right-skewed was wrong
- **What happened:** from a box plot, I concluded that past-year spend stayed right-skewed after a log transform. Checking showed a skewness of -0.01. The plot was wrong: it computed outliers on the dollar scale and drew them on a log axis.
- **Decision: the plot and the EDA summary were corrected** before they were committed.

## 2026-11-02

### Validity checks before any effect estimates
- **Decision:** I ran a chi-square test of the group sizes, a standardized mean difference table for all pre-treatment features, and logic checks on the outcome columns.
- **Result:** no evidence of a problem (p = 0.904, largest absolute SMD 0.0169).
- **Write-up:** I asked for the limitations to start with the missing email-delivery records, because they change how every effect must be described.

### Spend is the primary metric
- **Decision: `spend` is primary and `conversion` is secondary.** Profit is calculated from spend.
- **Additions from review:** Claude suggested adding `visit`, which challenge question 6 asks about, and a direct Mens vs Womens comparison, which question 1 needs.

### Welch t-test as the main test, bootstrap as a check
- **Question:** I asked whether to use a bootstrap.
- **Decision: Welch t-test for the main estimate, with a bootstrap check,** because 99.1% of customers spent nothing and the t-test's normal approximation might be unreliable. The plan states that if the two disagree, the result is reported as sensitive to the method, so neither can be chosen afterwards.

### Segment hypotheses: changes to my first draft
I drafted five hypotheses, with AI help on the statistical wording. Review changed them in four ways:

- **H2's cross-check was redundant.** No customer has both `mens` and `womens` equal to 0, so "did not buy women's merchandise" is the same group as "bought only men's". Claude pointed this out.
- **All hypotheses use spend.** My draft tested three of them on conversion, which did not match the primary metric.
- **The emails are pooled except in H2.** Testing each email separately would have produced 10 tests. I decided that only H2, which is about matching content to past purchases, needs the emails separately.
- **H4 uses a merged `history_level`.** I asked how to handle the small top segments and suggested regrouping spend amounts. Claude pointed out that the grouping must use `history`, which is measured before the email, and not `spend`. The top three segments were merged into one level before any outcomes were viewed.

### The "worth sending" rule
- **Margin:** 40%, based on Gap Inc.'s fiscal 2025 gross margin, tested from 30% to 60%.
- **Cost per email:** I chose $80 per 10,000 emails, based on an illustrative industry rate.
- **Revenue-first scenario:** I wanted to allow sending at a small loss in exchange for higher sales. Claude suggested a 10% loss tolerance; I set it at 5%. It is reported separately from the main rule.
- **Holm correction:** applied separately to the three average-effect comparisons and the six segment tests, as Claude suggested.

### The analysis plan was committed before group outcomes were viewed
- **Commit:** `bb94140`, 2026-11-02 15:53 (UTC+8).
- **Wording:** the plan is described as "pre-specified", not "pre-registered", because a Git commit is not a formal registration.

### Wording of the average effects
- **Result:** the Mens email added $0.77 per customer and the Womens email $0.42.
- **Correction:** the first draft called the Mens email's lead over the Womens email "uncertain". I pointed out that the difference is significant. **The final wording is "significant but imprecisely estimated"**, because the interval runs from $0.03 to $0.66.
- **Structure:** I asked for the report to open with the challenge questions and the planned method, then answer directly.

## 2026-11-03

### Regression adjustment as a supplementary check
- **Reading:** Facure chapters 4 to 6, on regression.
- **Question:** I asked whether features should be added one at a time. **Decision: one model with all pre-treatment features, fixed before running.** Trying combinations would allow picking the best-looking result. `history` is used instead of `history_segment`, and `visit` and `conversion` are excluded because the email may affect them.
- **Result:** estimates moved by less than $0.01 and confidence intervals narrowed by less than 0.2%. The Welch estimates remain the main results, and this check is labeled as outside the plan.

### Feature coefficients are not interpreted
- **Question:** I asked whether features without significant coefficients, such as `channel` and `zip_code`, could be dropped.
- **Decision: no.** Only the emails were randomized, so feature coefficients show association, not cause. A feature can be unrelated to how much customers spend and still change how well the email works. H3 and H5 stay in the plan as written.

### H4 keeps the linear trend
- **Question:** after seeing the effect within each level, I asked whether to test each level as its own group instead of a straight line, because level 3 fell well below the line.
- **Decision: keep the linear trend from the plan as the confirmatory test.** Switching after seeing the results would mean choosing the analysis that looks best. Separate levels would also give noisier estimates, and the largest of them would likely be overstated. The effect within each level is still reported as a descriptive check.
- **Follow-up:** comparing a level-based rule with other rules belongs to stages 03 and 04, where it can be checked on held-out data.

### Targeting uses dollars per customer, not a ratio
- **Context:** per $100 of past-year spend, the effect was highest at level 1, while in dollars per customer it was highest at level 5.
- **Decision: the targeting rule ranks customers by the effect in dollars per customer.** I reasoned that each email costs the same, so what matters is the extra spend one email brings in. A ratio would matter only if the cost grew with customer value, as with a percentage discount.
