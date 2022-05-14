def run():
    list = [i**2 for i in range(1,1001 ) if i % 3 != 0]
    print(list)

if __name__ == "__main__":
    run()
