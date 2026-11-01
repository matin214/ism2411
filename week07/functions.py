#Reflection
# The first bug I saw was the missing colon when I saw it in the syntax but when Ir ead the traceback error
#it helped me find the indexerror in the while loop.
#The function takes a baseline price and then a discount tier and it figures out the correct discount percentage based on tier and returns a final discounted price. This is super easy to change the values of rather than doing it manually you only have to do it once
#I did use AI on this assingment for helping me understand the broken code but not to give me the answer.


#Defining a function

def calculate_tax(price, rate):
    return price * rate

#Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: {calculate_tax(350, 0.05):.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
    
#Calling function
original_price = 200

for tier in ["gold","silver","bronze","none"]:
    print(f"{tier}: ${apply_discount(original_price,tier):.2f}")


#Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#Call price
price = 1500

print(f"final_price(200,0.07,'gold) = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'),(150, 'silver'),(80, 'bronze'), (500, 'none')]
rate = 0.07
for price,tier in orders:
    total = final_price(price,rate,tier)
    print(f"Price: ${price} | Tier: {tier} | Total: {total}")


# --- Exercise 5 ---
print("\n--- Running Exercise 5 Fixed Sales Report ---")

# Original source lists
sales = [120, 80, 250, 175, 90]

#Changed 'total = sale' to 'total += sale' so it adds up the values instead of just overwriting the variable with the very last number.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

#Added a missing colon (:) at the end of the 'for sale in sales' line.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

#Changed 'while i <= len(sales)' to 'while i < len(sales)' 
#to prevent an IndexError since index counts stop at len(sales) - 1.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
print("\n--- Running Exercise 6 Scope Experiment ---")
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # What prints: 100
print(double_it()) # What prints: 1998
print(x)           # What prints: 100

# SCOPE EXPLANATORY COMMENT:
# Variable scope means where a variable can be seen and used in the code.
# The variable x outside the function is global and stays 100.
# The variable x inside double_it() is local. It only exists inside that 
# function and disappears when the function finishes, so it never changes the global x.
