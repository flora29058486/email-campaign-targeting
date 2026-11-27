"""Rerun every analysis notebook in order, each in a fresh kernel.

Usage, from the repository root:

    python src/reproduce.py

The data is downloaded first if it is missing, and checked against the file this
project used. The notebooks then run from top to bottom in stage order, with the
notebooks folder as the working directory, and are saved with their new outputs.
Figures are rewritten in reports/figures. If every result is unchanged, Git shows
no modified files afterwards.
"""

import asyncio
import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient

import download_data

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks"


def main():
    if sys.platform == "win32":
        # The event loop Jupyter's messaging library needs on Windows; avoids a startup warning.
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    data = download_data.OUT.relative_to(ROOT).as_posix()
    if download_data.OUT.exists():
        download_data.check()
        print(f"Data: {data} found and checked")
    else:
        download_data.download()
        print(f"Data: {data} downloaded and checked")

    paths = sorted(NOTEBOOKS.glob("[0-9][0-9]_[0-9][0-9]_*.ipynb"))
    start = time.perf_counter()
    for i, path in enumerate(paths, 1):
        print(f"[{i:2}/{len(paths)}] {path.stem} ...", end=" ", flush=True)
        began = time.perf_counter()
        nb = nbformat.read(path, as_version=4)
        client = NotebookClient(
            nb,
            kernel_name="python3",
            timeout=None,
            record_timing=False,
            coalesce_streams=True,  # printed text is saved as one block, however the kernel happened to send it
            resources={"metadata": {"path": str(NOTEBOOKS)}},
            # Kernels run on this computer only; hide their warning about unencrypted local connections.
            extra_arguments=["--log-level=ERROR"],
        )
        client.execute()  # stops with the failing cell's error; the notebook file is then left unchanged
        nbformat.write(nb, path)
        print(f"ok ({time.perf_counter() - began:.0f} s)")

    minutes = (time.perf_counter() - start) / 60
    print(f"All {len(paths)} notebooks ran in {minutes:.1f} minutes. "
          "Run `git status` to see whether any notebook or figure changed.")


if __name__ == "__main__":
    main()
