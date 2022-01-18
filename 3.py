with open('3.txt', 'r', encoding='utf-8') as f:
    b = split(str(f.read()))
    c=[]
    for i in b:
        if(int(i).isdigit()):
            c.append(int(i))
    print(c)
