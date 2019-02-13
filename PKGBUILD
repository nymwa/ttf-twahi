# Maintainer: nymwa <@nymwa>
pkgname=ttf-twahi
pkgver=$(date +"%y%m%d")
pkgrel=1
pkgdesc="Hand written Osa font"
arch=('any')
url="https://github.com/nymwa/ttf-twahi"
license=('GPL')
depends=()
makedepends=('python' 'fontforge' 'potrace' 'imagemagick')
provides=('ttf-font')

build() {
	cd "$srcdir"
	chmod +x gentwahi.py
	python gentwahi.py
}

package() {
	cd "$srcdir"
	install -d "$pkgdir/usr/share/fonts/TTF"
	install -m644 twahi.ttf "$pkgdir/usr/share/fonts/TTF/"
	rm twahi.ttf
}
