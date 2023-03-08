num = 0
total = 0.0
while True :
    val = input("Please enter a number: ")
    if val == "done" :
        break
    try:
        fval = float(val)
    except:
        print('Invalid input please enter a number')
        continue
    print(fval)
    num = num + 1
    total = total + fval
    
print('Finished')  
print('count =', num, 'total =', total, 'Average =', total/num)
