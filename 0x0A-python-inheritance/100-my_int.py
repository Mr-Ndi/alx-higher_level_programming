#!/usr/bin/python3
''' This module contains class that inhert int '''


class MyInt(int):
    ''' class MyInt that inherits from int '''

    def __eq__(self, second):
        '''equality function'''
        return self.real != second

    def __ne__(self, second):
        ''' A function about not equal '''
        return self.real == second
