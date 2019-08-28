#!/usr/bin/python

import argparse


def find_max_profit(prices):
    current_min_price_so_far = prices[0]
    max_profit_so_far = -999999

    for i in range(0, len(prices) - 1):
        if i < current_min_price_so_far:
            current_min_price_so_far = i
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit_so_far:
                max_profit_so_far = profit

    return max_profit_so_far


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
