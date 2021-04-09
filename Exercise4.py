def astrologers_star(number, pattern):
    pattern = bool(pattern)
    print(pattern)
    if pattern:
        for num in range(1, number+1):
            print('*' * num)
    elif not pattern:
        num = number
        while num > 0:
            print('*' * num)
            num -= 1

astrologers_star(10, 0)