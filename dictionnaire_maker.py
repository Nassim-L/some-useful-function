user_list = {'sim':'shelby',}
polling = True
p = "done you key has been added  to user_list"
while polling:
    key = input('put yout key:  ')
    value = input('put yout value: ')
    if key == 'quit' or value == 'quit':
        print("2")
        polling = False
        print(user_list)
        break






    for k in list(user_list):
        if key == k:
            print("3")
            A = input('''this key name is already taken u want use another name '
                      Yes / no :   ''')
            if A == 'no':
                polling = False
            elif A == 'yes':
                print("4")
                key = input('put yout key:  ')
                user_list[key] = value
                print(p)
        if key != k:
            print("5")
            user_list[key] = value
            print(p)




print(user_list)


























