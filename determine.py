# Determining training data
import glob
import pandas as pd
import os

# consts
target_col = 'Close'
master_file = 'data/sam.csv'
out_file = 'data/train.csv'
assoc_user_cols = ['Date', 'Open', 'High', 'Low']
drop_cols = ['Adj Close']

master_df = pd.read_csv(master_file)
master_df = master_df.dropna()
master_df = master_df.set_index('Date')
master_df = master_df.sort_index()

master_df = master_df.drop(columns=drop_cols)
eligible_df = pd.read_csv('data/eligible.csv')
print (eligible_df['eligible'])

for f in glob.glob("data/assoc/*.csv"):
    key = os.path.basename(f).replace('.csv', '')
    if key not in list(eligible_df['eligible']):
        print('file not appended : '+ f)
        continue
    temp = pd.read_csv(f, usecols=assoc_user_cols)
    temp = temp.dropna()
    temp = temp.set_index('Date')
    temp = temp.sort_index()
    temp.columns = [(str(col) + '_' + key) for col in temp.columns]
    master_df = master_df.join(temp)

master_df.to_csv(out_file)

