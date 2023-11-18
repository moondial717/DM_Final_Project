def miss_date():
	price = 0
	return price

def concate_oil():
    import pandas as pd
    oil = pd.read_csv('dataset/oil.csv')
    train = pd.read_csv('dataset/train.csv')
    #油價有缺值，前後一天取平均
    oil['dcoilwtico'].fillna((oil['dcoilwtico'].shift(1) + oil['dcoilwtico'].shift(-1)) / 2, inplace=True)

    train['oil_price'] = 0
    dictionary_oil = {}
    dictionary_oil['2013-01-01'] = float(93.14);

    # 建立oil dictionary
    for i in range(1, len(oil)):
        date = oil['date'][i]
        price = float(oil['dcoilwtico'][i])
        dictionary_oil[date] = float(price);

    for i in range(0, len(train)):
        print("完成第" + str(i) +"筆");
        if train['date'][i] in dictionary_oil.keys():
            train['oil_price'][i] = dictionary_oil[train['date'][i]]
        else:
            train['oil_price'][i] = 0
    train.to_csv('oilOut1.csv')

concate_oil()