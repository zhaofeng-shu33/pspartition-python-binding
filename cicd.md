# CI
## Overview
This project relies on `liblemon`. 
To integrate with python build system, we need to write custom wrapper to invoke
cmake in `setup.py`. This is also a source of complexity.

## Procedure common to all platforms
use `python setup.py bdist_wheel` to build the wheel

## Procedure specific
### Windows
We use `vcpkg` to fix the `liblemon` dependency. You should install `liblemon:x64-windows` before packaging. Set environment variable `VCPKG_ROOT` to your `vcpkg` installation directory.

### Mac

We use `homebrew` personal tap to package `liblemon` until official `homebrew-core` integrate this library.
Notice that `liblemon` should be patched.

### Manylinux
The manylinux wheel is built by specific docker image. See the repository [lemon-docker](https://gitee.com/freewind201301/lemon-docker.git) for detail.



## Installation Test
We install the package on systems without no boost-python.
See [install test](https://github.com/zhaofeng-shu33/info_cluster_install_test)

