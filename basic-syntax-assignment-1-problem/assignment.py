#1 Create two variables – one with your name and one with your age
name = 'Nikhil'
age = 31


#2 Create a function which prints your data as one string
print(str(name + str(age)))


#3 Create a function which prints ANY data (two arguments) as one string
def print_any_data():
    x = input('Enter first string: ')
    y = input('Enter second string: ')
    print(x + y)


print_any_data()


#4 Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)
def decades_alive(age):
    print('You have been alive for ', age // 10, ' decades.')


decades_alive(age)
