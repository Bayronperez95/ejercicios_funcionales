#Elabore un programa que, si una lista está vacía, la debe llenar con la serie Fibonacci hasta 50.

def fibonacci(longitud):
    fibo=[1,1]
    for i in range(2,longitud):
        val= fibo[i-2] +fibo[i-1]
        fibo.append(val)
    return fibo

x=[]
if len(x)==0:
    x = fibonacci(50)
else:
    print("lista no vacia")
print(x)