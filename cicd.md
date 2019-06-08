# CI
## Overview
This project relies on `liblemon` and `boost-python`. On different platforms, the library has different names, which makes
the CMakeLists.txt of this project quite complex. We use find_python which requires CMake > 3.12. Because it is a recent version of CMake,
many platforms do not install this newer version by default, which further make the build diffcult.
To integrate with python build system, we need to write custom wrapper to invoke
cmake in `setup.py`. This is also a source of complexity.

## Procedure common to all platforms
use `python setup.py` to build the wheel

## Procedure specific
### Windows
We use `vcpkg` to do the job. Because the weired dependency, it is impossible to build for multiple version of python within one
version of vcpkg.
Currently We use appveyor to build for python3.6 since its default vcpkg version is 2018.11 which supports python3.6.
We use local build to package for python3.7 since my vcpkg is up-to-date with upstream.


### Mac
We use `homebrew` personal tap to package dependencies like gtest and liblemon.
Notice that liblemon should be patched.

### Manylinux
Coming soon.


## Installation Test
We install the package on systems without no boost-python.
See [install test](https://github.com/zhaofeng-shu33/info_cluster_install_test)