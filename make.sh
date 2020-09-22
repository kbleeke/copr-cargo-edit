#!/bin/bash
copr buildscm pluth/ruststuff --nowait --clone-url https://github.com/pluth/copr-cargo-edit --method make_srpm --subdir ./$1  --spec ./rust-$1.spec