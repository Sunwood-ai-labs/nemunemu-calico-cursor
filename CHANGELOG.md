# Changelog / リリースノート

All notable changes to **Nemunemu Calico Cat Cursor (`nemunemu-calico-cursor`)** are documented in this file.  
「**ねむねむ三毛ネコ カーソル**」のバージョン履歴・更新内容を記載しています。

---

## [v3.0.0] - 2026-11-07

### 🇬🇧 English — Full 10-Role Animated Cursor Set (120 Binaries)

#### ✨ Added (6 New Dedicated Animated Cursor Roles)
- **05 Working in Background (`AppStarting` / `OCR_APPSTARTING = 32650`)**: Mint arrow pointer + miniature rotating ring + calico cat (`05_working_sheet.png`, Hotspot `26, 20` @ 96×96). Replaces the v2 fallback that shared `01_normal`.
- **06 Precision Select (`Crosshair` / `OCR_CROSS = 32515`)**: Center crosshair with cat ears & tail swaying (`06_precision_sheet.png`, Hotspot `48, 48` @ 96×96).
- **07 Unavailable (`No` / `OCR_NO = 32648`)**: Coral forbidden circle with a sleepy head-shaking calico cat (`07_unavailable_sheet.png`, Hotspot `48, 48` @ 96×96).
- **08 Vertical Resize (`SizeNS` / `OCR_SIZENS = 32645`)**: Vertical double-headed arrow with the cat stretching up and down (`08_vertical_sheet.png`, Hotspot `48, 48` @ 96×96).
- **09 Horizontal Resize (`SizeWE` / `OCR_SIZEWE = 32644`)**: Horizontal double-headed arrow with the cat swaying left and right (`09_horizontal_sheet.png`, Hotspot `48, 48` @ 96×96).
- **10 Move (`SizeAll` / `OCR_SIZEALL = 32646`)**: Four-way move cross arrow with a sleeping calico cat (`10_move_sheet.png`, Hotspot `48, 48` @ 96×96).

#### 🎨 Improved & Fixed
- **03 Text Select (`IBeam` / `OCR_IBEAM = 32513`)**: Redrawn mouth expression on the sleeping calico cat (`03_text_sheet.png`) while keeping the I-beam center hotspot (`23, 50` @ 96×96) rock-steady across all 8 frames.
- **Integer-Cell Sprite Sheet Normalization (`scripts/build_cursors.py`)**: Added `normalize_sheet()` to automatically resize non-divisible 4×2 sprite sheets (`1774×887` px in `03`, `06`, `07`, `08`, `09`, `10`) to `1776×888` px (`444×444` px per cell) via `Image.Resampling.LANCZOS`, eliminating 1px sub-pixel jitter between frames.
- **10-Role Installer & Uninstaller (`install.ps1`, `uninstall.ps1`, `install.inf`)**: Mapped all 10 Windows system cursor roles in `HKCU:\Control Panel\Cursors`, the `Nemunemu Calico Cat` scheme string (10 slots), and live `LoadImageW` + `SetSystemCursor` injection.
- **120 Verified Cursor Binaries**: Built and verified 10 roles × (`.ani` + `.cur`) × 5 size tiers (`32x32`, `48x48`, `64x64`, `96x96`, `128x128` + root `96x96` defaults) = **120 files** with Win32 `LoadCursorFromFileW`.

---

### 🇯🇵 日本語 — 全10種・10システムロール完全対応（計120バイナリ）

#### ✨ 新規追加（6種の専用8コマアニメーションカーソル）
- **05 バックグラウンド作業中 (`AppStarting` / `OCR_APPSTARTING = 32650`)**: ミント矢印＋ミニ回転リング＋三毛猫の専用スプライト（`05_working_sheet.png`、96×96時ホットスポット `26, 20`）を追加。v2 までの通常選択との共用を解消し、独立した専用アニメになりました。
- **06 領域選択 (`Crosshair` / `OCR_CROSS = 32515`)**: 猫耳付きの十字クロスヘアと揺れるしっぽの8コマアニメ（`06_precision_sheet.png`、ホットスポット中央 `48, 48`）。
- **07 利用不可 (`No` / `OCR_NO = 32648`)**: コーラルレッドの禁止マークと首をかしげる三毛猫の8コマアニメ（`07_unavailable_sheet.png`、ホットスポット中央 `48, 48`）。
- **08 上下拡大縮小 (`SizeNS` / `OCR_SIZENS = 32645`)**: 上下双方向矢印と伸びをする三毛猫の8コマアニメ（`08_vertical_sheet.png`、ホットスポット中央 `48, 48`）。
- **09 左右拡大縮小 (`SizeWE` / `OCR_SIZEWE = 32644`)**: 左右双方向矢印と揺れる三毛猫の8コマアニメ（`09_horizontal_sheet.png`、ホットスポット中央 `48, 48`）。
- **10 移動 (`SizeAll` / `OCR_SIZEALL = 32646`)**: 四方向移動クロス矢印と眠る三毛猫の8コマアニメ（`10_move_sheet.png`、ホットスポット中央 `48, 48`）。

