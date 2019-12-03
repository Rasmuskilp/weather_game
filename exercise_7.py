# Write a bizz and zzuu game ##project

# write a program that take a number
# prints back each individual number, but
    # if it is a multiple of 3 it returns bizz
    # if a multiple of 5 it return zzuu
    # if a multiple of 3 and 5 it return bizzzzuu
def biz_zzuu_game():
    #return print('you have entered'+' '+ str(number))
    #number = int(number)
    number_ent = int(input('Enter a number:'))
    if number_ent % 3 == 0:
        return print('bizz')
    elif number_ent % 5 == 0:
        return print('zzuu')
    elif number_ent % 3 and number_ent % 5 == 0:
        return print('bizzzzuu')
    else:
        return print('we have no values!')
# Learn about how to define a function
# remember what is DRY?
# what is separation of concerns?
# Turn this into a functional program

# Definition of done for the project:
# This should be it's own project
# it should have a read me
    # it should outline the project
    # it should have simple instructions on how to run the project
# it should have git and git history
# it should be on git hub