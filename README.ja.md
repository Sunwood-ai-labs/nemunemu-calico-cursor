<div align="center">
  <img src="./assets/header.ja.svg" alt="ねむねむ三毛ネコ カーソル バナー" width="800" />

  <h1>🐾 ねむねむ三毛ネコ カーソル (v3)</h1>

  <p><strong>ミントカラーのポインタに寄り添う「ねむねむ三毛ネコ」の Windows 10 / 11 用アニメーションマウスカーソルテーマ</strong></p>

  <p>
    <a href="https://github.com/Sunwood-ai-labs/nemunemu-calico-cursor/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/nemunemu-calico-cursor/ci.yml?branch=main&amp;label=CI&amp;logo=github" alt="CI Status" /></a>
    <a href="https://sunwood-ai-labs.github.io/nemunemu-calico-cursor/ja/"><img src="https://img.shields.io/badge/Docs-VitePress-38B2AC?logo=vitepress&amp;logoColor=white" alt="Documentation" /></a>
    <img src="https://img.shields.io/badge/Platform-Windows%2010%20%2F%2011-0078D6?logo=windows&amp;logoColor=white" alt="Windows 10 / 11" />
    <img src="https://img.shields.io/badge/Format-32--bit%20BGRA%20.ani%20%2F%20.cur-4A3B32" alt="32-bit BGRA .ani / .cur" />
    <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-DD6B20.svg" alt="MIT License" /></a>
  </p>

  <p>
    <a href="./README.md">English</a> | <strong>日本語</strong> | <a href="https://sunwood-ai-labs.github.io/nemunemu-calico-cursor/ja/">ドキュメント</a> | <a href="./CHANGELOG.md">リリースノート</a> | <a href="https://github.com/Sunwood-ai-labs/nemunemu-calico-cursor/releases">Releases</a>
  </p>
</div>

---

## ✨ 概要

**ねむねむ三毛ネコ カーソル (Nemunemu Calico Cursor v3)** は、爽やかなミントカラーのポインタの隣で三毛猫がぐーっと伸びをしたり、あくびをしたり、肉球を振ったり、回転リングの中で寝返りを打つ Windows 10 / 11 向けアニメーションマウスカーソルテーマです。すべてのカーソルは **全8フレーム・約160ms周期** の滑らかなループアニメーションで、余白を極限まで詰めたタイトクロップ＆背景完全透過の **32bit BGRA** フォーマット（`.ani` および静止画 `.cur`）として構築されています。

<div align="center">
  <img src="./assets/gif/04_calico_cat_256.gif" alt="ねむねむ三毛ネコ マスコットプレビュー (256x256)" width="160" />
</div>

- **日常操作の主要10ロールすべてを専用デザインで網羅（v3・10デザイン・10ロール収録）**: Windows標準の17種類のカーソル役割のうち、日常操作で使われる主要な **10種類すべて**（`Arrow`, `Hand`, `IBeam`, `Wait`, `AppStarting`, `Crosshair`, `No`, `SizeNS`, `SizeWE`, `SizeAll`）を個別の専用8コマアニメーションでカバー。特に **v3** では「待機（`Wait`）」と「バックグラウンド作業中（`AppStarting`：クリック可能な矢印＋小型スピナー）」を別デザインに分離し、`IBeam`（テキスト選択）の口元ディテール修正も行っています。
- **5段階のマルチサイズ展開 (`128` / `96` デフォルト / `64` / `48` / `32`)**: 全8コマの描画領域に合わせて余白をタイトクロップしているため、三毛猫がキャンバス目いっぱいに大きく表示されます（全6ディレクトリ・計120ファイルを自動検証）。
- **OSカーソル描画サイズの自動拡大 (`SPI_SETCURSORSIZE`)**: Windows の標準設定 (`CursorBaseSize = 32`) のままだと `.ani` が画面上で 32×32 に縮小描画されてしまいます。`install.ps1` は `CursorBaseSize`・`Accessibility\CursorSize`・Win32 API `SystemParametersInfo(SPI_SETCURSORSIZE)` を自動更新し、デフォルトで **96×96 の大サイズ**（または `-Size 128` で特大サイズ）に即時拡大します。
- **1ピクセル単位で調整されたホットスポット＆安全ロールバック**: 矢印の先端、指先、Iビームの中心軸、十字レティクル交点、リサイズ矢印中央、スピナー中心にホットスポットを厳密に配置。`uninstall.ps1` を実行すれば、カーソルだけでなくOSのカーソルサイズ設定（元の `32px`）も `backup-cursors.json` から即座に元通り復元されます。

---

## 🎨 カーソル一覧とホットスポット座標

### アニメーションカーソル プレビュー（全10デザイン・10ロール）

