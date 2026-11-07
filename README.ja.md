<div align="center">
  <img src="./assets/header.svg" alt="ねむねむ三毛ネコ カーソル バナー" width="800" />

  <h1>🐾 ねむねむ三毛ネコ カーソル</h1>

  <p><strong>ミントカラーのポインタに寄り添う「ねむねむ三毛ネコ」の Windows 10 / 11 用アニメーションマウスカーソルテーマ</strong></p>

  <p>
    <a href="https://github.com/Sunwood-ai-labs/nemunemu-calico-cursor/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/nemunemu-calico-cursor/ci.yml?branch=main&amp;label=CI&amp;logo=github" alt="CI Status" /></a>
    <a href="https://sunwood-ai-labs.github.io/nemunemu-calico-cursor/ja/"><img src="https://img.shields.io/badge/Docs-VitePress-38B2AC?logo=vitepress&amp;logoColor=white" alt="Documentation" /></a>
    <img src="https://img.shields.io/badge/Platform-Windows%2010%20%2F%2011-0078D6?logo=windows&amp;logoColor=white" alt="Windows 10 / 11" />
    <img src="https://img.shields.io/badge/Format-32--bit%20BGRA%20.ani%20%2F%20.cur-4A3B32" alt="32-bit BGRA .ani / .cur" />
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-DD6B20.svg" alt="MIT License" /></a>
  </p>

  <p>
    <a href="./README.md">English</a> | <strong>日本語</strong> | <a href="https://sunwood-ai-labs.github.io/nemunemu-calico-cursor/ja/">ドキュメント</a>
  </p>
</div>

---

## ✨ 概要

**ねむねむ三毛ネコ カーソル (Nemunemu Calico Cursor)** は、爽やかなミントカラーのポインタの隣でうとうと眠る三毛猫をモチーフにした、Windows 10 / 11 向けアニメーションマウスカーソルテーマです。すべてのカーソルは **全8フレーム・約160ms周期** の滑らかなループアニメーションで、背景完全透過の **32bit BGRA** フォーマット（`.ani` および静止画 `.cur`）として構築されています。

<div align="center">
  <img src="./assets/gif/04_calico_cat_256.gif" alt="ねむねむ三毛ネコ マスコットプレビュー (256x256)" width="160" />
</div>

- **4デザイン・5ロール収録**: 通常選択 (`Arrow`)、リンク選択 (`Hand`)、テキスト選択 (`IBeam`)、待ち状態 / バックグラウンド作業中 (`Wait` & `AppStarting`) をカバー。
- **3種類のサイズ展開**: 標準 `64×64` (`cursors/`)、ミディアム `48×48` (`cursors/48x48/`)、コンパクト `32×32` (`cursors/32x32/`) を同梱。
- **1ピクセル単位で調整されたホットスポット**: 矢印の先端、指先、Iビームの中心軸、スピナーの中央にホットスポット（クリック判定点）を厳密に配置しており、猫のイラストがクリック操作を邪魔しません。
- **再起動不要のワンコマンド導入＆安全ロールバック**: `install.ps1` が現在のカーソル設定を `backup-cursors.json` に自動保存し、Win32 API `SystemParametersInfo(SPI_SETCURSORS)` によって即時反映します。

---

## 🎨 カーソル一覧とホットスポット座標

### アニメーションカーソル プレビュー

| プレビュー (64×64) | カーソル名 | Windows ロール (`Registry`) | 収録ファイル (`.ani` / `.cur`) | デザイン説明 |
| :---: | :--- | :--- | :--- | :--- |
| <img src="./assets/gif/01_normal_64.gif" alt="Normal Select" width="64" /> | **Normal Select (通常選択)** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | ミント色の矢印ポインタの隣でうとうとする三毛猫。 |
| <img src="./assets/gif/02_link_64.gif" alt="Link Select" width="64" /> | **Link Select (リンクの選択)** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | ミント色の袖口の指差しハンドと三毛猫。 |
| <img src="./assets/gif/03_text_64.gif" alt="Text Select" width="64" /> | **Text Select (テキスト選択)** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | ミント色のIビームの横に座る三毛猫（クリック軸はIビーム中央に厳密調整）。 |
| <img src="./assets/gif/04_busy_64.gif" alt="Busy / Working" width="64" /> | **Busy / Working (待ち状態・作業中)** | `Wait`<br>`AppStarting` | `nemunemu_busy.ani`<br>`nemunemu_working.ani`<br>`nemunemu_busy.cur`<br>`nemunemu_working.cur` | 眠る三毛猫の周りを8個のミント色カプセルが回るインジケータ。 |

