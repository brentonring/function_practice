# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a, b, c):
    return max([a, b, c])


print(max_num(1, 2, 3))
print(max_num(349, 102, 987))
print(max_num(21, 22, 23))

# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(list):
    if len(list) == 0:
        return 0

    prod = list[0]

    if len(list) > 1:
        for i in list[1:]:
            prod = prod * i

    return prod


print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([671]))

# Write a Python function called rev_string() to reverse a string.


def rev_string(str):
    return str[::-1]


print(rev_string(''))
print(rev_string('python'))
print(rev_string('north carolina'))

# Write a Python function called num_within() to check whether a number falls in a given range.


def num_within(num, beg, end):
    if num >= beg and num <= end:
        return True
    else:
        return False


print(num_within(3, 1, 5))
print(num_within(10, 11, 20))
print(num_within(100, 99, 101))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1], [1, 1]]


def pascal(n):
    # base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                # first number is 1
                if i == 0:
                    row.append(1)
                # intermediate nunmbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        # print triangle
        for row in triangle:
            print(row)


pascal(2)
pascal(5)
