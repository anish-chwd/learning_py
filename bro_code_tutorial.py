var = "the quick brown fox jumps over the lazy dog"
print(var)
for i in var :
    print(i, end= " ")

print(" ")
print(len(var))

new_str = ""
count = 42
for i in var:
    var[count] = i
    count -= 1
print(var)