### ホットスポット検証ガイドと座標一覧

<div align="center">
  <img src="./assets/preview/hotspot-guide.png" alt="ホットスポット検証ガイド" width="680" />
</div>

| カーソルロール | 元GIFファイル | 原画スプライトシート (4列×2段) | ホットスポット `64×64` | ホットスポット `48×48` | ホットスポット `32×32` |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **Normal Select (`Arrow`)** | `assets/gif/01_normal_64.gif` | `assets/sprites/01_normal_sheet.png` | `(11, 9)` | `(8, 7)` | `(6, 5)` |
| **Link Select (`Hand`)** | `assets/gif/02_link_64.gif` | `assets/sprites/02_link_sheet.png` | `(21, 6)` | `(16, 5)` | `(11, 3)` |
| **Text Select (`IBeam`)** | `assets/gif/03_text_64.gif` | `assets/sprites/03_text_sheet.png` | `(18, 32)` | `(14, 24)` | `(9, 16)` |
| **Busy / Working (`Wait`, `AppStarting`)** | `assets/gif/04_busy_64.gif` | `assets/sprites/04_busy_sheet.png` | `(32, 32)` | `(24, 24)` | `(16, 16)` |

---

## 🚀 クイックスタート（インストール方法）

### 方法1: PowerShell ワンコマンド適用（推奨）

リポジトリのルートディレクトリで以下のコマンドを実行します。カーソル一式を `%LOCALAPPDATA%\Cursors\NemunemuCalico` にコピーし、変更前の設定を `backup-cursors.json` に自動バックアップした上で、`HKCU:\Control Panel\Cursors` と Win32 API `SystemParametersInfo(SPI_SETCURSORS)` により再起動不要で即座に反映します。

```powershell
# 標準サイズ (64x64) をインストール
powershell -ExecutionPolicy Bypass -File .\install.ps1

# 48x48 または 32x32 サイズを指定してインストールする場合
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 32
```

### 方法2: `install.inf` を使った GUI 導入

1. エクスプローラーで `install.inf` を右クリックし、**「インストール」** を選択します。
2. Windows の「マウスのプロパティ」（`Win + R` → `main.cpl` → **「ポインター」** タブ）を開きます。
3. デザイン（スキーム）一覧から **Nemunemu Calico** を選択して「適用」をクリックします。

---

## 🔄 アンインストール（元に戻す方法）

自動バックアップ（`%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json`）から導入前のカーソル設定を復元し、インストール先フォルダをクリーンアップします。

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```

---

## 🛠️ ソースからのビルドと検証

すべての `.ani` / `.cur` ファイルは、`assets/gif/` 内の透過 GIF から `scripts/build_cursors.py` によって生成・検証できます。

```powershell
# 全サイズ (64x64 / 48x48 / 32x32) の .ani / .cur とホットスポット検証画像を生成
uv run scripts/build_cursors.py

# RIFF ACON 構造、32bit BGRA フレーム、ホットスポット座標の整合性を検証
uv run scripts/build_cursors.py --check
```

---

## 📁 ディレクトリ構成

```text
nemunemu-calico-cursor/
├── assets/
│   ├── gif/                     # 元アニメーション透過GIF (全8コマ・64x64 および 256x256 マスコット)
│   ├── sprites/                 # 原画スプライトシート (4列×2段 8コマPNG)
│   ├── preview/                 # ホットスポット座標検証ガイド (hotspot-guide.png)
│   ├── icon.svg                 # プロジェクトアイコン (128x128)
│   └── header.svg               # リポジトリヘッダーバナー (800x240)
├── cursors/                     # ビルド済み 32bit BGRA .ani / .cur ファイル
│   ├── *.ani / *.cur            # 標準 64x64 サイズ
│   ├── 48x48/                   # ミディアム 48x48 サイズ
│   └── 32x32/                   # コンパクト 32x32 サイズ
├── docs/                        # 日英バイリンガル VitePress ドキュメントサイト
├── scripts/
│   └── build_cursors.py         # RIFF ACON (.ani) / 32bit BGRA (.cur) ビルド・検証スクリプト
├── install.ps1                  # 自動バックアップ・即時反映対応 PowerShell インストーラ
├── uninstall.ps1                # バックアップ復元対応 PowerShell アンインストーラ
├── install.inf                  # 右クリック導入用 INF インストーラ
└── LICENSE                      # MIT License
```

---

## 📄 ライセンス

本プロジェクトは [MIT License](./LICENSE) の下で公開されています。Copyright (c) 2026 Sunwood-ai-labs.
