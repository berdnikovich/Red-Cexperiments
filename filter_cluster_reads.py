import pandas as pd
df = pd.read_csv ('mycsv',sep=' ', header=None)
df.columns = ['ids', 'start1', 'start2', 'end1', 'end2']

my_list = []

for i,d in zip(df['start1'] < 4, df['start2'] < 4):
    if i or d:
        my_list.append(i or d)
    else:
        my_list.append(False)

df[my_list].to_csv('filtered_clasters.csv', sep=' ', header = False, index=False)