from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

URL = "http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv"
OUT = Path(__file__).resolve().parents[1] / "data" / "hillstrom.csv"

urlretrieve(URL, OUT)
df = pd.read_csv(OUT)
assert df.shape == (64000, 12), df.shape
print(f"Saved {OUT}: {df.shape}")
