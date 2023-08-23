#!/bin/bash

# SPDX-License-Identifier: BSD-3-Clause
# SPDX-FileCopyrightText: Czech Technical University in Prague

# Upload packages to launchpad PPA

set -e

rm ../*.changes
sed -i 's/) unstable/) bionic/' debian/changelog
gbp buildpackage -S --git-ignore-new
git checkout .

sed -i 's/) unstable/~ppa~f) focal/' debian/changelog
gbp buildpackage -S --git-ignore-new
git checkout .

sed -i 's/) unstable/~ppa~j) jammy/' debian/changelog
gbp buildpackage -S --git-ignore-new
git checkout .

for f in ../http-relay_*_source.changes; do
    dput ppa:peci1/http-relay $f
done