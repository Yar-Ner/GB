content = []
b = True
my_f = open('test.txt', 'w+', encoding="utf-8")
line = input('Введите текст \n')
content.append(line)
while b == True:
    my_f.writelines(line + "\n")
    line = input('Введите текст \n')
    content.append(line)
    if line == "":
        del(content[-1])
        print(content)
        b = False

my_f.close()
