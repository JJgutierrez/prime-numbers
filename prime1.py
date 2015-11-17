n = (2)
list = [n]
numPosition = input('enter a Nth to find :')
numPosition = int(numPosition)
newPosition = numPosition - 1
limit = input('enter a limit : ')
limit = int(limit)

while n < limit :
    n+=1
    for a in list:
        if n % a == 0:
            break
    else:  
        if n is not list:    
            list.extend([n])
        
print (list)    
print (list[newPosition])