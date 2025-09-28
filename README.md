# 100kanojo IME Dictionary

## How to Install the 100kanojo IME Dictionary

These instructions assume you have already downloaded the dictionary file(s) from this repository (for example, `100kanojo_dic.txt`, `100kanojo_gboard_dic.txt`, or `100kanojo_shiftjis_dic.txt`).

### For Windows IME / MS‐IME

1. Open **Settings → Time & Language → Language**.
2. Under "Keyboards" or "Input method," select your Japanese IME and open its properties.
3. Find the “Dictionary” or “User Dictionary” settings.
4. Import the file `100kanojo_dic.txt` (or the version appropriate for your IME) using the “Import” function.
5. Restart or reload the IME so that the new dictionary entries take effect.

### For Google / Gboard (Android / iOS)

1. Copy `100kanojo_gboard_dic.txt` to your device.
2. Open Gboard settings → Dictionary → Personal dictionary (or similar).
3. Use “Import” (or +) to load the file. If Gboard does not support bulk import via text file, you may need to use a third‐party tool or script that converts the file into a supported format.
4. Restart the keyboard app or device if necessary.

### For macOS

1. Open the “Dictionary” or “User Dictionary” tab in **System Preferences → Keyboard**.
2. Use the “Import” option to load `100kanojo_dic.txt`.
3. Authenticate if required.
4. Log out / log back in, or reboot, so the changes are applied.

### If Your IME Doesn’t Support Direct Import

If your Japanese input method doesn’t support importing a text dictionary directly:

- You may need to convert the dictionary file format (e.g. encoding, separators) to one your IME accepts.
- For example, check if it needs UTF‑8 or Shift‑JIS, tab‐separated fields, etc.
- Use a script (Python, etc.) to reformat if necessary.

---

## 100kanojo IME 辞書の導入方法

以下の手順は、すでにリポジトリから辞書ファイル（例: `100kanojo_dic.txt`、`100kanojo_gboard_dic.txt`、または `100kanojo_shiftjis_dic.txt`）をダウンロードしていることを前提としています。

### Windows IME / MS‐IME の場合

1. **設定 → 時刻と言語 → 言語** を開きます。
2. 「キーボード」または「入力方式」の設定から、日本語IMEを選択し、プロパティを開きます。
3. 「辞書」または「ユーザー辞書」の設定を見つけます。
4. 「インポート」機能を使用して、`100kanojo_dic.txt`（またはあなたのIMEに適したバージョン）をインポートします。
5. IMEを再起動または再読み込みして、新しい辞書が適用されるようにします。

### Google / Gboard（Android / iOS）の場合

1. `100kanojo_gboard_dic.txt` をデバイスにコピーします。
2. Gboard設定 → 辞書 → 個人辞書（またはそれに相当する設定）を開きます。
3. 「インポート」機能（または+）を使用してファイルを読み込みます。もしGboardがテキストファイルの一括インポートをサポートしていない場合、サポートされるフォーマットに変換するためのツールやスクリプトが必要です。
4. 必要に応じて、キーボードアプリやデバイスを再起動します。

### macOS の場合

1. **システム環境設定 → キーボード** から「辞書」または「ユーザー辞書」タブを開きます。
2. 「インポート」オプションを使用して `100kanojo_dic.txt` を読み込みます。
3. 必要に応じて認証を行います。
4. ログアウトして再ログインするか、再起動して変更を適用します。

### もしIMEが直接インポートをサポートしていない場合

もし使用している日本語入力方式がテキスト辞書のインポートを直接サポートしていない場合：

- IMEが受け入れるフォーマット（例えば、エンコーディングや区切り文字）に辞書ファイルの形式を変換する必要があるかもしれません。
- 例えば、UTF-8やShift-JIS、タブ区切りなどの形式が必要かもしれません。
- 必要であれば、Pythonなどのスクリプトを使って再フォーマットすることができます。
