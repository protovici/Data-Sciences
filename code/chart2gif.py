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
print('SETUP IS COMPLETE')

df = yf.download(["TSLA", "TWTR", "FB", "AMZN", "AAPL"], 
                 start="2019-01-01", 
                 end="2021-12-31")


@gif.frame
def helper_plot_2(df, i):
    
    df = df.copy()
    df.iloc[i:] = np.nan
    
    ax = df.plot(title="Selected stocks' change of value")
    ax.set_xlabel("")
    
    # move the legend below the plot
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                     box.width, box.height * 0.9])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1),
              fancybox=True, shadow=True, ncol=5)

fb_df = df[["Adj Close"]].resample("M").last()

frames = []
for i in range(1, len(fb_df)):
    frames.append(helper_plot_2(fb_df, i))

gif.save(frames, "fb_stock_price.gif", 
         duration=15, unit="s", 
         between="startend")

print('Chart_2_Gif IS COMPLETED')