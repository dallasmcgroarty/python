#plotly and cufflinks data visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly import __version__
import plotly.express as px
import cufflinks as cf
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot

# init to access visuals
init_notebook_mode(connected=True)

# go offline 
cf.go_offline()

# DATA
df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
print(df.head())

df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
print(df2)

# plotting
# plotly not working for me meh
