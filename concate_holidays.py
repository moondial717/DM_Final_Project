import pandas as pd
import numpy as np

# Read data
df_train = pd.read_csv('train.csv')
df_holidays = pd.read_csv('holidays_events.csv')

def concate_holidays(df_train, df_holidays):
    
    # 日期格式轉換
    df_train['date'] = pd.to_datetime(df_train['date']) 
    df_holidays['date'] = pd.to_datetime(df_holidays['date'])

    # 檢查是否有NA值
    df_holidays.isna().sum()

    # encode 
    df_train = pd.get_dummies(df_train, columns=['family'], dummy_na=False, prefix='family')
    df_train = pd.get_dummies(df_train, columns=['type'], dummy_na=False, prefix='Holiday_Type_Is')
    df_train = pd.get_dummies(df_train, columns=['locale'], dummy_na=False, prefix='Holiday_Is_local')
    df_train = pd.get_dummies(df_train, columns=['transferred'], dummy_na=False, prefix='Holiday_Is_transferred')

    # remove duplicates
    df_train[df_train['id'].duplicated(keep='first')]
    df_train[df_train['id'].duplicated(keep=False)]
    
if __name__ == '__main__':
    # Read data
    df_train = pd.read_csv('train.csv')
    df_holidays = pd.read_csv('holidays_events.csv')

    concate_holidays(df_train, df_holidays)