#  File: maximum_profit.py

#  Description: Utilizes Dynamic Programming to evaluate what combination of investments has the most value

import sys

# Add Your functions here
def maximizeProfit(money, prices, increase):
    # create 2d array dimensions money x # houses
    arr = [[0 for i in range(money + 1)] for j in range(len(prices) + 1)]
    for i in range(1, len(prices) + 1):
        for j in range(money + 1):
            if prices[i - 1] <= j:  # while any houses can be afforded
                # find max between value in row above and value in row above, column-weight
                arr[i][j] = max(arr[i - 1][j], (increase[i - 1] * prices[i - 1]) + arr[i - 1][j - prices[i - 1]])
            else:
                # copy value in row above
                arr[i][j] = arr[i - 1][j]

    return "%0.2f" % (arr[len(prices)][money])


def main():

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)


    # The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    num_houses = int(line)

    
    # The third line is a list of house prices in million dollar which is a list of \textit{integer numbers} (Consider that house prices can be an integer number in million dollar only).
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i in range(0, len(prices)):
        prices[i] = int(prices[i])
   

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i in range(0, len(increase)):
        increase[i] = float(increase[i])/100

    result = maximizeProfit(money, prices, increase)

    print(result)

    
if __name__ == "__main__":
  main()