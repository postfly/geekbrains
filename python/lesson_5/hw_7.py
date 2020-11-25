import json
my_dict = {}
n = 0
summa = 0
with open('file_for_hw_7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        firma, forma, revenue, cost = line.split()
        profit = (int(revenue) - int(cost))
        my_dict[firma] = profit
        if profit > 0:
            summa += profit
            n += 1
if n > 0:
    average_profit = summa / n
else:
    average_profit = 0
result = [my_dict, {'average_profit': average_profit}]
print(result)

with open("my_file.json", "w") as write_f:
    json.dump(result, write_f)
