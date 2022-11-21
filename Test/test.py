import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd
from parameters import df_fin

# Dashboarding
import param
import panel as pn
import random
from datetime import datetime, timedelta
import io

pn.extension('plotly')

df = df_fin.copy()