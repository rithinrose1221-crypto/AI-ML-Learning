import pandas as pd
import warnings

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules

warnings.filterwarnings("ignore")


# ==========================================
# 1. LOAD TRANSACTIONS
# ==========================================

transactions = []

with open("groceries.csv", "r", encoding="utf-8") as file:

    for line in file:

        line = line.strip()

        if line == "":
            continue

        items = [item.strip() for item in line.split(",")]

        transactions.append(items)


print("\nTotal Transactions :", len(transactions))

print("\nFirst 5 Transactions:\n")

for t in transactions[:5]:
    print(t)


# ==========================================
# 2. TRANSACTION ENCODING
# ==========================================

encoder = TransactionEncoder()

encoded = encoder.fit(transactions).transform(transactions)

basket = pd.DataFrame(
    encoded,
    columns=encoder.columns_
)

print("\nNumber of Products :", len(basket.columns))


# ==========================================
# 3. FP-GROWTH
# ==========================================

frequent_items = fpgrowth(
    basket,
    min_support=0.02,
    use_colnames=True
)


if frequent_items.empty:
    print("No frequent itemsets found.")
    exit()


print("\nFrequent Itemsets Found :", len(frequent_items))


# ==========================================
# 4. ASSOCIATION RULES
# ==========================================

rules = association_rules(
    frequent_items,
    metric="confidence",
    min_threshold=0.3
)


if rules.empty:
    print("No association rules found.")
    exit()


print("Association Rules Generated :", len(rules))

print("\nFP-Growth Model Ready!")


# ==========================================
# 5. RECOMMENDATION FUNCTION
# ==========================================

def recommend(product):

    print("\nRecommended Products\n")

    filtered = rules[
        rules["antecedents"].apply(
            lambda x: product in x
        )
    ]

    if filtered.empty:
        print("No recommendations found.")
        return

    filtered = filtered.sort_values(
        by=["confidence", "lift"],
        ascending=False
    )

    shown = set()

    for _, row in filtered.iterrows():

        for item in row["consequents"]:

            if item != product and item not in shown:

                shown.add(item)

                print("---------------------------------------")
                print("Recommended Item :", item)
                print("Support          :", round(row["support"], 3))
                print("Confidence       :", round(row["confidence"], 3))
                print("Lift             :", round(row["lift"], 3))


# ==========================================
# 6. PRODUCT SEARCH
# ==========================================

products = sorted(basket.columns)


while True:

    product = input(
        "\nEnter Grocery Item (or 'exit'): "
    ).strip().lower()


    if product == "exit":

        print("\nThank you!")

        break


    matched = None


    for p in products:

        if p.lower() == product:

            matched = p

            break


    if matched is None:

        print("\nProduct not found.")

        continue


    recommend(matched)