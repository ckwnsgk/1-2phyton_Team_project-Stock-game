import random
import matplotlib.pyplot as plt
import time
import math

Bitcoin = 70000000
Ethereum = 5000000
Ripple = 1500

#Use random functions to change the price of coins
def coin(coins):
    if random.randint(1, 2) == 1:
        coins = coins + coins * random.random() * 0.01
    else:
        coins = coins - coins * random.random() * 0.01
    
    return coins

while True:
    Bitcoin = coin(Bitcoin)
    Ethereum = coin(Ethereum)
    Ripple = coin(Ripple)

    print("Bitcoin = {0:,} 원" .format(round(Bitcoin)))
    print("Ethereum = {0:,} 원" .format(round(Ethereum)))
    print("Ripple = {0:,} 원" .format(round(Ripple)))
    print("")

    time.sleep(1)