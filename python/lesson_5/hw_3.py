with open('file_for_hw_3.txt', 'r', encoding='utf-8') as f_obj:
    sum_sal = 0
    i = 0
    for line in f_obj:
        name, salary = line.split()
        sum_sal += float(salary)
        i += 1
        if int(salary) < 20000:
            print('Оклад менее 20 тыс: ', name)
    average_salary = sum_sal / i
    print('Средняя зарплата: ', average_salary, 'руб')
