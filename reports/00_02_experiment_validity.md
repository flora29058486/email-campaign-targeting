# Experiment Validity

Before estimating any campaign effects, I checked whether the groups can be fairly compared and whether the data is internally consistent. **The checks found no evidence of a problem with the random assignment.** No outcomes were compared across groups at this stage. The code and full tables are in [`notebooks/00_02_experiment_validity.ipynb`](../notebooks/00_02_experiment_validity.ipynb).

## Sample ratio

The challenge description says that customers were randomly split into three equal groups. **A chi-square goodness-of-fit test found no evidence of a sample ratio mismatch (χ² = 0.203, df = 2, p = 0.904).**


| Group         | Observed | Expected | Difference |  Share |
| ------------- | -------: | -------: | ---------: | -----: |
| Mens E-Mail   |   21,307 | 21,333.3 |      -26.3 | 33.29% |
| No E-Mail     |   21,306 | 21,333.3 |      -27.3 | 33.29% |
| Womens E-Mail |   21,387 | 21,333.3 |      +53.7 | 33.42% |

## Covariate balance

Equal group sizes do not guarantee that the groups contain similar customers, so I compared them on all eight pre-treatment columns using the standardized mean difference (SMD). `history_segment`, `zip_code` and `channel` were split into one indicator per value, which gives 18 features and 54 pairwise comparisons.

**The largest absolute SMD was 0.0169 (`channel`: Phone, Mens E-Mail vs Womens E-Mail), well below the common 0.1 threshold for balance.** For example, mean past-year spend was $242.84, $240.88 and $242.54 in the Mens, No E-Mail and Womens groups.

## Data consistency


| Check                                         | Rows |
| --------------------------------------------- | ---: |
| Missing values                                |    0 |
| `conversion` = 1 but `visit` = 0              |    0 |
| `spend` > 0 but `conversion` = 0              |    0 |
| `conversion` = 1 but `spend` = 0              |    0 |
| `spend` < 0                                   |    0 |
| `recency` outside 1 to 12                     |    0 |
| Binary column not 0 or 1                      |    0 |
| `mens` = 0 and `womens` = 0                   |    0 |
| `history` outside its `history_segment` range |    0 |
| Unexpected experiment group                   |    0 |

The data also contains 6,562 exact repeat rows. **With no customer ID, they cannot be separated from different customers who share the same values, so they are kept.** The [EDA summary](00_01_eda_summary.md) describes them.

## Limitations

- **Email delivery:** the data records which group each customer was assigned to, not whether the email was delivered or opened. Effect estimates therefore describe being assigned to receive an email.
- **Unmeasured characteristics:** balance can only be checked on recorded columns. Random assignment is expected to balance other characteristics too, but the data cannot confirm this.
- **The assignment process:** these checks look for signs of a problem in the data. They cannot directly verify how customers were assigned.
