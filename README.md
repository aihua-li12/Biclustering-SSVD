# STA663-final-project-AY
Authors: Aihua Li, Yuxuan Chen

Based on the paper **Biclustering via Sparse Singular Value Decomposition** written by **Mihee Lee**, **Haipeng Shen**, **Jianhua Z. Huang**, and **J.S. Marron** from University of North Carolina at Chapel Hill [1], this project tries to investigate, develope, and realize biclustering by utilizing Sparse Singular Value Decomposition (SSVD).

SSVD is a tool for biclustering by seeking the low-rank matrix approximation with sparsed left and right sigular vectors of original matrix. This project realizes the SSVD algorithm and optimizes the process. 

Simulations, application on the tumor data set [2], and comparative analysis between SSVD, SVD, and SPCA are included in the report. Results are accessible in the corresponding Jupyter notebooks. 


You can install the package by using 
```
pip install SSVDpkg_663proj21
```
in the terminal. After the installation, in Python, import the functions by
```
import SSVDpkg_663proj21
from SSVDpkg_663proj21 import functions
```

The key functions in the `functions` module are:

- `SSVD_layer(X, lam_grid, gamma1, gamma2, max_iter=5000, tol=1e-6)`: Get the sparse SVD layer given the data matrix X at a SVD layer and the tuning parameters grid. Accessible by `functions.SSVD()`. 

- `SSVD(X, num_layer, lam_grid, gamma1, gamma2, max_iter=5000, tol=1e-6)`: Get the SSVD given the data matrix X and the desired number of SSVD layers. Accessible by `functions.SSVD()`. 

- `clusterheatmap(us, ss, vs, label)`: Plot the clustered heatmap. Accessible by `functions.clusterheatmap()`. 

Also, the optimization procedures are recorded in different modules in this package. See the report for detailed discussions on the optimization. 

 
## References

[1] Lee, M., Shen, H., Huang, J., and Marron, J. (2010). Biclustering via sparse singular value decomposition. *Biometrics* **66**, 1087-1095. 
 
[2] UCI machine Learning Repository: Gene EXPRESSION CANCER rna-seq data set. (n.d.). Retrieved April 28, 2021, from http://archive.ics.uci.edu/ml/datasets/gene+expression+cancer+RNA-Seq
