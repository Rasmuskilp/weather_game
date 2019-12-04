# Write a bizz and zzuu game ##project

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu
from game_functions import *
def biz_zzuu_game(number_ent):
    #return print('you have entered'+' '+ str(number))
    #number = int(number)
    #number_ent = int(input('Enter a number:'))
    while number_ent != 'no':
        if 'finish' == number_ent:
            print('you have finished the game!')
            #break
        elif biz_35(number_ent):
            return print('bizzzzuu')
        elif biz_5(number_ent):
            return print('bizz')
        elif biz_5(number_ent):
            return print('zzuu')
        else:
            return print('we have no values!')
# Learn about how to define a function
# remember what is DRY?
# what is separation of concerns?
# Turn this into a functional program
#TDD - test driven development
# use test - see what breaks - change code
#incremental and iterative
#test for true, false, add comments to aid in understanding test
#
# Definition of done for the project:
# This should be it's own project
# it should have a read me
    # it should outline the project
    # it should have simple instructions on how to run the project
# it should have git and git history
# it should be on git hub