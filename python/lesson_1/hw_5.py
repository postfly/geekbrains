# выручка
proceeds = int(input('Indicate the company revenue: '))
# издержки
costs = int(input('Indicate the costs of the company: '))

if proceeds > costs:
    # считаем рентабельность
    profitability = (proceeds - costs) / proceeds
    print('The firm works with profit')
    print('Profitability of proceeds: ', profitability)
    # запрашиваем численность
    employees = int(input('Indicate the number of employees: '))
    # считаем прибыль в расчете на одного сотрудника
    profit_employee = (proceeds - costs) / employees
    print('Profit per employee', profit_employee)
else:
    print('The firm is operating at a loss')
