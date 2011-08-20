#!/bin/sh
#
# simple tar-it-up script for pygtasks
# Copyright 2011  Vincent Batts, Vienna, VA, USA
# All rights reserved.
#
# Redistribution and use of this script, with or without modification, is
# permitted provided that the following conditions are met:
#
# 1. Redistributions of this script must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY EXPRESS OR IMPLIED
# WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


PRGNAM=pygtasks
VERSION=0.9.0
BUILD=${BUILD:-1}
TAG=${TAG:-vb}

if [ -z "$ARCH" ]; then
  case "$( uname -m )" in
    i?86) ARCH=i486 ;;
    arm*) ARCH=arm ;;
       *) ARCH=$( uname -m ) ;;
  esac
fi

CWD=$(pwd)
PKG=$CWD/tmp
IS_SLACK=false
MAKEPKG="/sbin/makepkg"
FAKEROOT="/usr/bin/fakeroot"

set -e

[[ -f $MAKEPKG ]] && IS_SLACK=true
[[ ! -f /usr/bin/fakeroot ]] && FAKEROOT=""
[[ ! -f setup.py ]] && exit 2
[[ -d tmp ]] && rm -rf tmp/

python setup.py install --root $PKG

cd $PKG
if $IS_SLACK ; then
	$FAKEROOT $MAKEPKG -l y -c y ${CWD}/$PRGNAM-$VERSION-$ARCH-${BUILD}_${TAG}.${PKGTYPE:-tgz}
else
	tar czvf ${CWD}/$PRGNAM-$VERSION-$ARCH-${BUILD}_${TAG}.${PKGTYPE:-tgz}
fi
cd -

# I may change this later, but I don't care to leave this laying around for now
[[ -d tmp ]] && rm -rf tmp/
[[ -d build ]] && rm -rf build/

