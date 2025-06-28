from pytrends.request import TrendReq
import pandas as pd

import warnings

# To ignore all warnings
warnings.filterwarnings("ignore")

pytrends = TrendReq(hl='es-CO', tz=360)

# Pick keywords you expect are trending
keywords = ['colombia', 'fútbol', 'elecciones']
pytrends.build_payload(keywords, geo='CO', timeframe='now 1-d')

df = pytrends.interest_over_time()
print(df.head())