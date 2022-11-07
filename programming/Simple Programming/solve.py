with open('./data.dat', 'r') as f:
    total = 0
    while True:
        line = f.readline()
        if not line:
            break
        total += 1 and (line.count('0') % 3 == 0 or line.count('1') % 2 == 0)

    print(f"Flag: CTFlearn{{{total}}}")
