[![Travis](https://api.travis-ci.com/zhaofeng-shu33/pspartition-python-binding.svg?branch=master)](https://travis-ci.com/zhaofeng-shu33/pspartition-python-binding)
[![Appveyor](https://ci.appveyor.com/api/projects/status/github/zhaofeng-shu33/pspartition-python-binding?branch=master&svg=true)](https://ci.appveyor.com/project/zhaofeng-shu33/pspartition-python-binding)

# Python binding
[![PyPI](https://img.shields.io/pypi/v/pspartition.svg)](https://pypi.org/project/pspartition)
## How to build
The binding uses `Cython`. 
To package the library, use `python setup.py bdist_wheel`.
Install the package by `pip install --user pspartition`. 
Below is the pre-built binary packages:

| Platform | py3.6 | py3.7 |
| -------- | :---: | :---: |
| Windows  |   T   |   T   |
| MacOS    |   T   |   T   |
| Linux    |   T   |   T   |

## Demo code
![](./example/example.png)

```Python
import pspartition # classify the three data points shown in the above figure
g = pspartition.PsPartition(3, [(0,1,1),(1,2,1),(0,2,5)]) # index started from zero, similarity is 5 for vertex 0 and 2
g.run() # default to use psp_i algorithm to classify them
print(g.get_critical_values()) # [2,5]
print(g.get_partitions()) # get the result which is [[{0, 1, 2}], [{0, 2}, {1}], [{0}, {1}, {2}]]
```




## ChangeLog

- Version 0.2: expose `PSP` (C++) class, which is high customizable in python.
- Version 0.3: expose `PyGraphPDT` (C++) class, which has similar API as `PyGraph` but different inner implementation.
- Version 0.5: expose `run_psp_i`  for `InfoCluster`.
- Version 0.7: change the python binding name from `info_cluster` to `pspartition`.
