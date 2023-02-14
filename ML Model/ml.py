import math
import cv2
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import matplotlib.pyplot as plt


import cv2

df=pd.read_csv('BHEL__EQ__NSE__NSE__MINUTE.csv')
df.dropna(inplace=True)


df=df.iloc[0:1200,:]

import seaborn as sns
plt.figure(figsize=(8,5))

plt.title('Close Price History')
plt.plot(df['close'])

plt.xlabel('timestamp',fontsize=18)
plt.ylabel('Close Price INR',fontsize=18)
plt.show()