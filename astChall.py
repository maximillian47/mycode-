displayAst = "* * * * *"
x=0 
for i in range(0, displayAst.length, 2) 
    x = x+2
    print(displayAst[0:x])

for i in range(0, displayAst.length, 2):
    x = x-2
    print(displayAst[0:x])
