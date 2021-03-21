###solution to exercise 77 from ben stephenson's "the python workbook".

num = str(input('Enter an binary number:'))
num = num[::-1]

result = 0

for i in range(len(num)):
  result += int(num[i]) * 2 ** i

print(f'The decimal equivalent is: {result}.')
