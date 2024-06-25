rows = int(input("ENTER YOUR NUMBER OF ROWS: "))
for i in range(rows, 0, -1):
    if i == 1:
        print("*" + " " * (rows - 2) + "*")
    else:
        print("*" * i)

for i in range(2, rows + 1):
    print("*" * i)
