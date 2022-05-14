def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname" : "Ruiz", "lastname":"conacento"}

    super_list = [
        {"firstname" : "Ruiz", "lastname":"conacento"},
        {"firstname" : "Ruiz", "lastname":"sinacento"},
        {"firstname" : "Ruiz", "lastname":"ARM"},
    ]
    super_dict = { 
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,0,1,2],
        "floating_nums" : [1.5,7.58,9.90,8.78,3.14159]
    }

    for key, value in super_dict.items():
        print(key,"-",value)

if __name__ =="__main__":
    run()