# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:32:26 2024

@author: leehj
"""

# -*- coding: utf-8 -*-

# sklern을 이용하여 원핫인코딩 처리(one-hot-encoding)
# 숫자 0과 1 또는 True, False로 데이터를 변환

# sklern 라이브러리 불러오기
# pip install scikit-learn

from sklearn import preprocessing    


# 라이브러리 불러오기
import pandas as pd
import numpy as np


# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환

# np.histogram 으로 3개의 bin으로 나누는 경계 값의 리스트 구하기
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

#%%
# 3개의 bin에 이름 지정
bin_names = ['저출력', '보통출력', '고출력']

# pd.cut 으로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],     # 데이터 배열
                      bins=bin_dividers,      # 경계 값 리스트
                      labels=bin_names,       # bin 이름
                      include_lowest=True)    # 첫 경계값 포함


#%%
# 전처리를 위한 encoder 객체 만들기
label_encoder = preprocessing.LabelEncoder()     # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder()   # one hot encoder 생성

print(label_encoder)
#%%
# label encoder로 문자열 범주를 숫자형 범주로 변환
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))  
# onehot_labeled = label_encoder.fit_transform(df['hp_bin'])  # 전체
print(onehot_labeled)
print(type(onehot_labeled))

#%%
# 2차원 행렬로 형태 변경 : 392 * 1
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1) 
print(onehot_reshaped)
print(type(onehot_reshaped))

# 희소행렬로  : (행, 열)
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))


