#!/usr/bin/env python

import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv( sys.argv[1], index_col=0 )

n, p = df.shape

pca = PCA()

fit = pca.fit( df )

plt.figure()
plt.bar( range(p), fit.explained_variance_ratio_ )
print p, len(fit.explained_variance_ratio_)
plt.savefig(sys.argv[2])