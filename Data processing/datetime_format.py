# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:59:03 2024

@author: leehj
"""

# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 파일 읽어와서 df로 변환
df = pd.read_csv('stock-data.csv')

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])   #df에 새로운 열로 추가
print(df.head())
print('\n')

#%%
# dt 속성을 이용하여 new_Date 열의 년월일 정보를 년, 월, 일로 구분
new_Date_dt = df['new_Date'].dt
print(type(new_Date_dt)) # <class 'pandas.core.indexes.accessors.DatetimeProperties'>
print(new_Date_dt.date)  # Series

#%%
df['Year'] = df['new_Date'].dt.year   # Series
df['Month'] = df['new_Date'].dt.month # Series
df['Day'] = df['new_Date'].dt.day     # Series
print(df.head())
print('\n')

#%%
# Timestamp를 Period로 변환하여 년월일 표기 변경하기
df['Date_yr'] = df['new_Date'].dt.to_period(freq='Y')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M') # 년-월
print(df.head())
print('\n')

#%%
# 원하는 열을 새로운 행 인덱스로 지정
df.set_index('Date_m', inplace=True)
print(df.head())