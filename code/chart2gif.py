########################################################################
################  Chart2Gif for Presentation Materials  ################
################  Developer: Patrick Vientos            ################
########################################################################

import numpy as np
import pandas as pd
import yfinance as yf

import matplotlib.pyplot as plt
import gif

# settings
plt.style.use("seaborn")
gif.options.matplotlib["dpi"] = 300

df = yf.download("FB", 
                 start="2019-01-01", 
                 end="2021-12-31")

@gif.frame
def helper_plot_1(df, i):
    df = df.copy()
    df.iloc[i:] = np.nan
    ax = df.plot(title="Tesla's stock price", legend=False, style="o--")
    ax.set_xlabel("")
    ax.set_ylabel("Price ($)")