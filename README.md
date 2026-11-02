# Email Campaign Targeting with Experimental Data

An independent project that uses a public randomized experiment of 64,000 retail customers to answer two decision questions: **who should receive a marketing email, and is sending it worth the cost?**

> **Status: in progress (started November 2026).** No campaign effects are reported yet. Findings and the final targeting rule will appear at the top of this page when v1.0 is released.

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
5. **Uplift models:** compare models with a simple segment rule on held-out data. If the simple rule performs as well, the simple rule is kept.
6. **Bias demonstration:** simulate non-random targeting from the experimental data to show how far observational estimates can drift from the experimental benchmark.
7. **Targeting rule:** convert the estimates into a profit-based rule, with sensitivity analysis on margin and cost per email.

## Challenge questions

These are the original questions from the challenge, quoted verbatim. Answers will be linked here as the analysis progresses.

| # | Question | Answer |
| --- | --- | --- |
| 1 | Which e-mail campaign performed the best, the Mens version, or the Womens version? | Not yet answered |
| 2 | How much incremental sales per customer did the Mens version of the e-mail campaign drive? How much incremental sales per customer did the Womens version of the e-mail campaign drive? | Not yet answered |
| 3 | If you could only send an e-mail campaign to the best 10,000 customers, which customers would receive the e-mail campaign? Why? | Not yet answered |
| 4 | If you had to eliminate 10,000 customers from receiving an e-mail campaign, which customers would you suppress from the campaign? Why? | Not yet answered |
| 5 | Did the Mens version of the e-mail campaign perform different than the Womens version of the e-mail campaign, across various customer segments? | Not yet answered |
| 6 | Did the campaigns perform different when measured across different metrics, like Visitors, Conversion, and Total Spend? | Not yet answered |
| 7 | Did you observe any anomalies, or odd findings? | Not yet answered |
| 8 | Which audience would you target the Mens version to, and the Womens version to, given the results of the test? What data do you have to support your recommendation? | Not yet answered |

## Progress

| Milestone | Target date | Status |
| --- | --- | --- |
| Project setup and data dictionary | Nov 2, 2026 | Done |
| [Exploratory data analysis](reports/00_01_eda_summary.md) | Nov 3, 2026 | Done |
| [Experiment validity checks](reports/00_02_experiment_validity.md) | Nov 4, 2026 | Done |
| [Analysis plan](analysis_plan.md) | Nov 5, 2026 | Done |
| Average effects | Nov 8, 2026 | Not started |
| Segment effects and one-page memo | Nov 15, 2026 | Not started |
| Uplift model comparison and bias demonstration | Nov 22, 2026 | Not started |
| Targeting rule, technical report and decision memo | Nov 26, 2026 | Not started |
| v1.0 release | Nov 29, 2026 | Not started |

## Known limitations

- The data is from 2008, and customer behavior and email channels have changed since then.
- Outcomes were tracked for only two weeks, so longer-term effects cannot be measured.
- The dataset does not include margin or cost per email. Both will be stated assumptions, and conclusions that depend on them will be tested with sensitivity analysis.
- The bias demonstration is a simulation built from public data. It does not use real company data.

## Repository structure

```text
data/             Downloaded data (not tracked by Git)
notebooks/        Analysis notebooks
reports/          Data dictionary and written reports
src/              Reusable code, including the data download script
analysis_plan.md  Metrics, hypotheses and decision rule, committed before group outcomes were viewed
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
