# 🚀 導入ガイド (Getting Started)

**ねむねむ三毛ネコ カーソル (Nemunemu Calico Cursor)** は、PowerShell ワンコマンドスクリプトまたは `install.inf` の右クリックメニューから、Windows 10 / 11 環境へ数秒で導入できます。

---

## ⚡ 方法1: PowerShell ワンコマンド適用（推奨）

`install.ps1` は以下の4つのステップを安全に自動実行します。

1. 指定されたサイズのカーソルファイルを `%LOCALAPPDATA%\Cursors\NemunemuCalico` にコピーします。
2. 変更前の `HKCU:\Control Panel\Cursors` レジストリ設定を `%LOCALAPPDATA%\Cursors\NemunemuCalico\backup-cursors.json` に自動保存します（初回導入時の設定を保持します）。
3. `Arrow`、`Hand`、`IBeam`、`Wait`、`AppStarting` の各ロールと **Nemunemu Calico** スキームをレジストリに登録します。
4. Win32 API `SystemParametersInfo(SPI_SETCURSORS)` を呼び出し、**Windows の再起動やサインアウト不要で即座にカーソルを反映**します。

### 標準サイズ (`64×64`) のインストール

```powershell
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

### サイズを変更してインストール (`48×48` / `32×32`)

画面解像度やスケーリング設定に合わせて小さめのサイズを使いたい場合は、`-Size` パラメータを指定します。

```powershell
# ミディアム 48x48 サイズを適用
powershell -ExecutionPolicy Bypass -File .\install.ps1 -Size 48

# コンパクト 32x32 サイズを適用
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

`uninstall.ps1` を実行すると、`backup-cursors.json` に保存された導入前のカーソル設定を正確に復元し、スキーム登録と `%LOCALAPPDATA%\Cursors\NemunemuCalico` フォルダをクリーンアップして即時反映します。

```powershell
powershell -ExecutionPolicy Bypass -File .\uninstall.ps1
```
