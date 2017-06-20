#!/usr/bin/env perl6
use v6;
use Data::Dump;


#   ◎ 基本題 
# v 1. 產生五個亂數，並將其輸出。
# v 2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，
#   每個亂數的值則不用輸出。N=10**1, 10**2, 10**3, 10**4, 10**5。
#   
#   ◎ 進階題
# v 3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。 
#   4. 自己寫一個亂數產生器。



sub MAIN {
	#1. 產生五個亂數，並將其輸出。
	say rand xx 5 ;

	#2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，
	# 	每個亂數的值則不用輸出。N=10**1, 10**2, 10**3, 10**4, 10**5。
	#3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。 
	for < 10 1e2 1e3 1e4 1e5  > -> $N {
		my  $startTime = now.Rat;
		my  @randList = rand xx $N;
		my  $average = ([+] @randList) / @randList.elems;
		my $stdDev = (([+] @randList.map({ ($_ - $average)**2 })) / @randList.elems ).sqrt ;
		say qq:to/END/;
		the average is { $average }
		the stdev is { $stdDev }
		time cost is { $startTime - now.Rat }
		END
	}

}
