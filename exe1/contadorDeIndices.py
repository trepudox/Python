string = 'stringfoda string aaaaaa string string string'
x = 0

while x < string.__len__():

    print('{:0>2}-{}'.format(x, string[x]), sep='-')
    x += 1

else:
    print('\nFIM')