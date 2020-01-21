def calc_total(num1, num2, num3, subtract_num):
    # Line breaks after binary operators hurt code readability
    # See: https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator
    total = (num1 +
             num2 +
             num3 -
             subtract_num)
    return total