#Reflection: 
# 1. The most surprising thing about Python is definately how easy the lists are to change especially rather than other languages, I learned a little bit of C# and it was much harder to edit lists in that language.
# 2. In a class I took to learn excel better, we had to look through client emails on an excel sheet to find duplicate entries. If I had a Python script that I wrote with loop methods I could have saved a lot of time and energy.

# --- Exercise 1 ---
print("--- Exercise 1 ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --- Exercise 2 ---
print("\n--- Exercise 2 ---")
print(inventory[0])

print(inventory[-1])

middle_index = len(inventory) // 2
print(inventory[middle_index])

# --- Exercise 3 ---
print("\n--- Exercise 3 ---")

print(inventory[0:3])


print(inventory[-2:])
print(inventory[::2])

# --- Exercise 4 ---
print("\n--- Exercise 4 ---")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)


inventory.sort()
print(inventory)

# --- Exercise 5 ---
print("\n--- Exercise 5 ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught")
    print("Tuples are useful for coordinates because they are immutable, meaning they cannot be changed accidentally after they are created, which keeps data safe.")
    print(coords)

# --- Exercise 6 ---
print("\n--- Exercise 6 ---")
sales = [100, 250, 75, 480, 200]

total_sales = sum(sales)
count_sales = len(sales)
average_sales = total_sales / count_sales

best_day = max(sales)
worst_day = min(sales)

print("Total:", total_sales)
print("Average:", average_sales)
print("Best:", best_day)
print("Worst:", worst_day)

# --- Exercise 7 ---
print("\n--- Exercise 7 ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = price * 0.90
    discounted.append(round(new_price, 2))

print("Original:", prices)
print("Discounted:", discounted)

# --- Exercise 8 ---
print("\n--- Exercise 8 ---")
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales_data:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_avg = sum(high_sales) / high_count

print(high_sales)
print("Count:", high_count)
print("Avg:", round(high_avg, 2))
