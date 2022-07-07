file = open("bacery.csv", "r")
top_15 = dict()
tea = dict()
coffee = dict()
time_sale = dict()
month_sale = dict()
while True:
    s = file.readline().strip()
    if not s:
        break
    item = s.split(",")[1]
    daytype = s.split(",")[-1]
    daytime = s.split(",")[2]
    if item in top_15:
        top_15[item] += 1
    else:
        top_15[item] = 1

    if item == "Tea":
        if daytype in tea:
            tea[daytype] += 1
        else:
            tea[daytype] = 1

    if item == "Coffee":
        if daytype in coffee:
            coffee[daytype] += 1
        else:
            coffee[daytype] = 1


    if daytime[11:13] in time_sale:
        time_sale[daytime[11:13]]+= 1
    else:
        time_sale[daytime[11:13]] = 1


    if daytime[:7] in month_sale:
        month_sale[daytime[:7]] += 1
    else:
        month_sale[daytime[:7]] = 1

file.close()
print('TOP 15: ', end='')
for key, value in sorted(top_15.items(), key=lambda para: -para[1])[:15]:
    print(key, '-', value)
i = 0
for key, value in month_sale.items():
    i += value

print()
print("Tea", tea)
print("Coffee", coffee)
print("Time of sales", time_sale)
print(" % of sales", month_sale)

for key, value in month_sale.items():
    print(key, '-', round((value/i)*100, 1))

