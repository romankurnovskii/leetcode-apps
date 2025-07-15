def gcdOfStrings(str1, str2):
    # If concatenating in both orders gives the same result, there is a common divisor
    if str1 + str2 != str2 + str1:
        return ""
    # The GCD of the lengths gives the length of the common divisor
    from math import gcd

    length = gcd(len(str1), len(str2))
    return str1[:length]
