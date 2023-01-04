#!/usr/bin/env python3

import time, os, sys

def main():
    start = time.time()

    # Palindrome length
    length = 9

    # Lowest digit: 1
    min = 1
    
    # Highest digit: 500,000,000
    max = 500000000

    # Setup variables
    skip = '\n'
    min -= 1
    max -= 1
    digits = min
    palindromes = {}

    path = os.path.join(sys.path[0], 'pi500m.txt') # 3.1415...
    file = open(path, 'r')
    file.seek(min + 2) # Skips '3.'

    while digits < max:
        s = file.read(length)
        
        if not s:
            break

        try:
            conditions = []
            conditions.append(s[0] != '0')

            if (length % 2) == 0:
                for i in range(int(length / 2)):
                    conditions.append(s[i] == s[(length - 1) - i])
            elif (length % 2) != 0:
                for i in range(int((length - 1) / 2)):
                    conditions.append(s[i] == s[(length - 1) - i])

            if all(conditions):
                palindromes[file.tell() - length - 2] = s

        except IndexError:
            break
        
        position = file.tell()
        file.seek(position - (length - 1))

        digits += 1
        progress = ((digits - min) / max) * 100
        elapsed = time.strftime('%H:%M:%S', time.gmtime(time.time() - start))

        os.system('cls')
        
        print('            Progress: ', f'{progress:.4f} %')
        print('        Elapsed time: ', elapsed)
        print('   Palindromes found: ', palindromes)
        print('Total of palindromes: ', len(palindromes), skip)
        
        print(' Palindrome\'s length: ', length)
        print('         First digit: ', min + 1)
        print('          Last digit: ', max + 1)
        print('      Digits checked: ', digits - min - 1)
        print('       Current digit: ', digits)
        print('      Current string: ', s)
        
    file.close()

if __name__ == '__main__':
    main()