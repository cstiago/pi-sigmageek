#!/usr/bin/env python3

from math import pow, sqrt
import time

def main():
    start = time.time()
    skip = '\n'

    # Insert palindromes found
    palindromes = {}

    for i in palindromes:
        prime = True
        number = int(palindromes[i])

        if ((number + 1) % 6 != 0 and (number - 1) % 6 != 0):
            prime = False
        else:
            s = sqrt(number)

            if (pow(s, 2) == number):
                prime = False
            else:
                f = int(s)
                l = int(pow(f, 2))

                for i in range(f + 1, l):
                    p = i - sqrt((pow(i, 2) - number))
                    q = number // p

                    if (p < 2 or q < 2):
                        break

                    if ((p * q) == number):
                        prime = False
                        break
                    else:
                        prime = True
        
        if prime:
            print(skip, 'First prime palindrome: ', number)
            print('Digit position: ', i, end='')

            number = str(i)
            l = int(number[len(number) - 1])

            ordinal = {
                1: 'st',
                2: 'nd',
                3: 'rd'
            }

            print(ordinal.get(l, 'th'))
            
            break

    elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - start))
    print('Elapsed time: ', elapsed)

if __name__ == '__main__':
    main()