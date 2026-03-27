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