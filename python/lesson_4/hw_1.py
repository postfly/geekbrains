from sys import argv


def zp_func(w, p, b):
    return w * p + b


file_path, rate, pay, bonus = argv
print(zp_func(int(rate), int(pay), int(bonus)))
