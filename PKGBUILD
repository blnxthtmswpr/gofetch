pkgname="blinx-gofetch"
pkgver="1.1.0"
pkgrel="1"
pkgdesc="Fetch system stats with gofetch"
arch=("x86_64")

depends=("python")
license=("GPL-3.0-or-later")
source("gofetch" "blinx-gofetch.py")
sha512sums=("SKIP")

package() {
	mkdir -p "${pkgdir}/usr/bin"
	cp "${srcdir}/blinx-gofetch.py" "${pkgdir}/usr/bin/blinx-gofetch.py"
	cp "${srcdir}/gofetch" "${pkgdir}/usr/bin/gofetch"
	chmod +x "${pkgdir}/usr/bin/gofetch"
}