| プレビュー | カーソル名 | Windows ロール (`Registry`) | 収録ファイル (`.ani` / `.cur`) | v3 アニメーション説明 |
| :---: | :--- | :--- | :--- | :--- |
| <img src="./assets/gif/01_normal_64.gif" alt="Normal Select" width="64" /> | **Normal Select (通常選択)** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | ミント色の矢印ポインタの隣で、ぐーっと伸び＆あくびをする三毛猫。 |
| <img src="./assets/gif/02_link_64.gif" alt="Link Select" width="64" /> | **Link Select (リンクの選択)** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | ミント色の袖口の指差しハンドの横で、目を覚まして片手を振る三毛猫。 |
| <img src="./assets/gif/03_text_64.gif" alt="Text Select" width="64" /> | **Text Select (テキスト選択)** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | ミント色のIビームに掴まって縦に伸びをする三毛猫（v3で口元ディテールを修正、クリック軸はIビーム中央に厳密調整）。 |
| <img src="./assets/gif/04_busy_64.gif" alt="Busy" width="64" /> | **Busy (待ち状態)** | `Wait` | `nemunemu_busy.ani`<br>`nemunemu_busy.cur` | 8セグメントのミント色カプセルが回るリングの中で、ごろごろ寝返りを打つ待機（`Wait`）専用インジケータ。 |
| <img src="./assets/gif/05_working_64.gif" alt="Working in Background" width="64" /> | **Working (バックグラウンド作業中)** | `AppStarting` | `nemunemu_working.ani`<br>`nemunemu_working.cur` | v3で `Wait` から独立分離。左上のミント矢印でクリック操作を行いつつ、小型回転リングと三毛猫でバックグラウンド処理を示すデザイン。 |
| <img src="./assets/gif/06_precision_64.gif" alt="Precision Select" width="64" /> | **Precision Select (領域選択)** | `Crosshair` | `nemunemu_precision.ani`<br>`nemunemu_precision.cur` | ミント色の精密十字レティクルの横から三毛猫がひょっこり覗き込むデザイン（ホットスポットは十字交点）。 |
| <img src="./assets/gif/07_unavailable_64.gif" alt="Unavailable" width="64" /> | **Unavailable (利用不可)** | `No` | `nemunemu_unavailable.ani`<br>`nemunemu_unavailable.cur` | 禁止マーク（スラッシュ入りサークル）に寄り添い、ドラッグ＆ドロップ不可などを可愛く伝える三毛猫。 |
| <img src="./assets/gif/08_vertical_64.gif" alt="Vertical Resize" width="64" /> | **Vertical Resize (上下拡大/縮小)** | `SizeNS` | `nemunemu_vertical.ani`<br>`nemunemu_vertical.cur` | 上下双方向のミント色リサイズ矢印（`↕`）に沿って縦に伸び縮みする三毛猫（ホットスポットは矢印中央）。 |
| <img src="./assets/gif/09_horizontal_64.gif" alt="Horizontal Resize" width="64" /> | **Horizontal Resize (左右拡大/縮小)** | `SizeWE` | `nemunemu_horizontal.ani`<br>`nemunemu_horizontal.cur` | 左右双方向のミント色リサイズ矢印（`↔`）の上でゴロゴロ揺れる三毛猫（ホットスポットは矢印中央）。 |
| <img src="./assets/gif/10_move_64.gif" alt="Move" width="64" /> | **Move (移動)** | `SizeAll` | `nemunemu_move.ani`<br>`nemunemu_move.cur` | 4方向移動のミント色クロス矢印（`✥`）の隣で寄り添う三毛猫（ホットスポットは十字クロス中心）。 |

### ホットスポット検証ガイドと座標一覧

<div align="center">
  <img src="./assets/preview/hotspot-guide.png" alt="ホットスポット検証ガイド" width="800" />
</div>

| カーソルロール | 原画スプライトシート (4列×2段) | `128×128` | `96×96` (標準) | `64×64` | `48×48` | `32×32` |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Normal Select (`Arrow`)** | `assets/sprites/01_normal_sheet.png` | `(5, 8)` | **`(3, 6)`** | `(2, 4)` | `(2, 3)` | `(1, 2)` |
| **Link Select (`Hand`)** | `assets/sprites/02_link_sheet.png` | `(39, 2)` | **`(29, 1)`** | `(19, 1)` | `(14, 1)` | `(10, 0)` |
| **Text Select (`IBeam`)** | `assets/sprites/03_text_sheet.png` | `(16, 60)` | **`(12, 45)`** | `(8, 30)` | `(6, 22)` | `(4, 15)` |
| **Busy (`Wait`)** | `assets/sprites/04_busy_sheet.png` | `(64, 64)` | **`(48, 48)`** | `(32, 32)` | `(24, 24)` | `(16, 16)` |
| **Working (`AppStarting`)** | `assets/sprites/05_working_sheet.png` | `(4, 24)` | **`(3, 18)`** | `(2, 12)` | `(2, 9)` | `(1, 6)` |
| **Precision Select (`Crosshair`)** | `assets/sprites/06_precision_sheet.png` | `(35, 38)` | **`(26, 29)`** | `(18, 19)` | `(13, 14)` | `(9, 10)` |
| **Unavailable (`No`)** | `assets/sprites/07_unavailable_sheet.png` | `(40, 41)` | **`(30, 31)`** | `(20, 21)` | `(15, 15)` | `(10, 10)` |
| **Vertical Resize (`SizeNS`)** | `assets/sprites/08_vertical_sheet.png` | `(21, 63)` | **`(16, 47)`** | `(11, 32)` | `(8, 24)` | `(5, 16)` |
| **Horizontal Resize (`SizeWE`)** | `assets/sprites/09_horizontal_sheet.png` | `(64, 25)` | **`(48, 19)`** | `(32, 13)` | `(24, 10)` | `(16, 6)` |
| **Move (`SizeAll`)** | `assets/sprites/10_move_sheet.png` | `(42, 41)` | **`(32, 31)`** | `(21, 21)` | `(16, 15)` | `(11, 10)` |

