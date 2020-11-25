my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('file_for_hw_4.txt', 'r', encoding='utf-8') as f_obj1, open('file_for_hw_4_a.txt', 'a',
                                                                      encoding='utf-8') as f_obj2:
    for line in f_obj1:
        new_line = line.split(' — ')
        new_line[0] = my_dict.get(new_line[0])
        f_obj2.write(' — '.join(new_line))
