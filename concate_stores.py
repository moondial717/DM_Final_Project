import pandas as pd

def concate_stores():
    stores = pd.read_csv('stores.csv')
    train = pd.read_csv('train.csv')

    # 將stores['store_nbr']的值轉成str，再與stores['x']一一配對zip起來，最後放入dictionary_x
    dictionary_city = dict(zip(stores['store_nbr'].astype(str), stores['city']))
    dictionary_state = dict(zip(stores['store_nbr'].astype(str), stores['state']))
    dictionary_type = dict(zip(stores['store_nbr'].astype(str), stores['type']))
    dictionary_cluster = dict(zip(stores['store_nbr'].astype(str), stores['cluster']))

    # 將train['store_nbr']的值轉成str，再用 apply 使'store_nbr'的每一個值套用 lambda ：
    # dictionary.get 會帶入 y (這裡的y就是'store_nbr'的值)，去 dictionary_x 找 keyvalue。 若有找到，則返回該值；若無，則返回""。
    # 最後 lambda 會將 dictionary.get 的 return 填入 train['x']
    train['city'] = train['store_nbr'].astype(str).apply(lambda x: dictionary_city.get(x, ""))
    train['state'] = train['store_nbr'].astype(str).apply(lambda x: dictionary_state.get(x, ""))
    train['type'] = train['store_nbr'].astype(str).apply(lambda x: dictionary_type.get(x, ""))
    train['cluster'] = train['store_nbr'].astype(str).apply(lambda x: dictionary_cluster.get(x, ""))

    train.to_csv('out_stores.csv', index=False) #不包含index

concate_stores()