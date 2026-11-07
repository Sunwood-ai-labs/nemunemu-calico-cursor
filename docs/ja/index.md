---
layout: home

hero:
  name: "ねむねむ三毛ネコ カーソル v2"
  text: "ミント色のポインタに寄り添う三毛猫テーマ"
  tagline: "Windows 10 / 11 対応・全8フレーム 32bit BGRA 透過アニメーションカーソル。余白を詰めた大サイズ表示 (128 / 96 / 64 / 48 / 32) とワンコマンド即時導入に対応。"
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
    title: 表情豊かな v2 8コマアニメーション
    details: 通常選択（伸び＆あくび）、リンク選択（片手を振る）、テキスト選択（Iビームで縦伸び）、待ち・作業中（回転リング内で寝返り）を滑らかな8フレームで表現。
  - icon: 🔎
    title: 大サイズでくっきり表示 (SPI_SETCURSORSIZE)
    details: セル余白を詰めたタイトクロップに加え、Windows のカーソル描画サイズも自動で 96×96（最大 128×128）へ拡大して即座に大きく表示します。
  - icon: 🎯
    title: 1ピクセル単位で調整されたホットスポット
    details: 矢印の先端、指先、Iビームの中央軸、スピナーの中心にホットスポット（クリック判定点）を厳密に設定。猫のイラストが操作の邪魔になりません。
  - icon: ⚡
    title: 再起動不要の即時適用＆ワンコマンド復元
    details: PowerShell と Win32 API によりサインアウト不要で即時反映。uninstall.ps1 で元のカーソルと元のサイズ（32px）へいつでも戻せます。
---

## 🎨 アニメーションカーソル プレビュー

| プレビュー | カーソル名 | Windows ロール | ファイル名 (`.ani` / `.cur`) | ホットスポット (`128` / `96` 標準 / `64` / `48` / `32`) |
| :---: | :--- | :--- | :--- | :---: |
| ![Normal Select](/assets/gif/01_normal_64.gif) | **Normal Select (通常選択)** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | `(5, 8)` / **`(3, 6)`** / `(2, 4)` / `(2, 3)` / `(1, 2)` |
| ![Link Select](/assets/gif/02_link_64.gif) | **Link Select (リンクの選択)** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | `(39, 2)` / **`(29, 1)`** / `(19, 1)` / `(14, 1)` / `(10, 0)` |
| ![Text Select](/assets/gif/03_text_64.gif) | **Text Select (テキスト選択)** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | `(16, 60)` / **`(12, 45)`** / `(8, 30)` / `(6, 22)` / `(4, 15)` |
| ![Busy / Working](/assets/gif/04_busy_64.gif) | **Busy / Working (待ち・作業中)** | `Wait`<br>`AppStarting` | `nemunemu_busy.ani`<br>`nemunemu_working.ani` | `(64, 64)` / **`(48, 48)`** / `(32, 32)` / `(24, 24)` / `(16, 16)` |

## 🚀 クイックインストール

```powershell
# デフォルトの大サイズ (96x96) を即座に適用（再起動不要）
powershell -ExecutionPolicy Bypass -File .\install.ps1

# 特大サイズ (128x128) を適用する場合
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# 元のカーソル設定と元のサイズ (32px) に戻す場合
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
