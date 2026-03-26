x = 5
y = float(20)
print(x, end=" ")
print (y)
print(type(x))
print(type(y))

if x > y:
    print ("x is greter than y")
    
elif y > x:
    print ("y is greater than x")

def var_output():
    global var
    var = 12

var_output()
print (var)