import numpy as np
from SSVD.functions import SSVD_layer
from SSVD.functions import SSVD
from SSVD.functions import clusterheatmap
from SSVD.opt import SSVD_layer3c
from SSVD.opt import SSVD3c


lam_grid = np.linspace(0, 1, 11)
gamma1 = gamma2 = 2

Ldata = pd.read_csv('../data/LungCancerData.txt', sep=' ', header = None)

Ldata = np.array(Ldata.T) 


n_iters, us, vs, ss, lambda_us, lambda_vs = SSVD(Ldata, 1, lam_grid, gamma1, gamma2)

level   = np.concatenate((np.ones(20), np.ones(13)*2, np.ones(17)*3, np.ones(6)*4))


clusterheatmap(us,ss,vs,level)
pass








