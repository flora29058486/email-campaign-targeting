# Email Campaign Targeting with Experimental Data

An independent project that uses a public randomized experiment of 64,000 retail customers to answer two decision questions: **who should receive a marketing email, and is sending it worth the cost?**

> **Status: in progress (started November 2026).** All analyses are complete and all eight challenge questions are answered. A single command to reproduce the analysis will be added before the v1.0 release.

## Start here

- **[Decision memo](reports/decision_memo.md):** the recommendation for a marketing team, in brief.
- **[Technical report](reports/technical_report.md):** the design, results and limitations in one document.
- **[Answers to the challenge questions](reports/challenge_answers.md):** the eight original questions, answered one by one with the evidence behind each answer.
- **[Analysis map](#analysis-map):** the stage reports and notebooks that hold the full analysis.

## Main findings

- **Both emails raised spend over the two weeks after the campaign:** by about $0.77 per customer for the Mens email and $0.42 for the Womens email ([average effects](reports/01_01_average_effects.md)).
- **The Mens email outperformed the Womens email** on spend, visits and conversion. Its lead on spend is significant but imprecisely estimated.
- **None of the six pre-specified segment hypotheses was supported** ([segment effects](reports/02_01_segment_effects.md)). The emails raised spend in almost every segment, and the data cannot show that they worked better in any of them.
- **The Mens email is worth sending to all three past-purchase audiences** ([direct comparison](reports/02_02_email_by_segment.md), exploratory). The Womens email is worth sending only to customers who bought only women's merchandise, where neither email was shown better.
- **If only 10,000 customers can be emailed, send the Mens email to 10,000 drawn at random. If 10,000 must be left out, choose them at random too.** Neither a [two-feature rule](reports/03_01_targeting_rule.md) nor an [uplift model using all seven features](reports/04_01_uplift_models.md) was shown to beat random selection on held-out data.
- **This data could not show which customers respond more to the email.** The rule's top cell gained $2.27 per customer in training but $1.37 on the test half, a case of regression to the mean. How good each list looks also depends on how random selection is measured, but none is shown to be better either way.
- **These answers hold under every margin and cost tested** ([profit and sensitivity](reports/06_01_profit_sensitivity.md)). Emailing a random 10,000 customers earns about $3,000 over two weeks at the base case, and the Mens email stays worth sending while each email costs less than about $0.15 to $0.29, depending on the margin.
- **Without random assignment, a simple comparison would have overstated the Mens email's effect by up to 69%** ([bias demonstration](reports/05_01_bias_demonstration.md)). Adjusting for the features used to choose customers removed the bias, but leaving one of them out left up to 38%.

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

## Analysis map

**Each stage answers one question and builds on the stage before it.** File names start with the stage number, so `02_01_segment_effects` is the first notebook of stage 02.

**Every test, threshold and decision rule was written down before the outcomes it judged were viewed:** first in the [analysis plan](analysis_plan.md), then in each stage's design in [`DECISIONS.md`](DECISIONS.md). A more complex targeting method replaces a simpler one only if it is shown to be better on held-out data, and checks added after the results are labeled as such.

| Stage | Question it answers | Challenge questions | Files |
| --- | --- | --- | --- |
| 00 Preparation | Can the data and the experiment be trusted? | 7 | [EDA summary](reports/00_01_eda_summary.md), [experiment validity](reports/00_02_experiment_validity.md) |
| 01 Average effects | Did the emails work overall? | 1, 2, 6 | [Average effects](reports/01_01_average_effects.md) |
| 02 Segment effects | For whom did the emails work better? | 5, 6, 8 | [Segment effects](reports/02_01_segment_effects.md), [email by segment](reports/02_02_email_by_segment.md) |
| 03 Targeting rule | Whom should we email, and whom should we suppress? | 3, 4 | [Targeting rule](reports/03_01_targeting_rule.md) |
| 04 Uplift models | Can a model target better than a simple rule or random selection? | 3, 4 (supporting) | [Uplift models](reports/04_01_uplift_models.md) |
| 05 Bias demonstration | How wrong would the estimates be without random assignment? | None | [Bias demonstration](reports/05_01_bias_demonstration.md) |
| 06 Profit and sensitivity | Is sending worth it under different cost assumptions? | 3, 4, 8 (final) | [Profit and sensitivity](reports/06_01_profit_sensitivity.md) |

## Progress

| Milestone | Target date | Status |
| --- | --- | --- |
| Project setup and data dictionary | Nov 2, 2026 | Done |
| [Exploratory data analysis](reports/00_01_eda_summary.md) | Nov 3, 2026 | Done |
| [Experiment validity checks](reports/00_02_experiment_validity.md) | Nov 4, 2026 | Done |
| [Analysis plan](analysis_plan.md) | Nov 5, 2026 | Done |
| [Average effects](reports/01_01_average_effects.md) | Nov 8, 2026 | Done |
| [Segment effects](reports/02_01_segment_effects.md) and [email by segment](reports/02_02_email_by_segment.md) | Nov 15, 2026 | Done; its memo is merged into the final decision memo |
| Uplift model comparison and bias demonstration | Nov 22, 2026 | Done: [uplift models](reports/04_01_uplift_models.md) and [bias demonstration](reports/05_01_bias_demonstration.md), the latter on Nov 26 |
| Targeting rule, technical report and decision memo | Nov 26, 2026 | Done: [targeting answers](reports/03_01_targeting_rule.md), [profit and sensitivity](reports/06_01_profit_sensitivity.md), the [technical report](reports/technical_report.md) and the [decision memo](reports/decision_memo.md), the latter two on Nov 27 |
| v1.0 release | Nov 29, 2026 | Not started |

## Known limitations

- The data is from 2008, and customer behavior and email channels have changed since then.
- Outcomes were tracked for only two weeks, so longer-term effects cannot be measured.
- The dataset does not include margin or cost per email. Both are stated assumptions, and [stage 06](reports/06_01_profit_sensitivity.md) tests the conclusions across a range of values.
- The bias demonstration is a simulation built from public data. It does not use real company data.

## How this project was built

I designed the analysis and made the final call on each methodological decision. I used Claude to write most of the code and the first drafts of the reports, and to help with statistical wording. I check results in conversation with Claude as the project progresses. [`DECISIONS.md`](DECISIONS.md) records who raised each point, and every commit that Claude helped with is marked as co-authored.

## Repository structure

```text
data/             Downloaded data (not tracked by Git)
notebooks/        Analysis notebooks
reports/          Data dictionary, stage reports, technical report, challenge answers and decision memo
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
