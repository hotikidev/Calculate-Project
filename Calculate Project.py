def report_len(num):
    for i in range(num):
        if num > 2:
            print('MORE THAN 2')
        elif num < 2:
            print('Less than2')
report_len(4)    



## say howmany
sayhowmany = input('Enter your word!')

avarage = len(sayhowmany)
print(avarage)



## X calculator  Between two numbers
num1 = int(input('Enter first Number'))
num2 = int(input('Enter Second Number'))

Total = num1 * num2

print(Total)


## - calculator between two numbers
num1 = int(input('Enter first Number'))
num2 = int(input('Enter Second Number'))

Total = num1 - num2

print(Total)


## + calculator between two numbers
num1 = int(input('Enter first Number'))
num2 = int(input('Enter Second Number'))

Total = num1 + num2

print(Total)


## Calculating the Average
Yourlist = [12,17,19,18,15]
avarage = sum(Yourlist) / len(Yourlist)
print(avarage)


## Say hello automaticly
def say_hello(name):
    print(f'Hello to dear{name}')
say_hello('Yourname')




#=========================== HOPE YOU LIKE IT CREATED WITH LOVE BY (@hotikidev)!!!========================