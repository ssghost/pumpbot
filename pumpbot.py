from bittrex.bittrex import Bittrex
import time
import sys

def main():
    with open('./BittrexAPI.txt') as apifile:
        lines = apifile.readlines()
        my_api_key = lines[2]
        my_api_secret = lines[4]

    try:
        my_bittrex = Bittrex(my_api_key, my_api_secret, api_version='v1.1')
        print('API Logged In.')
    except:
        print('Login Error.')
    
    try:
        quantity = float(input('Set quantity as:'))
        aim = str(input('Set aim coin as:'))
    except:
	aim = None
        print('Input Error.')

    balance = my_bittrex.get_balance('BTC')
    if aim != None
        buy_market = 'BTC-'+aim
        sell_market = aim+'-BTC'
    buy_rate = my_bittrex.get_ticker(buy_market)['result']['Bid']

    if quantity <= balance:
        start = time.time()
        buy_result = my_bittrex.buy_limit(buy_market, quantity, buy_rate)
        buy_uuid = buy_result['result']['uuid'] 
        if buy_result['success'] == True:
            end = time.time()
            print('Buying Has Done. Time: %s' % str(end-start))
        else:
            print('Buying Timeout.')
            my_bittrex.cancel(buy_uuid)
            sys.exit()

        sell_trig = str(input('Start Selling? (Y/N)'))
        if sell_trig != 'N':
            start = time.time()
            base_remain = my_bittrex.get_balance('BTC')
            aim_all = my_bittrex.get_balance(aim)
            sell_rate = my_bittrex.get_ticker(sell_market)['result']['Bid'] 
            if base_remain == balance-quantity:
                sell_result = my_bittrex.sell_limit(sell_market, aim_all, sell_rate)
                if sell_result['success'] == True:
                    end = time.time()
                    print('Selling Has Done. Time: %s' % str(end-start))
                else:
                    print('Selling timeout.')
                    sys.exit()
            else:
                print('Buying delayed. Canceling Order.')
                my_bittrex.cancel(buy_uuid)
                sys.exit()
    else:
        print('Not Enough Funds.')
        sys.exit() 



if __name__ == '__main__':
	main()
