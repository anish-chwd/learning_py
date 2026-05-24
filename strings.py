a = "Hello, World"
print(a[2])

for x in "banana":
    print (x)
    
print(len(a))

print ("world" not in a)

global txt
txt = "the quick brown fox jumps over the lazy dog"

if "quick" not in txt:
    print("yes, 'quick' is present")
    
#slicing

print (txt[5:10])
print (txt[:20])
print(txt[10:])
print (txt[-15:-5])

print (a.upper())
print (a.lower())
print (a.strip())
print (a.replace("H","J"))
print (a.split(","))

ant = "antonio"
cont = "and"
bast = "bastanio"
final = ant +" "+ cont +" "+bast
print (final)

age = 54
msg = f"age is : {age}"
print (msg)
msg2 = f"type double is : {age:.2f}"
print (msg2)
print(f"the product of 23 and 56 is {23 * 56}")

print(txt.title())
print(txt.capitalize())

print (txt.rstrip())
print(txt.lstrip())
print(txt.strip())
print (txt.strip("g"))