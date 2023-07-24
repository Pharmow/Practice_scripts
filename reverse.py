nbr = int(input("Please enter a number: "))
pali = nbr
rev = 0
while (nbr>0):
    dig = nbr % 10
    rev = rev * 10 + dig
    nbr = nbr // 10
print (rev)
