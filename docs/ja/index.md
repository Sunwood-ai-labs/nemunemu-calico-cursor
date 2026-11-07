---
layout: home

hero:
  name: "ねむねむ三毛ネコ カーソル v3"
  text: "ミント色のポインタに寄り添う三毛猫テーマ"
  tagline: "Windows 10 / 11 対応・日常操作の主要10ロールすべてを専用8コマ 32bit BGRA 透過アニメーションで網羅。余白を詰めた大サイズ表示 (128 / 96 / 64 / 48 / 32) とワンコマンド即時導入に対応。"
  image:
    src: /assets/gif/04_calico_cat_256.gif
    alt: ねむねむ三毛ネコ マスコット
  actions:
    - theme: brand
      text: 導入ガイド (Getting Started)
      link: /ja/guide/getting-started
    - theme: alt
      text: カーソル＆ホットスポット一覧
      link: /ja/guide/cursors-and-hotspots
    - theme: alt
      text: GitHub リポジトリ
      link: https://github.com/Sunwood-ai-labs/nemunemu-calico-cursor

features:
  - icon: 🐾
    title: 主要10ロール完全対応の v3 8コマアニメ
    details: 通常選択・リンク・テキスト（口元修正済）・待ち状態・バックグラウンド作業中（矢印＋スピナーに分離）・領域選択・利用不可・上下/左右リサイズ・移動の全10種類を専用デザインで収録。
  - icon: 🔎
    title: 大サイズでくっきり表示 (SPI_SETCURSORSIZE)
    details: セル余白を詰めたタイトクロップに加え、Windows のカーソル描画サイズも自動で 96×96（最大 128×128）へ拡大して即座に大きく表示します。
  - icon: 🎯
    title: 1ピクセル単位で調整されたホットスポット
    details: 矢印の先端、指先、Iビームの中央軸、十字交点、リサイズ矢印の中心にホットスポット（クリック判定点）を厳密に設定（全120ファイル検証済）。
  - icon: ⚡
    title: 再起動不要の即時適用＆ワンコマンド復元
    details: PowerShell と Win32 API によりサインアウト不要で全10ロールを即時反映。uninstall.ps1 で元のカーソルと元のサイズ（32px）へいつでも戻せます。
---

## 🎨 アニメーションカーソル プレビュー（全10デザイン・10ロール）

| プレビュー | カーソル名 | Windows ロール | ファイル名 (`.ani` / `.cur`) | ホットスポット (`128` / `96` 標準 / `64` / `48` / `32`) |
| :---: | :--- | :--- | :--- | :---: |
| ![Normal Select](/assets/gif/01_normal_64.gif) | **Normal Select (通常選択)** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | `(5, 8)` / **`(3, 6)`** / `(2, 4)` / `(2, 3)` / `(1, 2)` |
| ![Link Select](/assets/gif/02_link_64.gif) | **Link Select (リンクの選択)** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | `(39, 2)` / **`(29, 1)`** / `(19, 1)` / `(14, 1)` / `(10, 0)` |
| ![Text Select](/assets/gif/03_text_64.gif) | **Text Select (テキスト選択)** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | `(16, 60)` / **`(12, 45)`** / `(8, 30)` / `(6, 22)` / `(4, 15)` |
| ![Busy](/assets/gif/04_busy_64.gif) | **Busy (待ち状態)** | `Wait` | `nemunemu_busy.ani`<br>`nemunemu_busy.cur` | `(64, 64)` / **`(48, 48)`** / `(32, 32)` / `(24, 24)` / `(16, 16)` |
| ![Working](/assets/gif/05_working_64.gif) | **Working (バックグラウンド作業中)** | `AppStarting` | `nemunemu_working.ani`<br>`nemunemu_working.cur` | `(4, 24)` / **`(3, 18)`** / `(2, 12)` / `(2, 9)` / `(1, 6)` |
| ![Precision Select](/assets/gif/06_precision_64.gif) | **Precision Select (領域選択)** | `Crosshair` | `nemunemu_precision.ani`<br>`nemunemu_precision.cur` | `(35, 38)` / **`(26, 29)`** / `(18, 19)` / `(13, 14)` / `(9, 10)` |
| ![Unavailable](/assets/gif/07_unavailable_64.gif) | **Unavailable (利用不可)** | `No` | `nemunemu_unavailable.ani`<br>`nemunemu_unavailable.cur` | `(40, 41)` / **`(30, 31)`** / `(20, 21)` / `(15, 15)` / `(10, 10)` |
| ![Vertical Resize](/assets/gif/08_vertical_64.gif) | **Vertical Resize (上下拡大/縮小)** | `SizeNS` | `nemunemu_vertical.ani`<br>`nemunemu_vertical.cur` | `(21, 63)` / **`(16, 47)`** / `(11, 32)` / `(8, 24)` / `(5, 16)` |
| ![Horizontal Resize](/assets/gif/09_horizontal_64.gif) | **Horizontal Resize (左右拡大/縮小)** | `SizeWE` | `nemunemu_horizontal.ani`<br>`nemunemu_horizontal.cur` | `(64, 25)` / **`(48, 19)`** / `(32, 13)` / `(24, 10)` / `(16, 6)` |
| ![Move](/assets/gif/10_move_64.gif) | **Move (移動)** | `SizeAll` | `nemunemu_move.ani`<br>`nemunemu_move.cur` | `(42, 41)` / **`(32, 31)`** / `(21, 21)` / `(16, 15)` / `(11, 10)` |

## 🚀 クイックインストール

```powershell
# デフォルトの大サイズ (96x96) を即座に適用（再起動不要）
powershell -ExecutionPolicy Bypass -File .\install.ps1

# 特大サイズ (128x128) を適用する場合
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# 元のカーソル設定と元のサイズ (32px) に戻す場合
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
