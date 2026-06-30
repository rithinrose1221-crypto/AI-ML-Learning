import pandas as pd 
from mlxtend.frequent_patterns import apriori, association_rules
import warnings

warnings.filterwarnings("ignore")

data = pd.read_csv("basket_analysis.csv", index_col=0)
data = data.astype(bool)

frequent_item = apriori(data, min_support = 0.1, use_colnames = True )
if frequent_item.empty:
    print("❌ No frequent itemsets found. try lower support.")
    exit()
    
rules = association_rules(frequent_item, metric = "confidence", min_threshold = 0.4)
if rules.empty:
    print("❌ No rules found. Try lowering confidence.")
    exit()
print("\n ✅ Model Ready!")

def recommend(product, rules):
    print(f"\nRecommendations for '{product}':\n")

    filtered_rules = rules[
        rules["antecedents"].apply(lambda x: product in x)
    ]

    if filtered_rules.empty:
        print("❌ No strong recommendations found.")
        return

    filtered_rules = filtered_rules.sort_values(
        by=["confidence", "lift"],
        ascending=False
    )

    for _, row in filtered_rules.iterrows():
        antecedent = list(row["antecedents"])
        consequent = list(row["consequents"])

        print(f"{antecedent} -> {consequent}")
        print(f"Confidence: {row['confidence']:.2f}")
        print(f"Lift: {row['lift']:.2f}\n")
    
    
while True:
    product = input("\n Enter a product name (or type 'exit; to quit):".strip())
    if product.lower() == 'exit':
        print("Exiting...")
        break
    
    if product not in data.columns:
        print(" A Product not found in dataset. Try again.")
        print("Available products:", list(data.columns))
        continue

    recommend(product, rules)