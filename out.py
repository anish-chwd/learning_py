x = 5
y = float(20)
print(x, end=" ")
print (y)
print(type(x))
print(type(y))

global var

if x > y:
    print ("x is greater than y")
    
elif y > x:
    print ("y is greater than x")

def var_output():
    global var
    var = 12

var_output()
print (var)

special_str = 3 + 5j #j is added as an imaginary part ... complex cannot be converted to other number types

print(special_str)
print (type(special_str))