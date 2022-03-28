#One item tuple, remember the commma:



thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


vEdades=[2,7,58,7,45,26,10,8,56,57,97,19,11,53,3,99,62,78,29,9,37,42,56,86,28,86,95,26,49,67,21,815,67,10,58,512,24,92,89,67,53,10,9,83,1,44,10,77,98,73,57]
vEdades.remove(10)
vEdades.remove(10)
vEdades.remove(10)
vEdades.remove(10)
for vIndice in vEdades:
    print ("La edad es: ",vIndice)