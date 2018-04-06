def decimal_to_binary(decimal):
    stack = []
        # while their are still digits left
        # to convert in decimal.
    while decimal > 0:
            # caclute each binary number by dividing decimal 
            # by two. And since we are 'building' our binary
            # string backwards, insert() in the front of the 
            # list instead of append()-ing to the back.
        stack.insert(0, str(decimal % 2))
            # after we've calcute the binary value of the current 
            # decimal, divide the decimal by 2. But make sure we
            # use // instead of / to get a while number!
        decimal = decimal // 2
        # join() together each value in stack, and return
        # the finished binary string. Note: I simply
        # added the '0b' prefix because that is how Python
        # prepends its binary strings. If you don't perfer that,
        # then simply remove the '0b' + part from bellow.
    return '000000' + ''.join(stack)

print(decimal_to_binary(1))