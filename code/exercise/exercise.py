#/usr/bin/env python3


from random import randint
from collections import namedtuple


def foobar(arg=None):

    return True


class Caculator:

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def divide(a, b):
        return a / b

    def multiply(a, b):
        return a * b


class Robot:

    def __init__(self, name, task):

        Point = namedtuple('Point', 'x y')

        self.name = name
        self.task = task
        self.position = Point(0.0, 0.0)

    def greet(self):

        print('My name is {0}'.format(self.name))

    def move(self, coordinate):

        self.position = coordinate


class Node:

    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class MyList:

    def __init__(self, ):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item, self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next

        return count
