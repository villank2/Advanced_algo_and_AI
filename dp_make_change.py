import math

def dp_make_change(amount, coins):
    assert amount >= 0
    # Initialise memo to be infinity for each of amount + 1 values
    memo = [math.inf] * (amount+1)
    
    if len(coins) == 1:
        memo[amount] = get_min_coins(amount,coins)
        return memo
   # Insert code here
    
    for val in range(0,amount+1):
        if val in coins:
            memo[val] = get_min_coins(val,coins)
        elif memo[val-1] != math.inf and memo[val-2] != math.inf:
            tups = [(i,val-i) for i in range(1,(val//2)+1)]
            li_sums = [memo[x]+memo[y] for x,y in tups]
            min_sum = min(li_sums)
            memo[val] = min_sum    
        else:
            memo[val] = get_min_coins(val,coins)
    print(memo)
    return memo


def get_min_coins(amount,coins):
    
    ind = [0] * len(coins)
    for index,coin in enumerate(coins):
        while amount-coin >= 0:
            amount -= coin
            ind[index] += 1
    return sum(ind) 

print((dp_make_change(200,[200])))
print(dp_make_change(12,[5,2,1]))
print(dp_make_change(800,[200]))