from game_functions import *
from game_code_7 import *
print('testing whether the biz_5 correctly functions - expect output True')
print(biz_5(5)) == True
print('testing whether the biz_3 correctly functions- expect output True')
print(biz_3(3)) == True
print('testing whether the biz_35 correctly functions- expect output True')
print(biz_35(15)) == True
print('testing whether biz_zzu_game function functions correctly- expect output True')
print(biz_zzuu_game(15) == 'bizzzzuu')
check_list = ['bizzzzuu','we have no values!','bizz','zzuu']
for number in list(range(1,50,1)):
    print('test whether a range of int(numbers) will give out correct input- expect output True')
    if biz_zzuu_game(number) in check_list:
        print(True)
    else:
        print(False)

