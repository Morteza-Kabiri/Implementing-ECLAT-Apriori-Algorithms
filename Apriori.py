import pandas as pd
from apyori import apriori

# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/DataSets/Bike_AdventureWorkDW.csv', header=None)
transactions = []

# Convert the dataset into a list of transactions
for i in range(len(data)):
    transactions.append([str(data.values[i, j]) for j in range(len(data.columns))])

# print(transactions)
# print("*****************************")

# Perform Apriori association rule mining
association_rules = list(apriori(transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2, max_length=2))
# print(association_rules)
# the structure of the RelationRecord object is :
# ordered_statistics=[
#                     OrderedStatistic(
#                         items_base=frozenset({'Fender Set - Mountain'}),
#                         items_add= frozenset({'Mountain-200'}),
#                         confidence=0.3541329011345219,
#                         lift=3.1334739082018546),
#                     OrderedStatistic(
#                         items_base=frozenset({'Mountain-200'}),
#                         items_add= frozenset({'Fender Set - Mountain'}),
#                         confidence=0.2972789115646259,
#                         lift=3.1334739082018546)
#                     ]
#                 ),

# Create a list to store the association rules as dictionaries
rule_list = []

# Populate the list with the association rules, splitting the rule into left and right sides
for rule in association_rules:
    # Access the items_base and items_add from the ordered_statistics
    left_side = rule.ordered_statistics[0].items_base
    right_side = rule.ordered_statistics[0].items_add

    rule_dict = {
        "Left-hand Side": left_side,
        "Right-hand Side": right_side,
        "Support": rule.support,
        "Confidence": rule.ordered_statistics[0].confidence,
        "Lift": rule.ordered_statistics[0].lift
    }
    rule_list.append(rule_dict)

# Create a DataFrame from the list of rules
rule_df = pd.DataFrame(rule_list)

# Print the DataFrame in a table format
print(rule_df)
