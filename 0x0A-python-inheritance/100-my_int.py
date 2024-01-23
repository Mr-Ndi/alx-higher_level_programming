#!/usr/bin/python3
''' This module contains class that inhert int '''


class MyInt(int):
    ''' class MyInt that inherits from int '''

    def __equal__(self, second):
        '''equality function'''
        return self.real != second

    def __notequal__(self, second):
        ''' A function about not equal '''
        return self.real == second
