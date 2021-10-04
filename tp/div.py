import argparse
from os import path
import pandas as pd

p = argparse.ArgumentParser()

p.add_argument("filepath", help="分割ファイルパス")
args = p.parse_args()


def main():
    div(args.filepath)


def div(inputPath: str) -> None:
    outputDir = path.dirname(inputPath)
    outputName = path.splitext(path.basename(inputPath))[0]
    outputPath = path.join(outputDir, outputName)

    steps: pd.DataFrame = pd.read_table(
        inputPath,
        encoding="shift_jis",
        header=27,
        usecols=[2, 3],
        nrows=9,
    )[::2]

    df = pd.read_table(
        inputPath,
        encoding="shift_jis",
        header=44,
        usecols=[2, 4],
        skipfooter=1,
        engine="python",
    )

    for (i, s, e) in steps.itertuples(name=None):
        df[s:e].to_csv(f"{outputPath}__{i}.csv", index=False)
