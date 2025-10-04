#!/usr/bin/env python3
"""
convert_existing.py

既存の 100kanojo_dic.txt (UTF-16, 読み\t単語\t品詞) を読み込み、
LibreOffice Calc で編集可能な base_people.csv と base_words.csv を生成する。

- 単語に全角スペース「　」が含まれる場合 → フルネームとみなして base_people.csv に出力
  - 姓と名に分割
  - 姓や名が単独で登録されていれば、その読みを補完
  - 見つからなければ空欄にする（手動で補完する）
- 単語にスペースがない場合 → base_words.csv に出力

⚠️ 出力CSVには「フルネームの読み」は書き込まない。
    今後の自動生成スクリプト側で「姓よみ＋名よみ」を連結して生成する。
"""

import csv
from pathlib import Path

INPUT_FILE = "100kanojo_dic.txt"
BASE_PEOPLE = "base_people.csv"
BASE_WORDS = "base_words.csv"


def convert():
    names = []
    words = []

    # 全行を一度読み込む
    entries = []
    with open(INPUT_FILE, "r", encoding="utf-16") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            yomi, word = parts[0], parts[1]
            entries.append((yomi, word))

    # 単語->読み の辞書（単独登録された語の判定に利用）
    word_to_yomi = {}
    for yomi, word in entries:
        if "　" not in word:  # 全角スペースなし → 単独語
            word_to_yomi[word] = yomi

    # 分類処理
    for yomi, word in entries:
        if "　" in word:  # フルネーム
            try:
                sei, mei = word.split("　", 1)
            except ValueError:
                sei, mei = word, ""
            sei_yomi = word_to_yomi.get(sei, "")
            mei_yomi = word_to_yomi.get(mei, "")
            names.append({
                "姓よみ": sei_yomi,
                "名よみ": mei_yomi,
                "姓": sei,
                "名": mei
            })
        else:
            words.append({"よみ": yomi, "単語": word})

    # 書き出し（UTF-8 BOM付き）
    with open(BASE_PEOPLE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["姓よみ", "名よみ", "姓", "名"])
        writer.writeheader()
        writer.writerows(names)

    with open(BASE_WORDS, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["よみ", "単語"])
        writer.writeheader()
        writer.writerows(words)

    print(f"変換完了: {BASE_PEOPLE}, {BASE_WORDS}")
    print("※ 姓よみ/名よみ が空欄の部分は手動で補完してください。")


if __name__ == "__main__":
    convert()
