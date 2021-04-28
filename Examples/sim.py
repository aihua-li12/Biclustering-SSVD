import numpy as np
from SSVD.functions import SSVD_layer
from SSVD.functions import SSVD
from SSVD.functions import clusterheatmap
from SSVD.opt import SSVD_layer3c
from SSVD.opt import SSVD3c

u_tilde = np.r_[np.arange(3,11)[::-1], 2*np.ones(17), np.zeros(75)].reshape((-1,1))
u = u_tilde/np.linalg.norm(u_tilde)
v_tilde = np.r_[np.array([10,-10,8,-8,5,-5]),3*np.ones(5),-3*np.ones(5),np.zeros(34)].reshape((-1,1))
v = v_tilde/np.linalg.norm(v_tilde)
s = 50

label = np.concatenate((np.ones(8), np.ones(17)*2, np.ones(75)*3))

clusterheatmap(u,s,v,label)
pass


Xstar = s * np.outer(u, v)
n, d = X_star.shape
X_sim = X_star + np.random.randn(n,d)
lam_grid = np.linspace(0, 8, 100)
gamma1 = gamma2 = 2

n_iters, u, v, s, lambda_us, lambda_vs = SSVD3c(X_sim, 1, lam_grid, gamma1, gamma2)

clusterheatmap(u, s, v, label)
pass


