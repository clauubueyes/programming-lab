
def fibonacci(number):
    if number == 0:
        return []
    if number == 1:
        return [0]
    
    secuence= [0,1]
    
    for i in range(number -2 ): 
       
        next = secuence[-1] + secuence[-2]
        secuence.append(next)
    return secuence

print(fibonacci(number=4))  