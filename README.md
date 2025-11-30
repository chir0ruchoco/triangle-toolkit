# Triangle Toolkit 🧮✨
直角三角形の幾何構造から **N** を自動計算する Windows 向けツール
![triangle](./assets/triangle.png)

## 📘 概要

本アプリでは以下の幾何構造をもとに **N** を算出します：

- 左側に「斜辺 **b**」「高さ **c**」をもつ直角三角形  
- 右側に「斜辺 **N**」「高さ **c**」をもつ直角三角形  
- 2つの三角形を横に並べたとき、底辺が **a** になる

計算式：

1. 左側の三角形  
   \[
   x = \sqrt{b^2 - c^2}
   \]
2. 底辺の残り  
   \[
   y = a - x
   \]
3. 右側の三角形  
   \[
   N = \sqrt{y^2 + c^2}
   \]

ユーザーが入力するのは **a, b, c** の 3つのみ。  
アプリに表示されるのは **N のみ** です。

## ✨ 機能一覧

- **リアルタイム計算**
- **数値入力制限（0-9・小数点）**
- **b² < c² の数学チェック**
- **クリアボタン**


## 📁 ディレクトリ構成

```
triangle-toolkit/
  main.py
  assets/
    triangle.png
    triangle-icon.ico
  README.md
```

## 🔧 環境

- Windows  
- Python 3.12.10

## 📦 必要ライブラリ

```
pip install flet
pip install pyinstaller
```

以下はビルドに必要：

```
pip install "flet[cli]"
pip install pyinstaller
```

## ▶ 開発用アプリ実行

```
git clone https://github.com/your-name/triangle-toolkit.git
cd triangle-toolkit
pip install flet
python main.py
```

## 🏗 exe ビルド方法（Windows）

```
flet pack main.py `
  --name "TRIANGLE-TOOLKIT" `
  --icon assets/triangle-icon.ico `
  --add-data "assets;assets" `
  -D
```

### 出力物

```
dist/
  TRIANGLE-TOOLKIT.exe
```

## 📝 注意事項

- `b² < c²` の場合 N は算出不可  
- Windows 以外も python 実行は可能、exe ビルドは Windows 前提
