import lists_1 as lst

print (*lst.places, sep="\n")
# lst.places.sort()
print("\n\n")
print(*sorted(lst.places, reverse =True), sep = "\n")
print ("\n\n")
lst.places.reverse()
print (lst.places)