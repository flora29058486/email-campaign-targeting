# Email Campaign Targeting with Experimental Data

An independent project that uses a public randomized experiment of 64,000 retail customers to answer two decision questions: **who should receive a marketing email, and is sending it worth the cost?**

> **Status: in progress (started November 2026).** All eight challenge questions have answers linked below; 3, 4 and 8 are provisional until stage 06. The final targeting rule will appear at the top of this page when v1.0 is released.

## Results so far

- **Both emails raised spend over the two weeks after the campaign:** by about $0.77 per customer for the Mens email and $0.42 for the Womens email ([average effects](reports/01_01_average_effects.md)).
- **The Mens email outperformed the Womens email** on spend, visits and conversion. Its lead on spend is significant but imprecisely estimated.
- **None of the six pre-specified segment hypotheses was supported** ([segment effects](reports/02_01_segment_effects.md)). The emails raised spend in almost every segment, and the data cannot show that they worked better in any of them.
- **The Mens email is worth sending to all three past-purchase audiences** ([direct comparison](reports/02_02_email_by_segment.md), exploratory). The Womens email is worth sending only to customers who bought only women's merchandise, where neither email was shown better.
- **If only 10,000 customers can be emailed, send the Mens email to 10,000 drawn at random. If 10,000 must be left out, choose them at random too** (provisional until stage 06). Neither a [two-feature rule](reports/03_01_targeting_rule.md) nor an [uplift model using all seven features](reports/04_01_uplift_models.md) was shown to beat random selection on held-out data.
- **This data could not show which customers respond more to the email.** The rule's top cell gained $2.27 per customer in training but $1.37 on the test half, a case of regression to the mean. How good each list looks also depends on how random selection is measured, but none is shown to be better either way.

## Why this project

Comparing customers who were emailed with those who were not usually says little about whether the email worked, because companies tend to target customers who were already likely to buy. A randomized experiment removes that problem. This project uses one to estimate the causal effect of two campaigns, then turns the estimates into a targeting rule that a marketing team could act on.

The dataset has been public since 2008 and is widely used for teaching, so this project does not claim new findings. Its focus is the decision framework and the rigor of the analysis.

## Data

The [MineThatData E-Mail Analytics and Data Mining Challenge](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html) (Kevin Hillstrom, 2008) covers 64,000 customers who last purchased within twelve months. Customers were randomly assigned to one of three groups, each intended to be one-third of the sample:

- an email featuring men's merchandise
- an email featuring women's merchandise
- no email

Website visits, purchases and spend were tracked for two weeks after the campaign. See the [data dictionary](reports/data_dictionary.md) for all 12 columns.

The data is not stored in this repository. [`src/download_data.py`](src/download_data.py) downloads it from the author's website and checks its dimensions.

## Approach

1. **Experiment validity:** check that randomization held, using a sample-ratio test and covariate balance.
2. **Analysis plan:** commit the metrics, segment hypotheses and multiple-testing correction before looking at any segment-level results.
3. **Average effects:** compare each email with no email, with confidence intervals. Spend is the primary metric; visits and conversion are secondary.
4. **Heterogeneous effects:** estimate effects for the pre-specified segments, and label anything else as exploratory.
5. **Targeting rule:** convert the segment estimates into a first profit-based rule for whom to email.
6. **Uplift models:** compare models with the simpler choices on held-out data. A simpler choice is kept unless a more complex one is shown to be better.
7. **Bias demonstration:** simulate non-random targeting from the experimental data to show how far observational estimates can drift from the experimental benchmark.
8. **Profit and sensitivity:** finalize the rule, with sensitivity analysis on margin and cost per email.

## Analysis map

**Each stage answers one question and builds on the stage before it.** File names start with the stage number, so `02_01_segment_effects` is the first notebook of stage 02.

| Stage | Question it answers | Challenge questions | Files |
| --- | --- | --- | --- |
| 00 Preparation | Can the data and the experiment be trusted? | 7 | [EDA summary](reports/00_01_eda_summary.md), [experiment validity](reports/00_02_experiment_validity.md) |
| 01 Average effects | Did the emails work overall? | 1, 2, 6 | [Average effects](reports/01_01_average_effects.md) |
| 02 Segment effects | For whom did the emails work better? | 5, 6, 8 | [Segment effects](reports/02_01_segment_effects.md), [email by segment](reports/02_02_email_by_segment.md) |
| 03 Targeting rule | Whom should we email, and whom should we suppress? | 3, 4 | [Targeting rule](reports/03_01_targeting_rule.md) |
| 04 Uplift models | Can a model target better than a simple rule or random selection? | 3, 4 (supporting) | [Uplift models](reports/04_01_uplift_models.md) |
| 05 Bias demonstration | How wrong would the estimates be without random assignment? | None | Not started |
| 06 Profit and sensitivity | Is sending worth it under different cost assumptions? | 3, 4, 8 (final) | Not started |

## Challenge questions

These are the original questions from the challenge, quoted verbatim. Each answer links to the report behind it.

