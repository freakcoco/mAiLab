#!/usr/bin/env python3
import typing
import random
import functools
import math
import os
import time


#   ◎ 基本題 
# v 1. 產生五個亂數，並將其輸出。
# v 2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，
#   每個亂數的值則不用輸出。N=10**1, 10**2, 10**3, 10**4, 10**5。
#   
#   ◎ 進階題
# v 3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。 
#   4. 自己寫一個亂數產生器。






natural_number = typing.TypeVar('natural_number', int, float)

def random_list(how_many_element: int) -> typing.List[float]:
    return [random.random() % 1 for x in range(how_many_element)]

def average_of_list(input_list: typing.List[natural_number] ) -> natural_number: 
    return sum(input_list) / len(input_list)
   
def standard_deviation(input_list: typing.List[natural_number] ) -> natural_number:
    get_average = average_of_list(input_list)
    return math.sqrt(sum(map(lambda x : (x - get_average) ** 2 , input_list ) ) / len(input_list) )


    


def main():
    pline = lambda:print('-'*os.get_terminal_size().columns)
    # 1. 產生五個亂數，並將其輸出。
    print([random.random() for x in range(5)])
    
    # 2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，
    #    每個亂數的值則不用輸出。N=10**1, 10**2, 10**3, 10**4, 10**5。
    # 3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。 
    for N in [ 10, 10**2, 10**3, 10**4, 10**5 ] :
        start_time = time.time()
        get_random_List = random_list(N)
        pline()
        print("the average is ({}) ".format(average_of_list(get_random_List ) ) )
        print("the stdev is ({}) ".format(standard_deviation(get_random_List ) ) )
        print("time cost ({:7f}) ".format(time.time() - start_time ) )
    
if __name__ == '__main__':
    main()
