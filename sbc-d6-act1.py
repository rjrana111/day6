#for loops

#n = 0 
#while n < 5:
 #   print(n)
#    n += 1

#=======================================
#li = [0, 1, 2, 3, 4,]
#for i in li:
 #   print(i)

#=======================================
#_list = ["a", "b", "c", "d" ]
#for obj in _list:
#    print(obj)

#=======================================
#for i in range(10, -1, -1):
#    print(i)



#row = int(input("Row: "))
#for x in range(row):
#   print("*" * x)


#for x in range(1, 6):
#    print("*" * x)


#while Loops

#n = 0 
#while n < 10:
#    n = int(input("nganong baho kag baba"))
#else:
#    print("baho gihapon kag baba")
# Get the number of rows and columns from the user



rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
   
    if i == 0 or i == rows - 1:
        print("^" * columns)
    else:
        
        print("^" + " " * (columns - 2) + "^")









