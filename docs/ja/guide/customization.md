# 🛠️ ビルドとカスタマイズ

`cursors/` ディレクトリ内のすべての `.ani` および `.cur` バイナリは、`assets/gif/` 内の透過 GIF アニメーションから `scripts/build_cursors.py` によって再現可能にビルドされています。

---

## ⚙️ `scripts/build_cursors.py` の仕組み

Windows のアニメーションカーソル（`.ani`）と静止画カーソル（`.cur`）は以下のバイナリ仕様に従って生成されます。

1. **32bit BGRA `.cur` フレームのエンコード**:
   - 各フレームをボトムアップの `32bit BGRA` ピクセルデータに変換し、40バイトの `BITMAPINFOHEADER`（`biHeight = height * 2`, `biBitCount = 32`）と 32bit DWORD 境界パディング済みの 1-bpp AND マスクを付与します。
   - `ICONDIR`（カーソルを示す `idType = 2`）および `ICONDIRENTRY` に、各解像度（`64×64`, `48×48`, `32×32`）ごとの正確なホットスポット座標 `(wXHotspot, wYHotspot)` を記録します。
2. **RIFF `ACON` `.ani` コンテナの構築**:
   - 全8コマの `.cur` データを `RIFF` (`ACON`) コンテナに格納し、`anih` ヘッダ（`cFrames = 8`, `cSteps = 8`, `iDispRate = 10` jiffies ≒ `166.7ms`, `fl = AF_ICON`）、`rate` チャンク、`seq ` チャンク、`fram` (`icon`) リストを出力します。

---

## 🔄 カーソル一式の再ビルド

仮想環境の手動管理不要で `uv run` から直接ビルドスクリプトを実行できます。

```powershell
# 全サイズ (64x64, 48x48, 32x32) の .ani / .cur と hotspot-guide.png を再生成
uv run scripts/build_cursors.py
```

---

## ✅ バイナリ整合性の検証 (`--check`)

`--check` オプションを指定すると、`cursors/`, `cursors/48x48/`, `cursors/32x32/` の全ファイルが存在し、RIFF `ACON` / `ICONDIR` ヘッダ構造、フレーム数（8フレーム）、および各解像度のホットスポット座標 `(X, Y)` が仕様通りであることを自動検証します。

```powershell
uv run scripts/build_cursors.py --check
```

---

## ✏️ ホットスポット座標やアニメーション速度のカスタマイズ

`assets/gif/` 内の GIF アニメーションを差し替えたり、クリック位置や再生速度を調整したい場合は以下の手順で行えます。

1. `scripts/build_cursors.py` を開きます。
2. 各カーソルのホットスポット座標や `jiffies`（`1 jiffy = 1/60 秒`）の設定値を変更します。
3. `uv run scripts/build_cursors.py` と `uv run scripts/build_cursors.py --check` を実行します。
4. 生成された `assets/preview/hotspot-guide.png` を開き、赤い十字マークが意図したポインタ先端に合っているか確認します。
