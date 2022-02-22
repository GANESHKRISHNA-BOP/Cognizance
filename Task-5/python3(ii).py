multilist = [ ["RollNo","Name","Marks"],[1, 'Abc', 90],
     [2, 'Def', 95],
     [3, 'Ghi', 85]]
     
print("{:<10} {:<10} {:<10}".format('Roll no','name','marks'))

for i in range(3):
    print(multilist[2][i],end=" "*10)
