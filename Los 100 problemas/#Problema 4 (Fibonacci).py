#Problema 4 (Fibonacci)

#Hacer la definición (Fn = Fn-1 + Fn-2)

def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo [n]

n = int(input("Ingrese el limite que quiere para la Sucesión de Fibonacci: "))
for i in range (n):
    print (fibonacci_memo(i), end=" ")

#Okay, use chat gpt de nuevo para entender unas cosas... por no decir que lo hizo por mi.
#PEEEERO. En mi defensa, estoy aprendiendo muchas cosas con estos problemas, ya que no solo copio y pego.
#Osea, si copio, pero a mano, y le pregunto de todo a mi querido ChatGPT