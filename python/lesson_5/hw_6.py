result = {}
result_fin = {}
with open('file_for_hw_6.txt', 'a+', encoding='utf-8') as f_obj:
    f_obj.seek(0)
    for line in f_obj:
        subject, numbers = line[:-1].split(':')
        subject_sum = sum(int(a) for x in numbers.split() for a in x.split('(') if a.isdigit())
        result = {subject: subject_sum}
        result_fin.update(result)
    print(result_fin)
