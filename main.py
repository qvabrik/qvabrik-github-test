import number
import db


def Hello(name):
    print('Hello, ' + name)


r = number.Number()
db = db.Database()

print('App has been loaded...')
userName = input('Type your name: ')
Hello(userName)

someNumb = r.numberInput()
newNumb = r.randNumber(someNumb)
print('Number ' + str(someNumb) + ' has became ' + str(newNumb) + '.')

db.DBplus(someNumb, newNumb)
