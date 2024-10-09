def fibonacci(n):
    
    fib_sequence = [0, 1]
    
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > n:  
            break
        fib_sequence.append(next_fib)
    
    return fib_sequence

numero_informado = int(input("Informe um número: "))

sequencia = fibonacci(numero_informado)

if numero_informado in sequencia:
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
