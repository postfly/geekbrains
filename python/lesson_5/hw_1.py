with open('text.txt', 'a') as f_obj:
    while True:
        line = input('Some text. Press enter to finish: ')
        if line:
            f_obj.write(f"{line}\n")
        else:
            break

print(f_obj.closed)