---

## 🚀 クイックスタート（インストール方法）

### 方法1: PowerShell ワンコマンド適用（推奨）

リポジトリのルートディレクトリで以下のコマンドを実行します。カーソル一式を `%LOCALAPPDATA%\Cursors\NemunemuCalico` にコピーし、変更前の設定とカーソルサイズを `backup-cursors.json` に自動バックアップした上で、Win32 API `SystemParametersInfo(SPI_SETCURSORSIZE + SPI_SETCURSORS)` により再起動不要で全10ロールを即座に大きく反映します。

```powershell
# デフォルトの大サイズ (96x96) をインストール（推奨）
powershell -ExecutionPolicy Bypass -File .\install.ps1

# さらに大きい特大サイズ (128x128) をインストールする場合
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# 64x64 / 48x48 / 32x32 サイズを指定してインストールする場合
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 64
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 32
```

### 方法2: `install.inf` を使った GUI 導入

1. エクスプローラーで `install.inf` を右クリックし、**「インストール」** を選択します。
2. Windows の「マウスのプロパティ」（`Win + R` → `main.cpl` → **「ポインター」** タブ）を開きます。
3. デザイン（スキーム）一覧から **Nemunemu Calico** を選択して「適用」をクリックします。

---

## 🔄 アンインストール（元に戻す方法）

自動バックアップ（`%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json`）から導入前のカーソル設定および元のカーソルサイズ（`32px`）を復元し、インストール先フォルダをクリーンアップします。

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```

---

## 🛠️ ソースからのビルドと検証

全120個の `.ani` / `.cur`（10ロール × 2形式 × 6出力ディレクトリ）およびプレビュー `.gif` は、`assets/sprites/` 内の `v3` 全10種・8コマスプライトシート PNG から `scripts/build_cursors.py` によって自動切り出し・タイトクロップ・生成・検証されます。

```powershell
# 全サイズ (128/96/64/48/32) の .ani / .cur (計120ファイル)、透過GIF、ホットスポット検証画像を生成
uv run scripts/build_cursors.py

# 全120ファイルの RIFF ACON 構造、32bit BGRA フレーム、ホットスポット座標、Win32 LoadCursorFromFileW を検証
uv run scripts/build_cursors.py --check
```

---

## 📁 ディレクトリ構成

```text
nemunemu-calico-cursor/
├── assets/
│   ├── gif/                     # タイトクロップ済み透過GIFプレビュー (01..10 64x64 および 256x256 マスコット)
│   ├── sprites/                 # v3 原画スプライトシート全10種 (01..10 4列×2段 8コマ高解像度PNG)
│   ├── preview/                 # 全10ロール対応ホットスポット座標検証ガイド (hotspot-guide.png)
│   ├── icon.svg                 # プロジェクトアイコン (128x128)
│   ├── header.svg               # 英語版リポジトリヘッダーバナー (800x240)
│   └── header.ja.svg            # 日本語版リポジトリヘッダーバナー (800x240)
├── cursors/                     # ビルド済み 32bit BGRA .ani / .cur ファイル (全6フォルダ・計120ファイル)
│   ├── *.ani / *.cur            # デフォルト大サイズ 96x96 (10ロール × 2形式)
│   ├── 128x128/                 # 特大 128x128 サイズ (10ロール × 2形式)
│   ├── 96x96/                   # 大 96x96 サイズ (10ロール × 2形式)
│   ├── 64x64/                   # 中 64x64 サイズ (10ロール × 2形式)
│   ├── 48x48/                   # 小 48x48 サイズ (10ロール × 2形式)
│   └── 32x32/                   # 最小 32x32 サイズ (10ロール × 2形式)
├── docs/                        # 日英バイリンガル VitePress ドキュメントサイト
├── scripts/
│   └── build_cursors.py         # スプライト切り出し・タイトクロップ・.ani/.cur ビルド＆120ファイル検証スクリプト
├── install.ps1                  # SPI_SETCURSORSIZE 自動拡大・バックアップ・全10ロール即時反映インストーラ
├── uninstall.ps1                # バックアップ＆サイズ完全復元アンインストーラ
├── install.inf                  # 右クリック導入用 INF インストーラ (全10ロール登録)
└── LICENSE                      # MIT License
```

---

## 📄 ライセンス

本プロジェクトは [MIT License](./LICENSE) の下で公開されています。Copyright (c) 2026 Sunwood-ai-labs.
