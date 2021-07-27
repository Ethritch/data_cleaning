import pandas as pd

pd.options.display.max_columns = 18

#declares your dataframes and takes data from the csv files
df = pd.read_csv('transactions.csv')
df2 = pd.read_csv('token_transfers.csv')


#merges the two dataframes and gets rid of duplicates.
output = pd.merge(left=df, right=df2, how='left', left_on='hash', right_on='transaction_hash')
output = output.drop_duplicates(keep='first')

#prints the first 20 rows and lets you see the merger and converts the merged data into a csv file
print(output.head(20))
output.to_csv("merger.csv")
















#you may need this later
#new_df = new_df.iloc[0:110, 7:8]

#new_df = pd.to_numeric(new_df["value"])
#new_df = new_df[new_df.value!= '0']