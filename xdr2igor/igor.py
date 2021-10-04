import argparse
import re
from os import path
import pandas as pd

p = argparse.ArgumentParser()

p.add_argument("filepath", help="分割ファイルパス")
args = p.parse_args()


def main():
    xdrToIgor(args.filepath)


def xdrToIgor(inputPath: str) -> None:
    outputDir = path.dirname(inputPath)
    outputName = path.splitext(path.basename(inputPath))[0]
    outputPath = path.join(outputDir, re.sub(r"_1_2θ_θ$", "", outputName))

    df = pd.read_table(
        inputPath, encoding="shift_jis", header=2, names=["2theta", "intensity"]
    )

    df.to_csv(f"{outputPath}__igor.csv", index=None)
