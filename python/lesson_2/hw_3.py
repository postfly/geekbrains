some_list = ('Winter', 'Spring', 'Summer', 'Autumn', 'Winter')
i = int(input('Please enter a number from 1 to 12: '))
print(some_list[i // 3])

some_dict = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer",
             9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}
i = int(input('Please enter a number from 1 to 12: '))
print(some_dict.get(i))
