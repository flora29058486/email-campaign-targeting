# Email Campaign Targeting with Experimental Data

An independent project that uses a public randomized experiment of 64,000 retail customers to answer two decision questions: **who should receive a marketing email, and is sending it worth the cost?**

> **Status: in progress (started November 2026).** Answers to challenge questions 1, 2, 5, 6 and 8 are linked below. The final targeting rule will appear at the top of this page when v1.0 is released.

## Results so far

- **Both emails raised spend over the two weeks after the campaign:** by about $0.77 per customer for the Mens email and $0.42 for the Womens email ([average effects](reports/01_01_average_effects.md)).
- **The Mens email outperformed the Womens email** on spend, visits and conversion. Its lead on spend is significant but imprecisely estimated.
- **None of the six pre-specified segment hypotheses was supported** ([segment effects](reports/02_01_segment_effects.md)). The emails raised spend in almost every segment, and the data cannot show that they worked better in any of them.

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
6. **Uplift models:** compare models with the simple segment rule on held-out data. If the simple rule performs as well, the simple rule is kept.
7. **Bias demonstration:** simulate non-random targeting from the experimental data to show how far observational estimates can drift from the experimental benchmark.
8. **Profit and sensitivity:** finalize the rule, with sensitivity analysis on margin and cost per email.

## Analysis map

**Each stage answers one question and builds on the stage before it.** File names start with the stage number, so `02_01_segment_effects` is the first notebook of stage 02.

| Stage | Question it answers | Challenge questions | Files |
| --- | --- | --- | --- |
| 00 Preparation | Can the data and the experiment be trusted? | 7 (partly) | [EDA summary](reports/00_01_eda_summary.md), [experiment validity](reports/00_02_experiment_validity.md) |
| 01 Average effects | Did the emails work overall? | 1, 2 | [Average effects](reports/01_01_average_effects.md) |
| 02 Segment effects | For whom did the emails work better? | 5, 6, 8 | [Segment effects](reports/02_01_segment_effects.md) |
| 03 Targeting rule | Whom should we email, and whom should we suppress? | 3, 4 | Not started |
| 04 Uplift models | Can a model target better than a simple segment rule? | None | Not started |
| 05 Bias demonstration | How wrong would the estimates be without random assignment? | None | Not started |
| 06 Profit and sensitivity | Is sending worth it under different cost assumptions? | 3, 4 (final) | Not started |

## Challenge questions

These are the original questions from the challenge, quoted verbatim. Answers will be linked here as the analysis progresses.

| # | Question | Answer |
| --- | --- | --- |
| 1 | Which e-mail campaign performed the best, the Mens version, or the Womens version? | [The Mens email](reports/01_01_average_effects.md). Its lead over the Womens email is significant but imprecisely estimated. |
| 2 | How much incremental sales per customer did the Mens version of the e-mail campaign drive? How much incremental sales per customer did the Womens version of the e-mail campaign drive? | [About $0.77 per customer for the Mens email and $0.42 for the Womens email](reports/01_01_average_effects.md), over two weeks. |
| 3 | If you could only send an e-mail campaign to the best 10,000 customers, which customers would receive the e-mail campaign? Why? | Not yet answered |
| 4 | If you had to eliminate 10,000 customers from receiving an e-mail campaign, which customers would you suppress from the campaign? Why? | Not yet answered |
| 5 | Did the Mens version of the e-mail campaign perform different than the Womens version of the e-mail campaign, across various customer segments? | Partly: [the two emails showed different patterns](reports/02_01_segment_effects.md). The Mens email raised spend for both men's and women's buyers, while the Womens email's extra visits and purchases were concentrated among women's buyers. This contrast was not tested directly. |
| 6 | Did the campaigns perform different when measured across different metrics, like Visitors, Conversion, and Total Spend? | [Yes, for the Womens email](reports/02_01_segment_effects.md): it raised visits and conversion more among women's buyers, but the difference in spend was not significant. The visit and conversion results are supporting evidence, because secondary metrics are not corrected for multiple testing. |
| 7 | Did you observe any anomalies, or odd findings? | Partly answered: [spend stops at exactly $499 for 12 buyers](reports/00_01_eda_summary.md), which may indicate a cap, and [no customer under $200 of past-year spend bought both men's and women's merchandise](reports/00_01_eda_summary.md). The causes are unknown. |
| 8 | Which audience would you target the Mens version to, and the Womens version to, given the results of the test? What data do you have to support your recommendation? | Provisional: [send the Mens email broadly, and the Womens email to customers who bought women's merchandise](reports/02_01_segment_effects.md). The final rule, with costs and margins, will come from stage 03. |

## Progress

| Milestone | Target date | Status |
| --- | --- | --- |
| Project setup and data dictionary | Nov 2, 2026 | Done |
| [Exploratory data analysis](reports/00_01_eda_summary.md) | Nov 3, 2026 | Done |
| [Experiment validity checks](reports/00_02_experiment_validity.md) | Nov 4, 2026 | Done |
| [Analysis plan](analysis_plan.md) | Nov 5, 2026 | Done |
| [Average effects](reports/01_01_average_effects.md) | Nov 8, 2026 | Done |
| [Segment effects](reports/02_01_segment_effects.md) and one-page memo | Nov 15, 2026 | Report done, memo not started |
| Uplift model comparison and bias demonstration | Nov 22, 2026 | Not started |
| Targeting rule, technical report and decision memo | Nov 26, 2026 | Not started |
| v1.0 release | Nov 29, 2026 | Not started |

## Known limitations

- The data is from 2008, and customer behavior and email channels have changed since then.
- Outcomes were tracked for only two weeks, so longer-term effects cannot be measured.
- The dataset does not include margin or cost per email. Both will be stated assumptions, and conclusions that depend on them will be tested with sensitivity analysis.
- The bias demonstration is a simulation built from public data. It does not use real company data.

## How this project was built

I designed the analysis and made the final call on each methodological decision. I used Claude to write most of the code and the first drafts of the reports, and to help with statistical wording. I reviewed every result and report. [`DECISIONS.md`](DECISIONS.md) records who raised each point, and every commit that Claude helped with is marked as co-authored.

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
