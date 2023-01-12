# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.python3_formatted_output

# 기본 출력

print('Python Start!')
print()

# separator 옵션

print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1124', sep='-')

# end 옵션

print('Welcome to', end=' ')
print('IT News', end='')

# file 옵션

import sys

print('Learn Python', file=sys.stdout)
print()

#format 사용 (d:3, s: 'python', f: 3.1432)
print('%s %s' % ('one', 'two'))
print('{} {}' .format('one', 'two'))
print('{1} {0}' .format('one', 'two'))

# %s
print('%10s' % ('Nice'))
print('{:>10}' .format('Nice'))
print('%-10s' % ('Nice'))
print('{:10}' .format('Nice'))

print('{:#>10}' .format('Nice'))
print('{:^10}' .format('Nice'))

print('%.5s' % ('Niceandworm'))
print('{:10.5}' .format('Iamszkam'))


# %d
print('%d %d' % (1,2))
print('{} {}' .format(1,2))


print('%4d' % (42))
print('{:4d}' .format(42))

# %f

print('%1.8f' % (3.141414135213))
print('{:f}' .format(3.135135315))

print('%06.2f' % (3.14131463727282))
print('{06.2f}' .format(3.141314463274))
