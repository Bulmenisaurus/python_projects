import random
import matplotlib.pyplot as plt
from math import floor

########################################
########################################
# Bot functions
# these kinda just log the transactions and dont do much ._.


def sell_shares(share_num, sell_share_price):
    print(f"Sold {share_num} shares for ${round(sell_share_price * share_num, 2)}. Each share is ${sell_share_price}")
    pass


def buy_shares(available_money, share_cost, share_num):
    if share_cost * share_num <= available_money:
        print(f"Bought {share_num} shares for ${round(share_cost * share_num, 2)}. Each share is ${share_cost} each.")
        pass
    else:
        print('Not enough money to purchase stocks')

########################################
########################################
# bot script


def stock_bot(money, stock_list, shares, buy_lockdown):
    percent = stock_list[0]/stock_list[1] * 100  # percent = 200 ⬆, 150 ➚, 100 ➡︎, 50 ⬊, 0 ⬇
    money_calculated = money
    prev_percent = stock_list[1]/stock_list[2]*100
    if percent >= 100 and prev_percent > 100 and not buy_lockdown:
        # growing (hopefully)
        share_buy_percent = (percent-100)/3  # how many % of available stocks it should buy
        if share_buy_percent > 1:
            share_buy_percent = 1
        shares_to_buy = floor((money//stock_list[0]) * share_buy_percent)  # does the thign from line 37
        if shares_to_buy > 1:
            buy_shares(money, stock_list[0], shares_to_buy)
            money_calculated -= stock_list[0] * shares_to_buy  # just subtracts the money lost from buying
            shares += shares_to_buy
            print(f"Our money balance is ${round(money_calculated, 3)}, and we have {shares} shares.\n")
    elif percent <= 99.5 and shares > 1 and prev_percent < 100:
        # falling
        sell_shares(shares, stock_list[0])
        money_calculated += stock_list[0] * shares
        shares = 0
        print(f"Our money balance is ${round(money_calculated, 3)} and we have 0 shares.\n")
    return [money_calculated, shares]


#######################################
#######################################
# Stocks script

all_money = start_money = float(input("How much money should the bot start with?\n$"))
stock_market = [float(input("How much should each share cost by default?\n$"))]
iterations = int(input("How many iterations should the simulation run for? (100-10,000 is required)\n"))
if iterations < 100:
    iterations = 100
elif iterations > 10_000:
    iterations = 10_000

print("\n\n")

all_shares = 0
bank_account = [all_money, all_money, all_money]
old_price = stock_market[0]
volatility = .02
lock_down = False

for x in range(0, iterations):
    rand_num = (random.random()*2-1)/5
    change_amount = old_price * rand_num
    new_price = old_price + change_amount
    assert new_price != 0
    stock_market.insert(0, new_price)
    old_price = new_price
    if len(stock_market) > 4:  # because stock_bot() needs first 4 items for percent and previous percent
        bot_calcs = stock_bot(all_money, stock_market, all_shares, lock_down)
        all_money = bot_calcs[0]  # because stock_bot() returns a list with [money, shares]
        all_shares = bot_calcs[1]
        bank_account.append(all_money)
    if (all_money + (all_shares * stock_market[0])) < start_money/1.2 and not lock_down and not all_shares:
        if all_shares > 1:
            sell_shares(all_shares, stock_market[0])
            all_money += all_shares * stock_market[0]
        lock_down = True
        print('\nLockdown ENTERED. The bot cannot purchase any more stocks until lockdown is exited.\n')
if all_shares > 1:
    all_money += all_shares * stock_market[0]
    sell_shares(all_shares, stock_market[0])
    bank_account.append(all_money)
    print(f"Our money balance is ${round(all_money, 3)} and we have {all_shares} shares.\n")

#####################################
#####################################
# Graph all data

fig, axs = plt.subplots(2, constrained_layout=True, sharex='all')  # makes the graphs not clip? id rlly know this
fig.suptitle('The results:\n')                          # main title
axs[0].plot(stock_market[::-1], linewidth=1.0)                # plots graph and makes line thinner
axs[0].set_title("Stock market!")
axs[1].plot(bank_account, 'tab:green', linewidth=1.0)   # thin line, and a nice green color!
axs[1].set_title("All the bots money ")
print("\n\n\nFinal results:\n")
if all_money > start_money:
    print(f"Our bot has ${round(all_money, 2)} with ${round(all_money - start_money, 2)} net profit.")
else:
    print(f"Our bot has  ${round(all_money, 2)} with ${abs(round(all_money - start_money, 2))} net loss. :(")
difference = round(abs(stock_market[-1]-stock_market[0]), 2)
print(f"The final price for one share is ${stock_market[0]}, an ${difference} difference.")
plt.show()
