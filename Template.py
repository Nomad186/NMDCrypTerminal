import requests
import json
import os
from termcolor import colored, cprint
import time as wait

url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=gbp&include_market_cap=true&include_24hr_vol=false&include_24hr_change=true&include_last_updated_at=true"

def get_all_stats(url,symbol,vs_currency):
    stats = []

    response = requests.get(url = url).text
    response = json.loads(response)

    stats.append(response[symbol][vs_currency])
    stats.append(response[symbol][f'{vs_currency}_market_cap'])
    stats.append(response[symbol][f'{vs_currency}_24h_change'])

    return stats


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def main():
    first_time = True

    while True:

        
    
        stats = get_all_stats(url,'solana','gbp') #url

        if first_time:
            price_graphic = colored(f'Price : {stats[0]}' , 'cyan')
            mrket_cap_graphic = colored(f'Market Cap : {stats[1]}' , 'cyan')

            hist_price = stats[0]
            hist_mrket_cap = stats[1]


            # copy paste finished code here

            if stats[2] >= 0:
                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'green')
            else:
                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'red')

            
            print(colored('most recent stats :' , 'cyan'))
            print(colored('======================' , 'cyan'))
            print(price_graphic)
            print(mrket_cap_graphic)
            print(_24hr_change_graphic)
            print(colored('=======================' , 'cyan'))
                
    
            first_time = False
        else:
            if stats[0] >= hist_price:
                price_graphic = colored(f'Price : {stats[0]}' , 'green')
            else:
                price_graphic = colored(f'Price : {stats[0]}' , 'red')

            if stats[1] >= hist_mrket_cap:
                mrket_cap_graphic = colored(f'Market Cap : {stats[1]}' , 'green')
            else:
                mrket_cap_graphic = colored(f'Market Cap : {stats[1]}' , 'red')
            
            if stats[2] >= 0:
                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'green')
            else:
                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'red')
            

            # display graphic:

            print(colored('most recent stats' , 'cyan'))
            print(colored('======================' , 'cyan'))
            print(price_graphic)
            print(mrket_cap_graphic)
            print(_24hr_change_graphic)
            print(colored('======================='))


            hist_price = stats[0]
            hist_mrket_cap = stats[1]

        
        wait.sleep(15)
                
 
main()




