# Triangle Toolkit 🧮✨
直角三角形の幾何構造から **N** を自動計算する Windows 向けツール

本アプリには以下の2つのデザインバージョンがあります：

1. **泡版 (Bubbles)**  
   爽やかな水色背景と泡のアニメーションが特徴。  
   <img src="./assets/gif/triangle_bubbles.gif" alt="triangle_bubbles" width="400">

2. **血版 (Bloody)**  
   ダークな背景と血のしずくエフェクトが特徴。  
   <img src="./assets/gif/triangle_bloody.gif" alt="triangle_bloody" width="400">

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
  app_ver_bubbles.py  # 泡版
  app_ver_bloody.py   # 血版
  assets/
    triangle_bubbles-icon.ico
    triangle_bloody -icon.ico
  README.md
```

## 🔧 環境

- Windows  
- Python 3.12.10

## 📦 必要ライブラリ

```
pip install flet
```

以下はビルドに必要：

```
pip install pyinstaller
pip install "flet[cli]"
```

## ▶ 開発用アプリ実行

```
git clone https://github.com/your-name/triangle-toolkit.git
cd triangle-toolkit
pip install flet

# 泡版を実行
python app_ver_bubbles.py

# 血版を実行
python app_ver_bloody.py
```

## 🏗 exe ビルド方法（Windows）

```
# 泡版をビルド
flet pack app_ver_bubbles.py `
  --name "TRIANGLE-TOOLKIT Bubbles" `
  --icon assets/triangle_bubbles-icon.ico `
  --add-data "assets;assets" `
  -D

# 血版をビルド
flet pack app_ver_bloody.py `
  --name "TRIANGLE-TOOLKIT Bloody" `
  --icon assets/triangle_bloody -icon.ico `
  --add-data "assets;assets" `
  -D
```

### 出力物

```
dist/
  TRIANGLE-TOOLKIT Bubbles.exe
  TRIANGLE-TOOLKIT Bloody.exe
```

## 📝 注意事項

- `b² < c²` の場合 N は算出不可  
- Windows 以外も python 実行は可能、exe ビルドは Windows 前提
