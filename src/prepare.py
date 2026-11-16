"""Shared data preparation for the targeting stages (03 onward).

Every function reproduces a step fixed in DECISIONS.md, so that stages 03 to 06
use the same cells, the same train-test split and the same random baseline.
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "hillstrom.csv"
SEED = 42
N_TARGET = 10_000
LEVEL_LABELS = {1: "under $100", 2: "$100-$200", 3: "$200 or more"}


def load_data(path=DATA_PATH):
    """Load the data and add email indicators and the stage 03 cells."""
    df = pd.read_csv(path)
    df["mens_email"] = (df["segment"] == "Mens E-Mail").astype(int)
    df["womens_email"] = (df["segment"] == "Womens E-Mail").astype(int)
    df["level"] = df["history_segment"].str[0].astype(int).clip(upper=3)
    df["bought"] = np.select(
        [(df["mens"] == 1) & (df["womens"] == 1), df["mens"] == 1],
        ["both", "men's only"],
        default="women's only",
    )
    df["cell"] = df["level"].map(LEVEL_LABELS) + ", " + df["bought"]
    return df


def split(df, seed=SEED):
    """The 50:50 split stratified by assigned group (DECISIONS.md, 2026-11-07)."""
    return train_test_split(df, test_size=0.5, stratify=df["segment"], random_state=seed)


def random_baseline(df, n=N_TARGET, seed=SEED):
    """The random 10,000 customers used as the baseline (DECISIONS.md, 2026-11-11)."""
    return df.index.isin(df.sample(n, random_state=seed).index)
