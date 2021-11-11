# Biclustering by Sparse Singular Value Decomposition in Python

Authors: Aihua Li, Yuxuan Chen

Date: June 29, 2021

## Introduction

This is an introduction page for Python package `SSVDpkg_663proj21`.

Sparse singular value decomposition (SSVD) is an algorithm proposed for biclustering [1], realized by low-rank matrix approximation with sparsed left and right sigular vectors of original matrix. Package `SSVDpkg_663proj21` provides functions to realize the SSVD algorithm in Python and optimizes the process. Codes are optimized by `Cython`, a C-extensions in Python. 

A complete document for package `SSVDpkg_663proj21` is accessible on https://github.com/aihua-li12/STA663-final-project-AY, where we have presented the codes optimization procedures. Simulation examples and real data application on a tumor dataset [2] are also included in the document. Besides, comparative analysis between SSVD, SVD, and SPCA are performed. 

For more information, see the [package source page](https://github.com/aihua-li12/Biclustering-SSVD).

## Basic Usage

You can install the package by using 
```
pip install SSVDpkg_663proj21
```
in the terminal. After the installation, in Python, import the `functions` module by
```
import SSVDpkg_663proj21
from SSVDpkg_663proj21 import functions
```

The key functions in the `functions` module are:

- `SSVD_layer(X, lam_grid, gamma1, gamma2, max_iter=5000, tol=1e-6)`: Get the sparse SVD layer given the data matrix X at a SVD layer and the tuning parameters grid.

- `SSVD(X, num_layer, lam_grid, gamma1, gamma2, max_iter=5000, tol=1e-6)`: Get the SSVD given the data matrix X and the desired number of SSVD layers.

- `clusterheatmap(us, ss, vs, label)`: Plot the clustered heatmap.

Also, the optimization procedures are recorded in different modules in this package. See the report for detailed discussions on the optimization. 

 
## References

[1] Lee, M., Shen, H., Huang, J., and Marron, J. (2010). Biclustering via sparse singular value decomposition. *Biometrics* **66**, 1087-1095. 
 
[2] UCI machine Learning Repository: Gene EXPRESSION CANCER rna-seq data set. (n.d.). Retrieved April 28, 2021, from http://archive.ics.uci.edu/ml/datasets/gene+expression+cancer+RNA-Seq
