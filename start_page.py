from termcolor import colored, cprint
import os
import build
from pathlib import Path
import time as wait
import csv
import json

def full_build(symbol,vs_currency):

    url = "https://api.coingecko.com/api/v3/simple/price?ids={_symbol}&vs_currencies={_vs_currency}&include_market_cap=true&include_24hr_vol=false&include_24hr_change=true&include_last_updated_at=true".format(_symbol = symbol, _vs_currency = vs_currency)
    sub_terminal = open(f'sub_terminal_{symbol}','x')

    build.build(url = url,symbol = symbol, vs_currency=vs_currency, file=f'sub_terminal_{symbol}')
    sub_terminal.close()

    wait.sleep(2)
    print(f'symbol: {symbol}')
    os.rename(f'sub_terminal_{symbol}',f'sub_terminal_{symbol}.py')


    print(colored('Terminal Built','cyan'))




def start():
    while True:
        ava_file_obj = open('available.txt','r')
        ava_lst_unprocessed = ava_file_obj.readlines()

        ava_lst = []
        for i in ava_lst_unprocessed:
            ava_lst.append(i.strip())



        ava_file_obj.close()

        welcome_msg1 = colored('Welcome to NMDCrypTerminal','cyan')
        Graphic1 = colored('==========================','cyan')
        input_msg = colored('choose a currency to open : ', 'cyan')

        print(Graphic1)
        print(welcome_msg1)
        print(Graphic1)
        choice = input(f'{input_msg}')

        if choice not in ava_lst:
            if choice == '[EXIT]':
                exit()

            ERROR1 = colored('[ERROR] could not find sub - terminal, build it instead?','red')
            ERROR1_cont = colored('enter a crypto symbol according to coinGecko API : ','red')
            ERROR1_cont2 = colored('enter a vs currency symbol according to coinGecko API : ','red')

            print(ERROR1)
            full_build(input(f'{ERROR1_cont}') , input(f'{ERROR1_cont2}'))

            ava_file = open('available.txt','a')
            ava_file.write('\n')
            ava_file.write(f'{choice}')
            ava_file.close()

            os.system(f'sub_terminal_{choice}.py')
        else:
            os.system(f'sub_terminal_{choice}.py')



start()
