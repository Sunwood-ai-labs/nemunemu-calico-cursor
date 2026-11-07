---
layout: home

hero:
  name: "ねむねむ三毛ネコ カーソル"
  text: "ミント色のポインタに寄り添う三毛猫テーマ"
  tagline: "Windows 10 / 11 対応・全8フレーム 32bit BGRA 透過アニメーションカーソル。1ピクセル単位で調整されたホットスポットとワンコマンド導入スクリプトを収録。"
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
    title: 4種のデザイン・5つのロールをカバー
    details: 通常選択 (Arrow)、リンク選択 (Hand)、テキスト選択 (IBeam)、待ち状態・作業中 (Wait & AppStarting) を全8コマ（約160ms周期）のなめらかなループで表現。
  - icon: 🎯
    title: 1ピクセル単位で調整されたホットスポット
    details: 矢印の先端、指先、Iビームの中央軸、スピナーの中心にホットスポット（クリック判定点）を厳密に設定。猫のイラストが操作の邪魔になりません。
  - icon: 📐
    title: 3サイズ展開 (64×64, 48×48, 32×32)
    details: 背景完全透過の 32bit BGRA フォーマットで、標準 64×64、ミディアム 48×48、コンパクト 32×32 の3解像度を同梱。
  - icon: ⚡
    title: 再起動不要の即時適用＆ワンコマンド復元
    details: PowerShell と Win32 API SystemParametersInfo により再起動なしで即座に反映。変更前の設定は backup-cursors.json に自動バックアップされます。
---

## 🎨 アニメーションカーソル プレビュー

| プレビュー | カーソル名 | Windows ロール | ファイル名 (`.ani` / `.cur`) | ホットスポット (`64×64` / `48×48` / `32×32`) |
| :---: | :--- | :--- | :--- | :---: |
| ![Normal Select](/assets/gif/01_normal_64.gif) | **Normal Select (通常選択)** | `Arrow` | `nemunemu_normal.ani`<br>`nemunemu_normal.cur` | `(11, 9)` / `(8, 7)` / `(6, 5)` |
| ![Link Select](/assets/gif/02_link_64.gif) | **Link Select (リンクの選択)** | `Hand` | `nemunemu_link.ani`<br>`nemunemu_link.cur` | `(21, 6)` / `(16, 5)` / `(11, 3)` |
| ![Text Select](/assets/gif/03_text_64.gif) | **Text Select (テキスト選択)** | `IBeam` | `nemunemu_text.ani`<br>`nemunemu_text.cur` | `(18, 32)` / `(14, 24)` / `(9, 16)` |
| ![Busy / Working](/assets/gif/04_busy_64.gif) | **Busy / Working (待ち・作業中)** | `Wait`<br>`AppStarting` | `nemunemu_busy.ani`<br>`nemunemu_working.ani` | `(32, 32)` / `(24, 24)` / `(16, 16)` |

## 🚀 クイックインストール

```powershell
# 標準 64x64 サイズを即座に適用（再起動不要）
powershell -ExecutionPolicy Bypass -File .\install.ps1

# 元のカーソル設定に戻す場合
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
