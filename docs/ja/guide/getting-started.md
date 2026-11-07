# 🚀 導入ガイド (Getting Started)

**ねむねむ三毛ネコ カーソル v2 (Nemunemu Calico Cursor)** は、PowerShell ワンコマンドスクリプトまたは `install.inf` の右クリックメニューから、Windows 10 / 11 環境へ数秒で導入できます。

---

## ⚡ 方法1: PowerShell ワンコマンド適用（推奨）

`install.ps1` は以下の5つのステップを安全に自動実行します。

1. 指定されたサイズ（`128`, `96` デフォルト, `64`, `48`, `32`）のカーソルファイルを `%LOCALAPPDATA%\Cursors\NemunemuCalico` にコピーします。
2. 変更前の `HKCU:\Control Panel\Cursors` レジストリ設定および元のカーソルサイズ（`CursorBaseSize` / `Accessibility\CursorSize`）を `%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json` に自動保存します。
3. `Arrow`、`Hand`、`IBeam`、`Wait`、`AppStarting` の各ロールと **Nemunemu Calico** スキームをレジストリに登録します。
4. `CursorBaseSize` と `Accessibility\CursorSize` を更新し、Win32 API `SystemParametersInfo(SPI_SETCURSORSIZE)` を呼び出すことで、OS側の32px縮小を解除して指定サイズ（標準 `96×96`、最大 `128×128`）で大きくくっきり描画させます。
5. Win32 API `SystemParametersInfo(SPI_SETCURSORS)` を呼び出し、**Windows の再起動やサインアウト不要で即座にカーソルを反映**します。

### デフォルトの大サイズ (`96×96`) のインストール

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### 特大サイズ (`128×128`) や中・小サイズ (`64×64` / `48×48` / `32×32`) を選ぶ場合

画面解像度やお好みに合わせて `-Size` パラメータを指定できます。

```powershell
# 特大 128x128 サイズを適用
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 128

# ミディアム 64x64 サイズを適用
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 64

# コンパクト 48x48 / 32x32 サイズを適用
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 32
```

---

## 🖱️ 方法2: `install.inf` による GUI インストール

エクスプローラーからスキーム登録を行う手順です。

1. リポジトリ直下の `install.inf` を右クリックし、**「インストール」** を選択します。
2. `Win + R` キーを押して `main.cpl` と入力し、**「マウスのプロパティ」** を開きます。
3. **「ポインター」** タブに切り替え、「デザイン」一覧から **Nemunemu Calico** を選択して **「適用」** をクリックします。

---

## 🔄 アンインストール（元に戻す方法）

`uninstall.ps1` を実行すると、`backup-cursors.json` に保存された導入前のカーソル設定および元のカーソル描画サイズ（`32px`）を正確に復元し、スキーム登録と `%LOCALAPPDATA%\Cursors\NemunemuCalico` フォルダをクリーンアップして即時反映します。

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
