my_list = '4 8 99 71 26 47'
with open('file_for_hw_5.txt', 'a+', encoding='utf-8') as f_obj:
    f_obj.write(my_list)
    print("Мы находимся на позиции: ", f_obj.tell())
    f_obj.seek(0)
    content = f_obj.readline().split()
    print(sum([int(item) for item in content]))
