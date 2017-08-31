#!/usr/bin/env python

"""
Usage ./01-timecourse.py <samples.csv> <ctab_dir>

- Plot timecourse of FBtr0331261 for females
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples = pd.read_csv( sys.argv[1] )
soi = df_samples["sex"] == "female"

fpkms = []
for sample in df_samples["sample"][soi]:
    # Build complete file path
    fname = os.path.join( sys.argv[2], sample, "t_data.ctab" )
    # Read current sample
    df = pd.read_csv( fname, sep="\t" )
    # Subset just Sxl rows
    roi = df["t_name"] == transcript
    # Save FPKM value to list    
    fpkms.append( df[roi]["FPKM"].values )

print fpkms

plt.figure()
plt.plot( fpkms )
plt.savefig( "timecourse.png" )
plt.close()














