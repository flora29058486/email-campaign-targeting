# Analysis Plan

> This plan was committed before any outcomes were compared across experiment groups or customer segments. The commit timestamp is the record of this order.

## Analysis population

All 64,000 customers are analyzed in the group they were assigned to, including customers with zero spend and the 6,562 repeat rows. Spend values are not capped or transformed.

## Primary metric

`spend`: dollars spent per customer in the two weeks after the campaign.

## Secondary metrics

- `conversion`: share of customers who purchased.
- `visit`: share of customers who visited the website.

Secondary metrics are used to check whether conclusions are consistent. They do not determine the targeting rule.

## Average effects

These comparisons answer challenge questions 1 and 2:

1. Mens E-Mail vs No E-Mail
2. Womens E-Mail vs No E-Mail
3. Mens E-Mail vs Womens E-Mail

For `spend`, the effect is the difference in mean spend per customer:

- **Main estimate:** Welch t-test with a two-sided 95% confidence interval. This test does not assume that the groups have equal variances.
- **Robustness check:** percentile bootstrap 95% confidence interval, using 10,000 resamples within each group and a fixed random seed. Each resample includes customers with zero spend. This check is included because 99.1% of customers spent nothing, so the spend distribution is extreme and the normal approximation behind the t-test may be less reliable.

If the two intervals lead to different conclusions, the result is reported as sensitive to the method.

## Segment hypotheses

Each hypothesis concerns a difference in the effect of email on `spend` (email group minus No E-Mail group). Each is tested with a two-sided interaction term in an OLS regression with robust standard errors. `conversion` and `visit` are reported as consistency checks and are not part of the correction. Any other segment cut is labeled exploratory.

Unless stated otherwise, "email" pools the Mens and Womens groups.

- **H1 (recency):** The effect is larger for customers who last purchased 1-3 months ago than for those who last purchased 4-12 months ago. Rationale: recent purchasers are likely to be more engaged. The three-month cutoff is a judgment call, fixed before viewing outcomes.
- **H2a (product match):** The Womens email effect is larger for customers who bought women's merchandise (`womens` = 1) than for those who bought only men's. Rationale: content that matches past purchases is more relevant.
- **H2b (product match):** The Mens email effect is larger for customers who bought men's merchandise (`mens` = 1) than for those who bought only women's. The rationale is the same as for H2a.
- **H3 (channel):** The effect is larger for Web and Multichannel customers than for Phone customers. Rationale: email leads to the website, while phone customers would need to change how they shop.
- **H4 (spend history):** The effect increases with past-year spend, tested as a linear trend across a new column, `history_level`. It keeps the first four `history_segment` values as levels 1 to 4 (under $100, $100-$200, $200-$350 and $350-$500) and merges the top three into level 5 ($500 or more). The merge is needed because the top values are small: the original $1,000+ segment has only 1,308 customers. It uses a pre-treatment column and was fixed before viewing outcomes. Rationale: higher-value customers may spend more per order once they buy. Descriptive only: effect relative to mean past spend per level, with bootstrap confidence intervals.
- **H5 (zip code):** The effect is larger for Urban than for Rural customers. Suburban customers are reported descriptively and not tested. Rationale: urban customers may be more used to shopping online. This is an assumption that the data cannot verify.

## Multiple-testing correction

The Holm correction is applied separately to two families, because they answer different questions:

- **Average effects:** the three `spend` comparisons.
- **Segment hypotheses:** the six tests H1, H2a, H2b, H3, H4 and H5.

Results are judged at a 0.05 significance level after correction. Secondary metrics are not corrected and are not used to claim significance.

## Criteria for "worth sending"

The data contains no margin or cost figures, so both inputs are stated assumptions:

Incremental profit per customer = incremental spend × gross margin − cost per email

- **Gross margin (base case: 40%).** Close to Gap Inc.'s [40.8% in fiscal 2025](https://investors.gapinc.com/press-releases/news-details/2026/Gap-Inc--Reports-Fourth-Quarter-and-Fiscal-2025-Results-Provides-Fiscal-2026-Outlook/default.aspx). The tested range reflects [January 2026 sector averages](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/margin.html) of 35.3% for specialty retail and 56.9% for apparel. These are recent figures, while the experiment dates from 2008, and the retailer's actual margin is unknown.
- **Cost per email (base case: $0.008, or $80 per 10,000 emails).** Based on an [illustrative rate of $8 per 1,000 emails](https://www.emailvendorselection.com/cost-per-mille-cpm/) for volumes of 50,000 to 250,000. This is an example rate, not a market benchmark.

**Decision rule:**

- **Worth sending:** estimated incremental profit per customer is above zero.
- **Uncertain:** the estimate is above zero, but the 95% confidence interval for incremental spend includes the break-even value (cost per email ÷ gross margin).
- **Revenue-first scenario:** reported separately from the main rule, this accepts a loss of up to 5% of incremental spend in exchange for higher sales. The 5% tolerance is an assumption.

**Sensitivity analysis:** the rule is recalculated for gross margins of 30%, 40%, 50% and 60%, and for costs per email of $0.001, $0.008, $0.05 and $0.10.

**Not included:** unsubscribes, email fatigue, creative and staff costs, and customer value beyond the two-week window. The data cannot measure these, so the rule may overstate or understate the true value of sending.
