# Constant - O(1)
lista = [1, 2, 3, 4, 5]

def constant(n):
    print(n[0])
    print(n[1])

print(constant(lista))

# Linear O(n)
def linear(n):
    for i in n:
        print(i)

print(linear(lista))

# Quadratic - O(n*2) - polynomial
def quadratic(n):
    for i in n:
        for j in n:
            print(i,j)
        print('---')

print(quadratic(lista))

# Combination
def combination(n):
    
    # 0(1)
    print(n[0])

    # 0(5)
    for i in range(5):
        print('test', i)
    
    # 0(n)
    for i in n:
        print(i)
    
    # 0(n)
    for i in n:
        print(i)
    
    # 0(3)
    print("Python")
    print("Python")
    print("Python")

print(combination(lista))

