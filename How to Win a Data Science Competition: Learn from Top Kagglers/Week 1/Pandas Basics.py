import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
%matplotlib inline 

from grader import Grader

DATA_FOLDER = '../readonly/final_project_data/'

transactions    = pd.read_csv(os.path.join(DATA_FOLDER, 'sales_train.csv.gz'))
items           = pd.read_csv(os.path.join(DATA_FOLDER, 'items.csv'))
item_categories = pd.read_csv(os.path.join(DATA_FOLDER, 'item_categories.csv'))
shops           = pd.read_csv(os.path.join(DATA_FOLDER, 'shops.csv'))


#Now use your pandas skills to get answers for the following questions. The first question is:

# 1. What was the maximum total revenue among all the shops in September, 2014?


tran_sep_14 = transactions[(transactions.month==9)&(transactions.year==2014)]
tran_sep_14['revenue'] = tran_sep_14.item_price * tran_sep_14.item_cnt_day

max_revenue = tran_sep_14.groupby(['shop_id'])['revenue'].sum().max()
grader.submit_tag('max_revenue', max_revenue)

# 2. What item category generated the highest revenue in summer 2014?


tran_14 = transactions[transactions.year==2014]
tran_summer = tran_14[(tran_14.month==6) | (tran_14.month==7) | (tran_14.month==8)]
category_id_with_max_revenue = tran_summer.revenue.argmax()
grader.submit_tag('category_id_with_max_revenue', category_id_with_max_revenue)

## 3. How many items are there, such that their price stays constant (to the best of our knowledge) during the whole period of time?

num_items_constant_price = sum([1 if item==1 else 0 for item in transactions.groupby(['item_id'])['item_price'].nunique()])
grader.submit_tag('num_items_constant_price', num_items_constant_price)

# 4. What was the variance of the number of sold items per day sequence for the shop with shop_id = 25 in December, 2014? Do not count the items, that were sold but returned back later.

shop_id = 25

total_num_items_sold = transactions[(transactions.month==12) & (transactions.year==2014) & (transactions.shop_id==25)].groupby(['day'])['item_cnt_day'].sum()
days = [day[0] for day in transactions[(transactions.month==12) & (transactions.year==2014) & (transactions.shop_id==25)].groupby(['day'])]

# Plot it
plt.plot(days, total_num_items_sold)
plt.ylabel('Num items')
plt.xlabel('Day')
plt.title("Daily revenue for shop_id = 25")
plt.show()

total_num_items_sold_var = np.var(total_num_items_sold)
grader.submit_tag('total_num_items_sold_var', total_num_items_sold_var)










