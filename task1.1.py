def sum_of_multiples(_max_num):
    _sum = 0
    for _num in range(0, _max_num):
        if _num % 3 == 0 or _num % 5 == 0:
            _sum += _num
    print(_sum)


sum_of_multiples(1000)
# This code was written by Crown
