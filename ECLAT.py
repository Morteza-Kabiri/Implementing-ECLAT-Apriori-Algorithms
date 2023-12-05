import pandas as pd
from pyECLAT import ECLAT

# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/DataSets/Bike_AdventureWorkDW.csv', header=None)

# Convert the dataset into a list of transactions
transactions = []
for i in range(0, len(data)): #i = rows , j = columns
    transactions.append([str(data.values[i, j]) for j in range(0, len(data.values[i]))])

# Convert the list of transactions to a DataFrame
df = pd.DataFrame(transactions)

# Set your ECLAT parameters
min_n_products = 2
min_support = 0.05
max_length = 2

# Create an instance of ECLAT
my_eclat = ECLAT(data=df, verbose=True)

# Fit the algorithm
rule_indices, rule_supports = my_eclat.fit(min_support=min_support, min_combination=min_n_products, max_combination=max_length)

# Create a DataFrame to store the frequent itemsets and their support
itemset_df = pd.DataFrame({"Itemset": rule_indices, "Support": rule_supports})

# Print the DataFrame
print(itemset_df)