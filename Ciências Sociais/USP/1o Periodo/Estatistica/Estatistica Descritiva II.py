import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a = [5,4,7,8,3,4,2,7,9,7,6,18]
pandas_a =  pd.Series(a)

plt.boxplot(a)