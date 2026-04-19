# Python program to get top 3 items in a shop - NO LAMBDA, NO IMPORT

shop_data = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

print("Shop Data:", shop_data)
print()

# ============ METHOD 1: Using Loop to Find Max (SIMPLE) ============
print("METHOD 1 - Using Loop to Find Max:")
print("Top 3 items:")

remaining = shop_data.copy()
for i in range(3):
    max_item = None
    max_price = -1

    for item, price in remaining.items():
        if price > max_price:
            max_price = price
            max_item = item

    print(f"{max_item} {max_price}")
    del remaining[max_item]
print()

# ============ METHOD 2: Manual Sorting (Bubble Sort) ============
print("METHOD 2 - Manual Bubble Sort:")

items_list = []
for item, price in shop_data.items():
    items_list.append((item, price))

# Bubble sort in descending order
for i in range(len(items_list)):
    for j in range(len(items_list) - 1 - i):
        if items_list[j][1] < items_list[j + 1][1]:
            items_list[j], items_list[j + 1] = items_list[j + 1], items_list[j]

print("Top 3 items:")
for i in range(3):
    print(f"{items_list[i][0]} {items_list[i][1]}")
print()

# ============ METHOD 3: Store in List and Sort Manually ============
print("METHOD 3 - Convert to List and Sort:")

items_list = []
for item, price in shop_data.items():
    items_list.append((item, price))

# Sort by price (second element) - bubble sort
n = len(items_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if items_list[j][1] < items_list[j + 1][1]:
            temp = items_list[j]
            items_list[j] = items_list[j + 1]
            items_list[j + 1] = temp

print("Top 3 items:")
count = 0
for item, price in items_list:
    if count < 3:
        print(f"{item} {price}")
        count = count + 1
print()

# ============ METHOD 4: Nested Loop Approach ============
print("METHOD 4 - Nested Loop Approach:")

top_3_items = []
remaining_items = shop_data.copy()

# Find top 3
for rank in range(3):
    max_item = None
    max_price = 0

    for item in remaining_items:
        if remaining_items[item] > max_price:
            max_price = remaining_items[item]
            max_item = item

    top_3_items.append((max_item, max_price))
    del remaining_items[max_item]

print("Top 3 items:")
for item, price in top_3_items:
    print(f"{item} {price}")
print()

# ============ METHOD 5: Using Simple Function ============
print("METHOD 5 - Simple Function:")

def get_top_3(data):
    result = []
    temp = data.copy()

    for i in range(3):
        best_item = None
        best_price = 0

        for item, price in temp.items():
            if price > best_price:
                best_price = price
                best_item = item

        result.append((best_item, best_price))
        del temp[best_item]

    return result

top_items = get_top_3(shop_data)
print("Top 3 items:")
for item, price in top_items:
    print(f"{item} {price}")
