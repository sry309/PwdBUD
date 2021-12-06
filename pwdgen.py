import os
import sys
from colorama import Fore
import src.factor2 as fa2
import src.parseArgs as pa

banner = '''
      ___         ___                         ___           ___           ___     
     /\  \       /\  \         _____         /\__\         /\__\         /\  \    
    /::\  \     _\:\  \       /::\  \       /:/ _/_       /:/ _/_        \:\  \   
   /:/\:\__\   /\ \:\  \     /:/\:\  \     /:/ /\  \     /:/ /\__\        \:\  \  
  /:/ /:/  /  _\:\ \:\  \   /:/  \:\__\   /:/ /::\  \   /:/ /:/ _/_   _____\:\  \ 
 /:/_/:/  /  /\ \:\ \:\__\ /:/__/ \:|__| /:/__\/\:\__\ /:/_/:/ /\__\ /::::::::\__\\
 \:\/:/  /   \:\ \:\/:/  / \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\~~\~~\/__/
  \::/__/     \:\ \::/  /   \:\  /:/  /   \:\  /:/  /   \::/_/:/  /   \:\  \      
   \:\  \      \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\  \     
    \:\__\      \::/  /       \::/  /       \::/  /       \::/  /       \:\__\    
     \/__/       \/__/         \/__/         \/__/         \/__/         \/__/    
'''
print(Fore.RED + banner)


def stdSave():
    f = open(str(pa.parse_args().outfile), "w+")
    sys.stdout = f
    seq1 = fa2.Factor2(pa.parse_args().domain).sequence1()
    seq2 = fa2.Factor2(pa.parse_args().domain).sequence2()
    seq3 = fa2.Factor2(pa.parse_args().domain).sequence3()
    seq = seq1+seq2+seq3
    for i in seq:
        print(i)


if __name__ == '__main__':
    print(Fore.WHITE)
    print('[-] Saving...')
    #通过stdout方式重定向输出，大幅度减少写入时间
    stdSave()

