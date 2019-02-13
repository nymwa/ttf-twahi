# ttf-twahi
オサフォント"twahi"のデータとビルド用のコードです

## 依存パッケージ
自分でビルドする場合は，python(3.7以上),potrace,imagemagick,fontforgeが必要です．

## インストール方法
### ビルド済のものをpacmanでインストールする方法(Arch linux使い向け)
`README.md`と同じディレクトリで
	$ sudo pacman -U ttf-twahi-YYMMDD-1-any.pkg.tar.xz
とすればインストール完了です．
YYMMDDの部分は最も新しい日付にしてください．

アンインストールは
	$ sudo pacman -R ttf-twahi
です．

### PKGBUILDでビルドしてpacmanでインストールする方法(Arch linux使い向け)
`README.md`と同じディレクトリで
	$ makepkg
とすると，
`ttf-twahi-YYMMDD-1-any.pkg.tar.xz`が生成されるので，
そのパッケージを上の「ビルド済のものをpacmanでインストールする方法」を参照してインストールしてください．

### Arch linux以外のUnix/Linuxでtwahi.ttfをビルドする方法
`README.md`と同じディレクトリで
	sh gen-twahi.sh
とすると，ビルドされ，`twahi.ttf`が現在のディレクトリに生成されます．

この際，python,potrace,imagemagick(convertコマンド),fontforgeがインストールされていて，`src/gentwahi.py`が実行可能であるかに注意してください．

### ビルドせずにtwahi.ttfを得る方法
`ttf-twahi-YYMMDD-1-any.pkg.tar.xz`のうち最新のものを解凍し，`twahi.ttf`を探してください．
