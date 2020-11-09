all_item = []
dict_all = {}
i = 1
while True:
    dict_all['Название'] = input('Укажите название товара: ')
    dict_all['Цена'] = float(input('Укажите цену: '))
    dict_all['Количество'] = int(input('Напишите количество: '))
    dict_all['Ед'] = input('Единица измерения: ')
    limit = int(input('Напечатайте "1", для продолжения или "2", чтобы закончить: '))
    if limit == 1:
        pre_item = (i, dict_all.copy())
        i += 1
        all_item.append(pre_item)
    else:
        pre_item = (i, dict_all)
        all_item.append(pre_item)
        break
print(all_item)
print('Первая часть задачи закончена')
product_analytics = {"Название": [], "Цена": [], "Количество": [], "Ед": []}
for number, my_dict in all_item:
    for key, value in my_dict.items():
        product_analytics[key].append(value)
print(product_analytics)
print('Вторая часть задачи закончена')