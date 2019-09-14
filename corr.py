# Determining training data
import glob
import pandas as pd
import os

# consts
target_col = 'Close'
master_file = 'data/sam.csv'
assoc_user_cols = ['Date', 'Close']
drop_cols = ['Adj Close']
margin = 0.3
prefix = 'Close_'

master_df = pd.read_csv(master_file)
master_df = master_df.dropna()
master_df = master_df.set_index('Date')
master_df = master_df.sort_index()

master_df = master_df.drop(columns=drop_cols)

for f in glob.glob("data/assoc/*.csv"):
    temp = pd.read_csv(f, usecols= assoc_user_cols)
    temp = temp.dropna()
    temp = temp.set_index('Date')
    temp = temp.sort_index()
    temp.columns = [(str(col) + '_' + os.path.basename(f)).replace('.csv', '') for col in temp.columns]
    master_df = master_df.join(temp)


others = [x for x in list(master_df) if prefix in x]

eligible = []
for c in others:
    val = master_df[target_col].corr(master_df[c])
    val = abs(val)
    print(c + ' Corr val : '+ str(val))
    if val >= margin:
        eligible.append(str(c).replace(prefix, ''))

out = pd.DataFrame({'eligible': eligible})
out.to_csv('data/eligible.csv')