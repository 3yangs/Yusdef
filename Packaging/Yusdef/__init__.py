""""""

from datetime import date
from time import time, sleep
import webbrowser as w
from random import choice
import random

__version__ = '0.0.3'
MAXPOOWER = 39.99999999999999
MINPOOWER = -39.99999999999999
PI = 3.141592653589793   # global constant -- only place the value of PI is set
periodic_table_many = 118

def primes_number(start, end):
    for n in range(start, end):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            if (n != 1) and (n != 0):
                print(n, 'is a prime number')
            else:
                print(n, 'is not a prime number or a compositive number')

def use_math(n, q):
    print('The product of these is: ' + str(n * q))
    print('The sum of these is ' + str(n + q))
    if n > q:
        print('The differens of these is ' + str(n - q))
        print(n / q)
        print('The rest of these is ' + str(n % q))
    else:
        print('The differens of these is ' + str(q - n))
        print(q / n)
        print('The rest of these is ' + str(q % n))


def fib(end_n):    # write Fibonacci series up to end_n
    a, b = 0, 1
    while a < end_n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(end_n):  # return Fibonacci series up to end_n
    result = []
    a, b = 0, 1
    while a < end_n:
        result.append(a)    # see below
        a, b = b, a+b
    return result
def fab(end_n):
    a, b = 0, 1
    while a < end_n:
        print(a)
        a, b = b, a+b
    print()

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    kind1 = "-- I'm sorry, we're all out of " + kind
    kind2 = "-- Here you are your " + kind
    both = [kind1, kind2]
    ct = random.choice(both)
    print(ct)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

def poower(d, a):
    if (d < 40 and a < 40) and (d > -40 and a > -40):
        print(d ** a)
        print(a ** d)
    elif d <= MINPOOWER or a <= MINPOOWER:
        print('It\'s to small.')
    else:
        print('It\'s to big.')
def secretry(password):
    print('your new password is: ' + ''.join(reversed(password)))
    answer = input('(yes or no)Even better? Write it here: ')
    if answer == 'yes':
        pass

def sec_on_days(days):
    hours = days * 24
    minuts = hours * 60
    seconds = minuts * 60
    if days != 1:
        print('They are ' + str(seconds) + ' seconds on ' + str(days) + ' days.')
    else:
        print('They are 86400 seconds on one day.')

def min_on_days(days):
    hours = days * 24
    minuts = hours * 60
    if days != 1:
        print('They are ' + str(minuts) + ' minuts on ' + str(days) + ' days.')
    else:
        print('They are 1440 minuts on one day.')

def sec_on_weeks(weeks):
    days = weeks * 7
    hours = days * 24
    minuts = hours * 60
    seconds = minuts * 60

    print('They are ' + str(seconds) + ' seconds on ' + str(weeks) + ' weeks.')

def min_on_weeks(weeks):
    days = weeks * 7
    hours = days * 24
    minuts = hours * 60
    print('They are ' + str(minuts) + ' minuts on ' + str(weeks) + ' weeks.')

def wekday(year, month, day):
    if date(year, month, day).weekday() == 0:
        print('Monday')
    elif date(year, month, day).weekday() == 1:
        print('Tuesday')
    elif date(year, month, day).weekday() == 2:
        print('Wednesday')
    elif date(year, month, day).weekday() == 3:
        print('Thurday')
    elif date(year, month, day).weekday() == 4:
        print('Friday')
    elif date(year, month, day).weekday() == 5:
        print('Saturday')
    else:
        print('Sunday')

def whilee(while_word):
    while True:
        print(while_word)
        svar = input('More? (yes, no): ')
        if svar == 'no':
            break

def open_webb(webb):
    w.open(webb)

def random_number3(s, x, y, z):
    ord3 = [x, y, z]
    ord4 = choice(ord3)
    print(str(ord4))

def random_not_number3(s, x, y, z):
    wert3 = [x, y, z]
    wert4 = choice(wert3)
    print(wert4)

def circleArea(radius):
    print('PI = ' + str(PI))
    return PI*radius*radius    # use value of global constant PI

def circleCircumference(radius):
    print('PI = ' + str(PI))
    return 2*PI*radius

def GlobeVolume(radius):
    print('PI = ' + str(PI))
    return 4/3*PI*radius**3

def ConeVolume(Base_radius, height):
    print('PI = ' + str(PI))
    return 1/3*PI*Base_radius**2*height

class Card:
    def __init__(self, color, value):
        self._color = color
        self._value = value

    def get_color(self):
        return self._color

    def get_value(self):
        return self._value

    ftab = '\N{BLACK CLUB SUIT}\N{WHITE DIAMOND SUIT}'\
               '\N{WHITE HEART SUIT}\N{BLACK SPADE SUIT}'

    vtab = ('E', '2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'Kn', 'D', 'K')

    def __str__(self):
        return Card.ftab[self._color-1] + ' ' +\
               Card.vtab[self._value-1]

class Cardgame:
    def __init__(self):
        self._game = []
        for i in range(1, 5):
            for j in range(1, 14):
                self._game.append(Card(i, j))
        random.shuffle(self._game)

    def give(self):
        if len(self._game) > 0:
            return self._game.pop()
        else:
            return None
