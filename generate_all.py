import csv
import datetime
import os
import codecs

# === 設定 ===
BASE_DIR = "."
OUTPUT_DIR = "."

GBOARD_FILE = "100kanojo_Gboard_dic.txt"
MSIME_FILE = "100kanojo_Shiftjis_dic.txt"
OTHER_FILE = "100kanojo_dic.txt"

FILES = [
    (GBOARD_FILE, "utf-8-sig", "Gboard"),
    (MSIME_FILE, "shift_jis", "MSIME"),
    (OTHER_FILE, "utf-16", "Other")
]

USAMI_SUFFIX = "_Usami"

# === ヘルパー関数 ===

def generate_header_comment():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    return f"# Generated on {timestamp} by GitHub Actions\n"

def read_csv(filename):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_with_encoding(path, encoding, lines):
    # 文字コードに応じて安全に書き込み
    if encoding.lower().startswith("utf-16"):
        with codecs.open(path, "w", encoding=encoding) as f:
            f.writelines(lines)
    else:
        with open(path, "w", encoding=encoding, newline="") as f:
            f.writelines(lines)

# === メイン生成処理 ===

def generate_files():
    # 読み込み元CSV
    base_people = read_csv(os.path.join(BASE_DIR, "base_people.csv"))
    base_words = read_csv(os.path.join(BASE_DIR, "base_words.csv"))

    # 辞書データを格納するリスト
    gboard_lines = []
    msime_lines = []
    other_lines = []

    # === 人名 ===
    for row in base_people:
        sei_yomi = row["姓よみ"].strip()
        mei_yomi = row["名よみ"].strip()
        sei = row["姓"].strip()
        mei = row["名"].strip()

        full_yomi = sei_yomi + mei_yomi
        full_name_space = f"{sei}　{mei}"
        full_name_nospace = f"{sei}{mei}"

        # 各形式に応じた書式
        for with_space, full_name in [(True, full_name_space), (False, full_name_nospace)]:
            suffix = "" if with_space else USAMI_SUFFIX

            gboard_lines.append(f"{full_yomi}\t{full_name}\tja-JP\n")
            msime_lines.append(f"{full_yomi}\t{full_name}\t人名\n")
            other_lines.append(f"{full_yomi}\t{full_name}\t人名\n")

    # === 一般単語 ===
    for row in base_words:
        yomi = row["よみ"].strip()
        word = row["単語"].strip()
        pos = row.get("品詞", "名詞").strip()

        gboard_lines.append(f"{yomi}\t{word}\tja-JP\n")
        msime_lines.append(f"{yomi}\t{word}\t{pos}\n")
        other_lines.append(f"{yomi}\t{word}\t{pos}\n")

    # === 出力 ===
    header = generate_header_comment()

    for filename, encoding, label in FILES:
        # 通常版
        normal_path = os.path.join(OUTPUT_DIR, filename)
        write_with_encoding(normal_path, encoding, [header] + locals()[f"{label.lower()}_lines"])

        # _Usami版
        usami_path = os.path.join(OUTPUT_DIR, filename.replace(".txt", f"{USAMI_SUFFIX}.txt"))
        write_with_encoding(usami_path, encoding, [header] + locals()[f"{label.lower()}_lines"])

    print("✅ 全6ファイルを生成しました。")

if __name__ == "__main__":
    generate_files()
