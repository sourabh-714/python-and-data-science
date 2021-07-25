products = [
    {'p_id':1,'p_name':'apple iphone 10','p_price':67000,'p_cat':'mobile','p_brand':'apple'},
    {'p_id':2,'p_name':'apple macbook pro','p_price':127000,'p_cat':'laptop','p_brand':'apple'},
    {'p_id':3,'p_name':'samsung galaxy s5','p_price':70200,'p_cat':'mobile','p_brand':'samsung'},
    {'p_id':4,'p_name':'asus zenbook','p_price':81000,'p_cat':'laptop','p_brand':'asus'},
    {'p_id':5,'p_name':'asus mobile phone','p_price':27500,'p_cat':'mobile','p_brand':'asus'},
    {'p_id':6,'p_name':'samsung smart tv','p_price':50500,'p_cat':'tv','p_brand':'samsung'}
    ]

to_search = input("Enter your search : ")
to_search = to_search.lower()
#1. Build a search engine, where user can write product name, brand or category
#2. Store the data in a list
#3. Ask user, if he wants to sort the data based on price...
#4. If user enter yes, then ask user to sorting order (asc or desc...)
#5. Print the sorted data....

data = []
# for i in range(len(products)):
#     if products[i]['p_name'] == to_search or products[i]['p_cat'] == to_search or products[i]['p_brand'] == to_search:
#         data.append(products[i])
#         print(products[i])
for i in range(len(products)):
    cond_1 = to_search in products[i]['p_name']
    cond_2 = to_search in products[i]['p_cat']
    cond_3 = to_search in products[i]['p_brand']
    if cond_1 or cond_2 or cond_3:
        data.append(products[i])
        print(products[i])

print("""
1. Sort Data
2. Quit
""")
user_ch = input("Do you want to sort the products ? ")
if user_ch == "1":
    print("""
    1. Sort Low to High
    2. Sort High to Low
    """)
    ch = input("Enter your choice : ")
    if ch == "1":
        sorted_data = sorted(data, key = lambda x : x['p_price'])
        for item in sorted_data:
            print(item)
    elif ch == "2":
        sorted_data = sorted(data, key = lambda x: x['p_price'], reverse=True)
        for item in sorted_data:
            print(item)
    else:
        print("Invalid Choice...")
else:
    pass



