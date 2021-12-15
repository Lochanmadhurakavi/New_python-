def prime_checker(number):
    times = 0
    for n in range(2, number+1):
        if number % n == 0:
            times += 1
    if times == 1:
        print("It's a prime number")
    else:
        print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)
