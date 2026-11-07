# 🛠️ ビルドとカスタマイズ

`cursors/` ディレクトリ内のすべての `.ani` / `.cur` バイナリおよび `assets/gif/` 内のプレビュー GIF は、`assets/sprites/` 内の高解像度 4列×2段スプライトシート PNG から `scripts/build_cursors.py` によって再現可能にビルドされています。

---

## ⚙️ `scripts/build_cursors.py` の仕組み

1. **スプライトシート切り出し・背景ノイズ除去・タイトクロップ**:
   - 各 `1774×887` の 4列×2段スプライトシート（`assets/sprites/01_normal_sheet.png` 〜 `04_busy_sheet.png`）を8コマに分割します。
   - 極薄い半透明ノイズ（`alpha < 128 -> 0`）を完全透過にクレンジングし、全8コマの Union BBox に合わせて正方形タイトクロップを行うことで、余白をなくしてカーソルを大きく表示します。
2. **32bit BGRA `.cur` フレームのエンコード**:
   - 各フレームをボトムアップの `32bit BGRA` ピクセルデータに変換し、40バイトの `BITMAPINFOHEADER`（`biHeight = height * 2`, `biBitCount = 32`）と 32bit DWORD 境界パディング済みの 1-bpp AND マスクを付与します。
   - `ICONDIR`（`idType = 2`）および `ICONDIRENTRY` に、各解像度（`128×128`, `96×96`, `64×64`, `48×48`, `32×32`）ごとの正確なホットスポット座標 `(wXHotspot, wYHotspot)` を記録します。
3. **RIFF `ACON` `.ani` コンテナの構築**:
   - 全8コマの `.cur` データを `RIFF` (`ACON`) コンテナに格納し、`anih` ヘッダ（`cFrames = 8`, `cSteps = 8`, `jiffies = 10` ≒ `166.7ms`, `fl = AF_ICON`）および `LIST` (`fram` / `icon`) チャンクを出力します。

---

## 🔄 カーソル一式の再ビルド

仮想環境の手動管理不要で `uv run` から直接ビルドスクリプトを実行できます。

```powershell
# 全サイズ (128/96/64/48/32) の .ani / .cur、透過GIF、hotspot-guide.png を再生成
uv run scripts/build_cursors.py
```

---

## ✅ バイナリ整合性の検証 (`--check`)

`--check` オプションを指定すると、`cursors/` (96×96 デフォルト) および `cursors/{128x128,96x96,64x64,48x48,32x32}/` の全60ファイルが存在し、RIFF `ACON` / `ICONDIR` ヘッダ構造、各解像度のホットスポット座標 `(X, Y)`、および Win32 `LoadCursorFromFileW` によるネイティブロードがすべて正常であることを自動検証します。

```powershell
uv run scripts/build_cursors.py --check
```

---

## ✏️ ホットスポット座標やアニメーション速度のカスタマイズ

`assets/sprites/` 内のスプライトシートを編集したり、クリック位置や再生速度を調整したい場合は以下の手順で行えます。

1. `scripts/build_cursors.py` を開きます。
2. 各カーソルの `crop_box`、`hotspots`、または `jiffies`（`1 jiffy = 1/60 秒`）の設定値を変更します。
3. `uv run scripts/build_cursors.py` と `uv run scripts/build_cursors.py --check` を実行します。
4. 生成された `assets/preview/hotspot-guide.png` を開き、赤い十字マークが意図したポインタ先端に合っているか確認します。
