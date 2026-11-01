# Data Dictionary

Source: [MineThatData E-Mail Analytics and Data Mining Challenge](https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html) (Kevin Hillstrom, 2008). The raw file has 64,000 rows, 12 columns and no missing values.

Definitions follow the challenge description. Types, ranges and values were observed in the raw CSV.

## Columns

Each column has one of three roles:

- **Pre-treatment:** measured before the campaign, so it can be used as a model feature.
- **Treatment:** the group the customer was randomly assigned to.
- **Outcome:** measured in the two weeks after the campaign, so it must never be used as a model feature.

| Column | Type | Role | Unit | Definition | Observed values |
| --- | --- | --- | --- | --- | --- |
| `recency` | Integer | Pre-treatment | Months | Months since last purchase | 1 to 12 |
| `history_segment` | Ordered category | Pre-treatment | USD range | Categorization of dollars spent in the past year | `1) $0 - $100`, `2) $100 - $200`, `3) $200 - $350`, `4) $350 - $500`, `5) $500 - $750`, `6) $750 - $1,000`, `7) $1,000 +` |
| `history` | Float | Pre-treatment | USD | Actual dollar value spent in the past year | 29.99 to 3,345.93 |
| `mens` | Binary | Pre-treatment | None | 1 = purchased men's merchandise in the past year | 0, 1 |
| `womens` | Binary | Pre-treatment | None | 1 = purchased women's merchandise in the past year | 0, 1 |
| `zip_code` | Category | Pre-treatment | None | Classifies the zip code as urban, suburban or rural | `Urban`, `Surburban`, `Rural` |
| `newbie` | Binary | Pre-treatment | None | 1 = new customer in the past twelve months | 0, 1 |
| `channel` | Category | Pre-treatment | None | Channels the customer purchased from in the past year | `Phone`, `Web`, `Multichannel` |
| `segment` | Category | Treatment | None | Email campaign the customer was assigned to | `Mens E-Mail`, `Womens E-Mail`, `No E-Mail` |
| `visit` | Binary | Outcome | None | 1 = visited the website in the following two weeks | 0, 1 |
| `conversion` | Binary | Outcome | None | 1 = purchased merchandise in the following two weeks | 0, 1 |
| `spend` | Float | Outcome | USD | Actual dollars spent in the following two weeks | Minimum 0 |

## Notes on the raw data

- **`segment` is the treatment group.** Despite its name, it is not a customer segment. Customer segments in this project are defined from pre-treatment columns.
- **`zip_code` contains a misspelling.** The raw file spells "Suburban" as `Surburban` in every suburban row. The raw file is left unchanged, and the value will be corrected during data cleaning.
- **`history_segment` is stored as text.** Its order comes from the numeric prefix in each label, so it needs to be treated as an ordered category.
- **`mens` and `womens` are not mutually exclusive.** A customer can have both set to 1.
- **There is no customer ID.** 6,562 rows exactly duplicate an earlier row. Without an ID, these cannot be distinguished from different customers who happen to share the same values, so they are kept until they have been reviewed during exploratory analysis.