#### 🎨 改善・修正
- **03 テキスト選択 (`IBeam` / `OCR_IBEAM = 32513`)**: Iビームに寄り添う三毛猫の口元表現をブラッシュアップ（`03_text_sheet.png`）。Iビーム縦棒中央のホットスポット（`23, 50` @ 96×96）は全8コマで完全に固定。
- **非整数セルサイズ（`1774×887`）の自動正規化（`scripts/build_cursors.py`）**: 4列×2行で割り切れないスプライトシート（`1774×887` px）をスライス前に `1776×888` px（1コマあたり厳密に `444×444` px）へ `LANCZOS` 補正する `normalize_sheet()` を実装し、コマ間の1px端数ズレを完全に防止。
- **全10ロール対応インストーラ（`install.ps1`, `uninstall.ps1`, `install.inf`）**: レジストリ設定・スキーム文字列（10スロット）・Win32 `LoadImageW` + `SetSystemCursor` によるサインアウト不要の即時メモリ注入を全10ロールへ拡張。
- **全120バイナリの自動検証**: 10種 × (`.ani` + `.cur`) × 5サイズ（`32x32`, `48x48`, `64x64`, `96x96`, `128x128` ＋ ルート標準 `96x96`）＝ **計120ファイル**を Win32 `LoadCursorFromFileW` で検証し、10種一覧の `assets/preview/hotspot-guide.png` を更新。

---

## [v2.0.0] - 2026-11-07

### 🇬🇧 English — Dynamic 8-Frame Sprites, Tight-Cropped Multi-Size Tiers & Win32 Live Injection

#### ✨ Added & Improved
- **Upgraded v2 Dynamic Sprite Sheets**: Replaced the initial subtle animations with lively 8-frame animations (swaying body, popping sleep bubbles, wagging tail, rotating dashed spinner).
- **Tight Bounding-Box Cropping (`margin_ratio = 0.04`)**: Eliminated excessive transparent padding around the artwork so the cursor appears crisp and large even at standard sizes.
- **5 Size Tiers (`32x32` to `128x128`)**: Added `32x32`, `48x48`, `64x64`, `96x96` (default), and `128x128` builds alongside `-Size` parameter support in `install.ps1`.

#### 🐛 Fixed
- **Fixed Screenshot Downscaling (`32×32` fallback)**: Bypassed Windows logon `SM_CXCURSOR (32px)` downscaling by injecting native `96×96` `HCURSOR` handles directly via Win32 `LoadImageW` + `SetSystemCursor`.
- **Fixed 3× DWM Double-Scaling Overflow (`288px` disappearing cursor on `Win+Shift+S`)**: Reset `SPI_SETCURSORSIZE (0x2029)` to `32` (1.0× base scale) before injecting custom-sized `HCURSOR` handles so `96×96` cursors stay safely within the 256×256 compositor limit.
- **Bilingual SVG Hero Banners**: Split hero banners into `assets/header.svg` (English) and `assets/header.ja.svg` (Japanese) with `clipPath` rounded borders and a 2×2 role showcase grid.

### 🇯🇵 日本語 — v2 ダイナミック8コマ原画・余白タイトクロップ・Win32 即時注入と二重拡大バグ修正

#### ✨ 追加・改善
- **v2 ダイナミック8コマ原画への刷新**: 鼻ちょうちんの膨らみ・しっぽの揺れ・破線リング回転など、小サイズでも動きがはっきり分かる8コマ原画へアップデート。
- **全8コマ合成バウンディングボックスによる余白最小化（余白4%）**: スプライト周辺の無駄な透明余白を削り、ホットスポットを1pxもブレさせずにイラストの表示密度を最大化。
- **5段階のサイズ展開（`32x32` 〜 `128x128`）**: 標準の `96x96` に加え、5種類のサイズフォルダと `install.ps1 -Size` オプションを追加。

#### 🐛 バグ修正
- **スクショ撮影時に `32×32` に縮小される問題の修正**: `SPI_SETCURSORS` のみではログオン時の `SM_CXCURSOR (32px)` に丸められる仕様を回避するため、`LoadImageW` + `SetSystemCursor` で指定サイズの `HCURSOR` を直接メモリ注入する処理を追加。
- **DWM 3倍拡大との重複による `288px` 巨大化・`Win+Shift+S` 消失バグの修正**: `SPI_SETCURSORSIZE (0x2029)` を `32`（等倍 1.0x）にリセットした上で `96×96` の `HCURSOR` を注入することで、見た目とスクリーンショットキャプチャのサイズを完全一致化。
- **日英 SVG ヘッダーバナーの分離と整形**: `header.svg`（英語）と `header.ja.svg`（日本語）に分離し、`clipPath` と2×2ロールグリッドでレイアウト崩れを解消。

---

## [v1.0.0] - 2026-11-07

### 🇬🇧 English — Initial Release
- Initial release with 4 animated cursor designs (`Normal`, `Link`, `Text`, `Busy`) mapped across 5 Windows cursor roles.
- Pure-Python RIFF `ACON` (`.ani`) and `.cur` builder (`scripts/build_cursors.py`) with Win32 `LoadCursorFromFileW` validation.
- PowerShell installer (`install.ps1`), uninstaller with automatic JSON backup (`uninstall.ps1`), and Explorer `.inf` installer (`install.inf`).
- Bilingual documentation (`README.md`, `README.ja.md`) and VitePress documentation site with GitHub Actions CI/CD.

### 🇯🇵 日本語 — 初回リリース
- 初期4種のアニメーションカーソル（`Normal`, `Link`, `Text`, `Busy` / 5システムロール割り当て）を公開。
- Pure Python による RIFF `ACON` (`.ani`) / `.cur` ビルダースクリプト（`scripts/build_cursors.py`）および Win32 API 検証パイプラインの構築。
- 自動バックアップ付き PowerShell インストーラ（`install.ps1` / `uninstall.ps1`）と右クリック用 `install.inf` の同梱。
- 日英バイリンガル README および VitePress ドキュメントサイト・GitHub Actions ワークフローの整備。
