import lists_1 as lst

# print (lst.places)

lst.places.insert(0, "Victoria memorial")

copy_places = []
for i in range(len(lst.places)):
    copy_places.append(lst.places[i])

del lst.places[0]

global mismatch

for place in copy_places:
    if place not in lst.places:
        print(f"{place} got deleted")    

var = copy_places.pop(0)
print (f"var = {var}")

for place in copy_places:
    if place not in lst.places:
        print(f"{place} got deleted") #nothing gets printed as both lists are the same 

