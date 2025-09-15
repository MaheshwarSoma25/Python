#Factorial
def fact_while(num):
    fact = 1
    i = 1
    while num >= i:
        fact *= i
        i+=1
    return fact


def fact_for(num):
    fact = 1               
    for i in range(1, num+1):   
        fact *= i
    return fact

print(fact_while(0)) 
print(fact_for(4))  
