# STA663-final-project-AY
Authors: Aihua Li, Yuxuan Chen

Based on the paper **Biclustering via Sparse Singular Value Decomposition** written by **Mihee Lee**, **Haipeng Shen**, **Jianhua Z. Huang**, and **J.S. Marron** from University of North Carolina at Chapel Hill, this project tries to investigate, develope, and realize biclustering by utilizing Sparse Singular Value Decomposition (SSVD).

SSVD is a tool for biclustering by seeking the low-rank matrix approximation with sparsed left and right sigular vectors of original matrix. This project realizes the SSVD algorithm and optimizes the process. 

Simulations, application on the tumor data set, and comparative analysis between SSVD, SVD, and SPCA are included in the report. Results are accessible in the corresponding Jupyter notebooks. 


You can install the package by using: `pip install git+https://github.com/YuxuanMonta/STA663-final-project-AY.git@main`

Functions in this package:  `SSVD_layer`, `SSVD`,and `clusterheatmap`

You can load these functions by using:

`from SSVD.functions import SSVD_layer`

`from SSVD.functions import SSVD`

`from SSVD.functions import clusterheatmap`
 
 
## SSVD_layer
 
 Get the sparse SVD layer given the data matrix X at a SVD layer and the tuning parameters grid.
    Input: 
        X: (n, d), can be the original data matrix or the residual matrix
        lam_grid: ndarray, a grid of lambdas to be selected 
        gamma1, gamma2: scalar, tuning parameter
        max_iter: integer, the maximum iteration times
        tol: float, tolerance to stop the iteration
    Return: n_iter, u, v, s, lambda_u, lambda_v
        n_iter: number of iterations
        u: (n, 1), the final u at convergence 
        v: (d, 1), the final v at convergence 
        s: scalar, the singular value at convergence
        lambda_u, lambda_v: the optimal tuning parameter at convergence
        
## SSVD
 
 Get the SSVD given the data matrix X and the desired number of SSVD layers.
    Input: 
        X: (n, d), the original data matrix
        num_layer: desired number of SSVD layers
        lam_grid: ndarray, a grid of lambdas to be selected 
        gamma1, gamma2: scalar, tuning parameter
        max_iter: integer, the maximum iteration times
        tol: float, tolerance to stop the iteration
    Return: n_iters, us, vs, ss, lambda_us, lambda_vs
        n_iters: (num_layer,), number of iterations for each layer
        us: (n, num_layer), the final u at convergence for each layer
        vs: (d, num_layer), the final v at convergence for each layer
        ss: (num_layer,), the singular value at convergence for each layer
        lambda_us, lambda_vs: (num_layer,), the optimal tuning parameter at convergence for each layer
        
        
 
## clusterheatmap

 Plot the clustered heatmap
  Input:
      us,ss,vs: sparse value from after SSVD
      label : Data group
  
  Output:
      a checkerboard heatmap plot
 
## References

Lee, M., Shen, H., Huang, J., and Marron, J. (2010). Biclustering via sparse singular value decomposition. *Biometrics* **66**, 1087-1095. 
 
UCI machine Learning Repository: Gene EXPRESSION CANCER rna-seq data set. (n.d.). Retrieved April 28, 2021, from http://archive.ics.uci.edu/ml/datasets/gene+expression+cancer+RNA-Seq
