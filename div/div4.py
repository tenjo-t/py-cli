import tkinter.filedialog as tkfd
import pandas as pd
import os

"""
df : 全データの保存先
forigin : 作成ファイル名
df3 : countに応じたデータの2次元配列
fourbun : countに応じたデータを保存するファイルパス
"""

# 元データファイルを指定する
inputPath = tkfd.askopenfilename()
dirname = os.path.dirname(inputPath)

# dfにデータを格納する
df = pd.read_csv(inputPath, header=None, comment="%")
# これから作るファイル名を入力してもらう
forigin = input("enter file name: ")

# 作成ファイルの末尾
Hz = [
    "3_0",
    "3_2",
    "3_4",
    "3_6",
    "3_8",
    "4_0",
    "4_2",
    "4_4",
    "4_6",
    "4_8",
    "5_0",
    "5_2",
    "5_4",
    "5_6",
    "5_8",
    "6_0",
]
# 測定周波数リスト
fq = [
    1000,
    1584.89,
    2511.89,
    3981.07,
    6309.57,
    10000,
    15848.9,
    25118.9,
    39810.7,
    63095.7,
    100000,
    158489,
    251189,
    398107,
    630957,
    1000000,
]

# ステージに応じたカウント数(1.0→1stHeating, 2.0→1stCooling, 3.0→2ndHeating, 4.0→2ndCooling)
nm = [
    "1stHeating",
    "1stCooling",
    "2ndHeating",
    "2ndCooling",
    "3rdHeating",
    "3rdCooling",
    "4thHeating",
    "4thCooling",
]
count = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]

for n in range(8):
    with open(f"{dirname}/{forigin}_{nm[n]}_all.csv", mode="w", newline="") as fourbun:
        # count(1.0,2.0,...)に応じてデータを格納する
        df3 = df[df[7] == count[n]]
        # fourbunにdf3を出力する
        df3.to_csv(fourbun, index=False, mode="a", header=False)

    for m in range(16):
        with open(
            f"{dirname}/{forigin}_{nm[n]}_({Hz[m]})Hz.csv", mode="w", newline=""
        ) as sixteenbun2:
            # fqの値に応じてdf3のデータを選抜する
            sixteenbun = df3[df3[1] == fq[m]]
            # ヘッダ―をつける
            sixteenbun.columns = [
                "time(s)",
                "frequency(Hz)",
                "temperature(K)",
                "Cp",
                "epsilon_real",
                "epsilon_img",
                "D",
                "count",
            ]
            # sixteenbun2にsixteenbunを出力
            sixteenbun.to_csv(sixteenbun2, index=False, mode="a", header=True)

print("Completed!")
