# Management System
# 3 clients - Google, Amazon, Apple

clients = {'1': 'Google',
           '2': 'Amazon',
           '3': 'Apple'}

def get_date():
    import datetime
    return datetime.datetime.now()


def log_record(client_id, preferece_id):
    if int(preferece_id) == 1:
        exercise = input('Write your exercise!\n')
        filename = clients.get(str(client_id)) + '_exercise.txt'
        with open(filename, 'a') as f:
            text = '[' + str(get_date()) + ']' + str(exercise)
            f.write(text)
            print('Added your entry')
    else:
        food = input('Write your food!\n')
        filename = clients.get(str(client_id)) + '_food.txt'
        with open(filename, 'a') as f:
            text = '[' + str(get_date()) + ']' + str(food)
            f.write(text)
            print('Added your entry')


def retrive_record(client_id, preferece_id):
    if int(preferece_id) == 1:
        filename = clients.get(str(client_id)) + '_exercise.txt'
        with open(filename) as f:
            retrived_information = f.readlines()
            print(retrived_information)
    else:
        filename = clients.get(str(client_id)) + '_food.txt'
        with open(filename) as f:
            retrived_information = f.readlines()
            print(retrived_information)


option1 = int(input('Do you want to (1)log or (2)retrive?\n'))
if option1 == 1:
    print('Choose your user ID', clients)
    option2 = int(input())
    option3 = int(input('Do yo want to log (1)exercise or (2)diet?\n'))
    log_record(option2, option3)

elif option1 == 2:
    print('Choose your user ID', clients)
    option2 = int(input())
    option3 = int(input('Do you want to retrive (1)exercie or (2)diet?\n'))
    retrive_record(option2, option3)

