# Python program to get the top 3 items in a shop

shop_data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

print("Shop Data:", shop_data)
print()

# ============ METHOD 1: Using sorted() with lambda (SIMPLE) ============
print("METHOD 1 - Using sorted() with lambda:")
sorted_items = sorted(shop_data.items(), key=lambda x: x[1], reverse=True)
print("Top 3 items:")
for item, price in sorted_items[:3]:
    print(f"{item} {price}")
print()

# ============ METHOD 2: Using sorted() and operator.itemgetter ============
print("METHOD 2 - Using operator.itemgetter:")
from operator import itemgetter
sorted_items = sorted(shop_data.items(), key=itemgetter(1), reverse=True)
print("Top 3 items:")
for item, price in sorted_items[:3]:
    print(f"{item} {price}")
print()

# ============ METHOD 3: Using heapq.nlargest() (FASTEST) ============
print("METHOD 3 - Using heapq.nlargest():")
import heapq
top_3 = heapq.nlargest(3, shop_data.items(), key=lambda x: x[1])
print("Top 3 items:")
for item, price in top_3:
    print(f"{item} {price}")
print()

# ============ METHOD 4: Using dict comprehension with sorted ============
print("METHOD 4 - Creating top 3 dictionary:")
top_3_dict = dict(sorted(shop_data.items(), key=lambda x: x[1], reverse=True)[:3])
print("Top 3 items:")
for item, price in top_3_dict.items():
    print(f"{item} {price}")
print()

# ============ METHOD 5: Using max() in a loop (for small N) ============
print("METHOD 5 - Using max() in a loop:")
remaining = shop_data.copy()
print("Top 3 items:")
for i in range(3):
    max_item = max(remaining.items(), key=lambda x: x[1])
    print(f"{max_item[0]} {max_item[1]}")
    del remaining[max_item[0]]
print()

# ============ METHOD 6: Using Counter from collections ============
print("METHOD 6 - Using Counter.most_common():")
from collections import Counter
counter = Counter(shop_data)
print("Top 3 items:")
for item, price in counter.most_common(3):
    print(f"{item} {price}")
print()

# ============ METHOD 7: Custom function ============
print("METHOD 7 - Custom function:")
def get_top_n_items(shop_dict, n=3):
    """Get top N items sorted by price"""
    sorted_items = sorted(shop_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:n]

top_3 = get_top_n_items(shop_data, 3)
print("Top 3 items:")
for item, price in top_3:
    print(f"{item} {price}")
print()

# ============ BONUS: Top 3 with additional info ============
print("="*50)
print("BONUS - Top 3 with additional formatting:")
print("="*50)
print()

sorted_items = sorted(shop_data.items(), key=lambda x: x[1], reverse=True)
print(f"{'Rank':<6} {'Item':<10} {'Price':<10}")
print("-" * 26)
for rank, (item, price) in enumerate(sorted_items[:3], 1):
    print(f"{rank:<6} {item:<10} ${price:<9.2f}")
print()

# ============ Different N values ============
print("="*50)
print("Getting different number of top items:")
print("="*50)
print()

for n in [1, 2, 3, 5]:
    print(f"Top {n} items:")
    top_n = sorted(shop_data.items(), key=lambda x: x[1], reverse=True)[:n]
    for item, price in top_n:
        print(f"  {item} {price}")
    print()
