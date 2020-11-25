with open('file_for_hw_2.txt', 'r') as f_obj:
    number = 0
    for number, item in enumerate(f_obj, 1):
        word = item.split(' ')
        print(f'In line {number} {len(word)} word')
    print(f'Total lines {number}')
