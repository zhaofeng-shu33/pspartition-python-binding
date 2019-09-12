# CI
## Overview
This project relies on `liblemon` to be build. 
Notice that `liblemon` should be patched if you install the stable version (1.3.1). Installation of the latest development version of `lemon` does not have the problem.
See [#625](https://lemon.cs.elte.hu/trac/lemon/ticket/625) for detail.

## Procedure common to all platforms
use `python setup.py bdist_wheel` to build the wheel

## Procedure specific
### Windows
We use `vcpkg` to fix the `liblemon` dependency. You should install `liblemon:x64-windows` before packaging. Set environment variable `VCPKG_ROOT` to your `vcpkg` installation directory.

### Mac

We use `homebrew` personal tap to package `liblemon`. You can add a tap pointing to [zhaofeng-shu33/liblemonformula](https://github.com/zhaofeng-shu33/homebrew-liblemonformula).

### Manylinux
The manylinux wheel is built by specific docker image. See the repository [lemon-docker](https://gitee.com/freewind201301/lemon-docker.git) for detail.

## Installation Test
We install the package on systems from fresh virtual machine.
See [install test](https://github.com/zhaofeng-shu33/info_cluster_install_test)