| # | Question | Answer |
| --- | --- | --- |
| 1 | Which e-mail campaign performed the best, the Mens version, or the Womens version? | [The Mens email](reports/01_01_average_effects.md). Its lead over the Womens email is significant but imprecisely estimated. |
| 2 | How much incremental sales per customer did the Mens version of the e-mail campaign drive? How much incremental sales per customer did the Womens version of the e-mail campaign drive? | [About $0.77 per customer for the Mens email and $0.42 for the Womens email](reports/01_01_average_effects.md), over two weeks. |
| 3 | If you could only send an e-mail campaign to the best 10,000 customers, which customers would receive the e-mail campaign? Why? | Provisional until stage 06: [send the Mens email to 10,000 customers drawn at random from all 64,000](reports/03_01_targeting_rule.md). The Mens email did best on average (+$0.77 per customer, 95% CI $0.49 to $1.05). Customers are drawn at random because no list passed the threshold set before testing: on held-out data, the segment rule beat a random 10,000 by $0.12 per customer (-$1.25 to $1.43) and [the uplift model](reports/04_01_uplift_models.md) by $0.11 (-$1.15 to $1.32). In a check added later, against the test-half average, both gaps rise to $0.51, and both intervals still include zero. This does not mean that all customers respond equally, only that this data could not identify the best 10,000. |
| 4 | If you had to eliminate 10,000 customers from receiving an e-mail campaign, which customers would you suppress from the campaign? Why? | Provisional until stage 06: [avoid suppressing if possible; if 10,000 customers must be suppressed, choose them at random](reports/03_01_targeting_rule.md). No list passed the same threshold: compared with a random 10,000, the segment rule's list gave up $0.56 less per customer (-$1.03 to $2.27) and [the uplift model's](reports/04_01_uplift_models.md) $0.45 less (-$0.91 to $1.90). A later check showed that most of these gaps came from that one random draw: against the test-half average, they are $0.22 and -$0.01, and both intervals still include zero. Suppressing a random 10,000 from the Mens email would give up about $7,700 in sales and $3,000 in profit (95% CI $1,900 to $4,100) over two weeks, at a 40% margin and $0.008 per email. This rests on the average effect: on the test half, six of seven customer cells are uncertain. |
| 5 | Did the Mens version of the e-mail campaign perform different than the Womens version of the e-mail campaign, across various customer segments? | [Not shown for spend](reports/02_02_email_by_segment.md): the Mens email's lead did not differ significantly across any of six segment splits after correction (exploratory). Visits differed by past purchases, but that is descriptive only. |
| 6 | Did the campaigns perform different when measured across different metrics, like Visitors, Conversion, and Total Spend? | [The Mens email leads on all three](reports/01_01_average_effects.md): by $0.35 per customer in spend, 3.14 percentage points in visits and 0.37 points in conversion. By segment the metrics differ: [visits vary with past purchases, while no difference was shown for spend](reports/02_02_email_by_segment.md). Visits and conversion are supporting evidence, because they are not corrected for multiple testing. |
| 7 | Did you observe any anomalies, or odd findings? | [Yes, three](reports/00_01_eda_summary.md): spend stops at exactly $499 for 12 buyers, which may indicate a cap; no customer under $200 of past-year spend bought both men's and women's merchandise; and 6,562 rows exactly repeat an earlier row. The causes of the first two are unknown. The repeated rows are kept, because without a customer ID they cannot be told apart from different customers with the same values. |
| 8 | Which audience would you target the Mens version to, and the Womens version to, given the results of the test? What data do you have to support your recommendation? | Provisional until stage 06: [send the Mens email to all three past-purchase audiences by default](reports/02_02_email_by_segment.md), because it is worth sending in each. It beat the Womens email only among buyers of both lines, a fragile exploratory result. If the Womens email must be used, send it to customers who bought only women's merchandise, where it is also worth sending and neither email was shown better. |

## Progress

| Milestone | Target date | Status |
| --- | --- | --- |
| Project setup and data dictionary | Nov 2, 2026 | Done |
| [Exploratory data analysis](reports/00_01_eda_summary.md) | Nov 3, 2026 | Done |
| [Experiment validity checks](reports/00_02_experiment_validity.md) | Nov 4, 2026 | Done |
| [Analysis plan](analysis_plan.md) | Nov 5, 2026 | Done |
| [Average effects](reports/01_01_average_effects.md) | Nov 8, 2026 | Done |
| [Segment effects](reports/02_01_segment_effects.md) | Nov 15, 2026 | Done; its memo is merged into the final decision memo |
| Uplift model comparison and bias demonstration | Nov 22, 2026 | Partly done: [uplift models](reports/04_01_uplift_models.md) |
| Targeting rule, technical report and decision memo | Nov 26, 2026 | Partly done: [rule v1](reports/03_01_targeting_rule.md) |
| v1.0 release | Nov 29, 2026 | Not started |

## Known limitations

- The data is from 2008, and customer behavior and email channels have changed since then.
- Outcomes were tracked for only two weeks, so longer-term effects cannot be measured.
- The dataset does not include margin or cost per email. Both will be stated assumptions, and conclusions that depend on them will be tested with sensitivity analysis.
- The bias demonstration is a simulation built from public data. It does not use real company data.

## How this project was built

I designed the analysis and made the final call on each methodological decision. I used Claude to write most of the code and the first drafts of the reports, and to help with statistical wording. I check results in conversation with Claude as the project progresses. [`DECISIONS.md`](DECISIONS.md) records who raised each point, and every commit that Claude helped with is marked as co-authored.

## Repository structure

```text
data/             Downloaded data (not tracked by Git)
notebooks/        Analysis notebooks
reports/          Data dictionary and written reports
src/              Reusable code, including the data download script
analysis_plan.md  Metrics, hypotheses and decision rule, committed before group outcomes were viewed
DECISIONS.md      Dated log of analytical decisions, including mistakes and dropped ideas
```

## Setup

Requires Python 3.11. Run these commands from the repository root.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/download_data.py
```

A single command to reproduce the full analysis will be added before v1.0.
