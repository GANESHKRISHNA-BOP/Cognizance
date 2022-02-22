multilist=[["RollNo","Name","Marks"], [1, 'Abc', 90],
     [2, 'Def', 95],
     [3, 'Ghi', 85]]
for i in range(len(multilist)) :
   for j in range(len(multilist[i])) :
      print(multilist[i][j], end="\t")
   print()
