#Assert no se usa normalmente, sino que es más común usar try excep raise y finanally

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Introduce un número: ")
    assert num.isnumeric(), "Solo se permiten números"
    print(divisors(int(num)))
    print("Termino mi programa")

if __name__ == "__main__":
    run()