'''
*
**
***
****
*****
'''

for x in range(5):
    str = ''
    for y in range(x+1):
        str += '*'
    print(f'{str}\n')

'''
    *
   **
  ***
 ****
*****
'''
for x in range(5):
    for y in range(5 - x - 1):
        print(' ', end='')
    for z in range(x+1):
        print('*', end='')
    print('\n')

'''
    *
   ***
  *****
 *******
*********
'''
for x in range(5):
    for y in range(5 - x - 1):
        print(' ', end='')
    for z in range(x * 2 + 1):
        print('*', end='')
    print('')