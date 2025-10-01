#!/usr/bin/env python3
"""
generate_all.py

base_names.csv / base_words.csv から
Gboard / MSIME / その他 用の辞書ファイルを生成する

出力ファイル:
- 100kanojo_Gboard_dic.txt         (UTF-8 BOM, 読み\t単語\tja-JP)
- 100kanojo_Shiftjis_dic.txt       (Shift_JIS, 読み\t単語\t品詞)
- 100kanojo_dic.txt                (UTF-16, 読み\t単語\t品詞)
- 上記の _Usami 版（単語内スペース削除）
"""

import csv
import codecs
from pathlib import Path

# 入力 CSV
NAMES_CSV = "base_names.csv"
WORDS_CSV = "base_words.csv"

# 出力定義
TARGETS = [
    {
        "filename": "100kanojo_Gboard_dic.txt",
        "formatter": lambda yomi, word, pos: f"{yomi[:15]}\t{word}\tja-JP\n",
        "encoding": "utf-8-sig",
    },
    {
        "filename": "100kanojo_Shiftjis_dic.txt",
        "formatter": lambda yomi, word, pos: f"{yomi}\t{word}\t{pos}\n",
        "encoding": "shift_jis",
    },
    {
        "filename": "100kanojo_dic.txt",
        "formatter": lambda yomi, word, pos: f"{yomi}\t{word}\t{pos}\n",
        "encoding": "utf-16",
    },
]


def read_words(csv_path):
    """ base_words.csv -> list of (yomi, word, kind) """
    rows = []
    if not csv_path.exists():
        return rows
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            y = (row.get("よみ") or "").strip()
            w = (row.get("単語") or "").strip()
            if y and w:
                rows.append((y, w, "word"))
    return rows


def read_names(csv_path):
    """ base_names.csv -> list of (yomi, word, kind) """
    rows = []
    if not csv_path.exists():
        return rows
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sei_yomi = (row.get("姓よみ") or "").strip()
            mei_yomi = (row.get("名よみ") or "").strip()
            sei = (row.get("姓") or "").strip()
            mei = (row.get("名") or "").strip()
            if sei and mei:
                # フルネーム
                y_full = sei_yomi + mei_yomi
                word_full = f"{sei} {mei}"  # スペースあり
                rows.append((y_full, word_full, "full"))
                # 姓のみ
                if sei:
                    rows.append((sei_yomi, sei, "sei"))
                # 名のみ
                if mei:
                    rows.append((mei_yomi, mei, "mei"))
    return rows


def dedupe_preserve_order(pairs):
    """ (yomi, word, kind) の重複を削除 """
    seen = set()
    out = []
    for y, w, k in pairs:
        key = (y, w, k)
        if key not in seen:
            seen.add(key)
            out.append((y, w, k))
    return out


def write_dict_file(path, entries, formatter, encoding):
    path.parent.mkdir(parents=True, exist_ok=True)
    with codecs.open(path, "w", encoding=encoding) as f:
        for y, w, kind in entries:
            if kind == "full":
                pos = "人名"
            elif kind == "sei":
                pos = "姓"
            elif kind == "mei":
                pos = "名"
            else:
                pos = "名詞"
            f.write(formatter(y, w, pos))


def main():
    base_dir = Path(".")
    words = read_words(base_dir / WORDS_CSV)
    names = read_names(base_dir / NAMES_CSV)
    all_entries = dedupe_preserve_order(words + names)

    for spec in TARGETS:
        out_path = base_dir / spec["filename"]
        usami_path = base_dir / spec["filename"].replace(".txt", "_Usami.txt")

        # 通常版
        write_dict_file(out_path, all_entries, spec["formatter"], spec["encoding"])

        # Usami版（単語内スペース削除）
        usami_entries = [(y, w.replace(" ", ""), k) for (y, w, k) in all_entries]
        write_dict_file(usami_path, usami_entries, spec["formatter"], spec["encoding"])

        print(f"生成完了: {out_path} 、 {usami_path}")

    print("全ファイル生成が完了しました。")


if __name__ == "__main__":
    main()
