import pandas as pd

data1 = pd.DataFrame({'key':['A','B','C','D','E','F','G'],
                'value1':[1,2,3,4,5,6,7]})

data2 = pd.DataFrame({'key':['C','D','E','F','G','H'],
                'value2':[8,9,10,11,12,13]})

print(data1)
print(data2)


merge_innerjoin = pd.merge(data1,data2,on='key',how='inner')

merge_left_join = pd.merge(data1,data2,on='key',how='left')

merge_right_join = pd.merge(data1,data2,on='key',how='right')

merged_left = pd.merge(data1,data2,on='key',how='left',indicator=True)
merge_left_anti_join = merged_left[merged_left['_merge'] == 'left_only']
merge_left_anti_join = merge_left_anti_join.drop('_merge',axis=1)

print(merge_left_anti_join)
