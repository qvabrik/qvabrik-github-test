import random


class Number:
    def randNumber(self, x):
        number = random.randint(x, 100)
        return number

    def numberInput(self):
        while True:
            try:
                someNumber = int(input('Type some number from 0 to 99: '))
                if someNumber < 0:
                    print('Input can\'t be less that 0, try again.')
                    continue
                if someNumber > 99:
                    print('Input can\'t be more that 99, try again.')
                    continue
                break
            except ValueError:
                print('Input must be number, try again.')
                continue
        return someNumber
