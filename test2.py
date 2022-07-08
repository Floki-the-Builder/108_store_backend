def test3():
    print('------- TEST 3 ---------')

    prices = [123, 3, 23, 6475, 58, 89, 45, 34, 87,
              34, -12, 23, 123, -23, -123, 0, 123, 0, -29, 10]

    solution = prices[0]
    for num in prices:
        if num > solution:
            solution = num

    print('The greatest nunber is: ' + str(solution))
    # find the most expensive product price
    # solution = price[0]
    # if price is grateer than your solution
    #    your solution is equal to price

    # outside loop, prive the result


test3()
