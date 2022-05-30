def build(url,symbol,vs_currency,file):
    with open(file , 'w') as f:
        f.write('import requests')
        f.write("\n")
        f.write('import json')
        f.write('\n')
        f.write('import os')
        f.write('\n')
        f.write('from termcolor import colored, cprint')
        f.write('\n')
        f.write('import time as wait')
        f.write('\n')
        f.write('\n')
        f.write('url = "{url}"'.format(url=url))
        f.write('\n')
        f.write('\n')
        f.write('def get_all_stats(url,symbol,vs_currency):')
        f.write('\n')
        f.write('    stats = []')
        f.write("\n")
        f.write('    response = requests.get(url = url).text')
        f.write('\n')
        f.write('    response = json.loads(response)')
        f.write("\n")
        f.write('    stats.append(response[symbol][vs_currency])')
        f.write('\n')
        f.write("    stats.append(response[symbol][f'{vs_currency}_market_cap'])")
        f.write('\n')
        f.write("    stats.append(response[symbol][f'{vs_currency}_24h_change'])")
        f.write('\n')
        f.write('    return stats')
        f.write('\n')
        f.write('\n')
        f.write('def clearConsole():')
        f.write('\n')
        f.write("    command = 'clear'")
        f.write('\n')
        f.write("    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls")
        f.write('\n')
        f.write("        command = 'cls'")
        f.write('\n')
        f.write('    os.system(command)')
        f.write('\n')
        f.write('\n')
        f.write('def main():')
        f.write('\n')
        f.write('    first_time = True')
        f.write('\n')
        f.write('    while True:')
        f.write('\n')
        f.write("        stats = get_all_stats(url,'{symbol}','{vs_currency}') #url".format(symbol=symbol,vs_currency=vs_currency))
        f.write('\n')
        f.write('        if first_time:')
        f.write('\n')
        f.write("            price_graphic = colored(f'Price : {stats[0]}' , 'cyan')")
        f.write('\n')
        f.write("            mrket_cap_graphic = colored(f'Market Cap : {stats[1]}' , 'cyan')")
        f.write('\n')
        f.write("            hist_price = stats[0]")
        f.write('\n')
        f.write("            hist_mrket_cap = stats[1]")
        f.write('\n')
        f.write('\n')
        f.write("            if stats[2] >= 0:")
        f.write('\n')
        f.write("                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'green')")
        f.write('\n')
        f.write("            else:")
        f.write('\n')
        f.write("                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'red')")
        f.write('\n')
        f.write("            print(colored('most recent stats :' , 'cyan'))")
        f.write('\n')
        f.write("            print(colored('======================' , 'cyan'))")
        f.write('\n')
        f.write("            print(price_graphic)")
        f.write('\n')
        f.write("            print(mrket_cap_graphic)")
        f.write('\n')
        f.write("            print(_24hr_change_graphic)")
        f.write('\n')
        f.write("            print(colored('=======================' , 'cyan'))")
        f.write('\n')
        f.write('\n')
        f.write("            first_time = False")
        f.write('\n')
        f.write("        else:")
        f.write('\n')
        f.write("            if stats[0] >= hist_price:")
        f.write('\n')
        f.write("                price_graphic = colored(f'Price : {stats[0]}' , 'green')")
        f.write('\n')
        f.write("            else:")
        f.write('\n')
        f.write("                price_graphic = colored(f'Price : {stats[0]}' , 'red')")
        f.write('\n')
        f.write('\n')
        f.write("            if stats[1] >= hist_mrket_cap:")
        f.write('\n')
        f.write("                mrket_cap_graphic = colored(f'Market Cap : {stats[1]}' , 'green')")
        f.write('\n')
        f.write("            else:")
        f.write('\n')
        f.write("                mrket_cap_graphic = colored(f'Market Cap : {stats[1]}' , 'red')")
        f.write('\n')
        f.write('\n')
        f.write("            if stats[2] >= 0:")
        f.write('\n')
        f.write("                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'green')")
        f.write('\n')
        f.write("            else:")
        f.write('\n')
        f.write("                _24hr_change_graphic = colored(f'24 hour change : {stats[2]}' , 'red')")
        f.write('\n')
        f.write('\n')
        f.write("            print(colored('most recent stats:' , 'cyan'))")
        f.write('\n')
        f.write("            print(colored('======================' , 'cyan'))")
        f.write('\n')
        f.write("            print(price_graphic)")
        f.write('\n')
        f.write("            print(mrket_cap_graphic)")
        f.write('\n')
        f.write("            print(_24hr_change_graphic)")
        f.write('\n')
        f.write("            print(colored('=======================' , 'cyan'))")
        f.write('\n')
        f.write("            wait.sleep(15)")
        f.write('\n')
        f.write('\n')
        f.write("            hist_price = stats[0]")
        f.write('\n')
        f.write("            hist_mrket_cap = stats[1]")
        f.write('\n')
        f.write("        clearConsole()")
        f.write('\n')
        f.write("main()")

        f.close()

        

