def read():
    number = []
    with open("./numbers.txt" ,"r",encoding="utf-8") as f:
        for i in f:
            number.append(int(i))
    print(number)
    print("Terminé el código")


def write():
    names = ["Miguel","Valeria","Gata","Maria"]
    with open("./names.txt","a",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()

if __name__ == "__main__":
    run()