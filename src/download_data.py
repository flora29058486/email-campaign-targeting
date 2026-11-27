"""Download the Hillstrom (2008) email experiment data and check that it is the file this project used."""

import hashlib
from pathlib import Path
from urllib.request import urlretrieve

import pandas as pd

URL = "http://www.minethatdata.com/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv"
OUT = Path(__file__).resolve().parents[1] / "data" / "hillstrom.csv"
SHA256 = "0e5893329d8b93cefecc571777672028290ab69865718020c78c7284f291aece"


def check(path=OUT):
    """Stop unless the file has the expected dimensions and SHA-256 hash."""
    shape = pd.read_csv(path).shape
    if shape != (64000, 12):
        raise SystemExit(f"{path} has shape {shape}, expected (64000, 12)")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != SHA256:
        raise SystemExit(f"{path} differs from the file used in this project (SHA-256 {digest})")
    return shape


def download(path=OUT):
    """Download the data and check it."""
    path.parent.mkdir(exist_ok=True)
    urlretrieve(URL, path)
    return check(path)


if __name__ == "__main__":
    print(f"Saved {OUT}: {download()}")
