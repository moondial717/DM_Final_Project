def concate_transactions()
	import pandas as pd
	transactions = pd.read_csv('transactions.csv')
	train = pd.read_csv('train.csv')

	train['transactions'] = 0
	dictionary = {}
	for i in range(len(transactions)):
		dictionary[transactions['date'][i] + str(transactions['store_nbr'][i])] = transactions['transactions'][i]
	#print(dictionary)

	train['transactions'] = 0
	for i in range(len(train)):
		if train['date'][i] + str(train['store_nbr'][i]) in dictionary.keys():
			train['transactions'][i] = dictionary[train['date'][i] + str(train['store_nbr'][i])]

	#train.to_csv('out.csv')

concate_transactions()