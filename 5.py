def sum ():
    sum_res = 0
    ext = False
    while ext == False:
        numb = input('! - выход ').split()
        res = 0
        for el in range(len(numb)):
            if numb[el] == '!':
                ext = True
                break
            else:
                res = res + int(numb[el])
        sum_res = sum_res + res
        print(f'сумма = {sum_res}')
    print(f'общая сумма = {sum_res}')
sum()
