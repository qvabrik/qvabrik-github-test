import number
import db


def Hello(name):
    print('Hello, ' + name)


r = number.Number()
db = db.Database()

print('App has been loaded...')
userName = input('Type your name: ')
Hello(userName)
while True:
    choise = input('Do you want to do some magic with number? [y]/[n]: ')
    if choise == 'y':
        break
    elif choise == 'n':
        exit()
    else:
        print('No such command as [' + choise + ']. Please try again.')
        continue

command = "y"
while command == "y":
    someNumb = r.numberInput()
    newNumb = r.randNumber(someNumb)
    print('Number ' + str(someNumb) + ' has became ' + str(newNumb) + '.')
    db.DBplus(someNumb, newNumb)
    print('Input-output has been added to database.')
    while True:
        command = input('Try another number? [y]/[n]: ')
        if command == "y" or command == "n":
            break
        else:
            print('Unknown command. Please try again.')
            continue
