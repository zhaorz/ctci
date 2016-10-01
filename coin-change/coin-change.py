#!/bin/python

import sys

def emptyWallet(coins):
    wallet = {}
    for c in coins:
        wallet[c] = 0
    return wallet

def walletValue(wallet):
    total = 0
    for c in wallet:
        total += c * wallet[c]
    return total

def walletAdd(wallet, c):
    result = wallet.copy()
    if c not in result:
        result[c] = 1
    else:
        result[c] += 1
    return result

def walletToStr(wallet):
    coins = sorted(wallet.keys())
    return ' '.join(map(lambda c: str(c) + ':' + str(wallet[c]), coins))


# Represent wallet using a hash of coin_value -> count
def make_change(coins, n):
    solutions = set()

    def helper(coins, n, change):
        if n < 0:               # Can't make change
            return
        if n == 0:              # Made change, add it to solutions
            solutions.add(walletToStr(change))
        else:                   # Make change with each coin value
            for c in coins:
                helper(coins, n - c, walletAdd(change, c))

    helper(coins, n , emptyWallet(coins))
    return len(solutions)



n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)
