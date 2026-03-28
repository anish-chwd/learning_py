
print(10 > 9)
# print(10 == 9)
print(10 < 9)

var1 = 1000
var2 = 341
var3 = 0

if var1 >= var2:
    print("var1>=var2")
else:
    print("var1<=var2")
    
    
print(bool("hello"))
print(bool(var1))
print(bool(var3))
print(bool(None))
print(bool([]))
print(bool("")); print(bool(" "))


class myclass():
    def __len__(self):
        return 0
    
    
myobj = myclass()
print (bool(myobj))

def myfnx():
    return True


print (myfnx())

print(isinstance(var1, float))