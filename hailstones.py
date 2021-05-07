import random


def main():
    count = 0
    n = int(input("Enter a number: "))
    while n > 1:
        if n % 2 == 0:
            print(str(n), " is even, so I take half", str(n / 2))
            n = n / 2
        else:
            if n % 2 != 0:
                print(str(n), " is odd, so I make 3n+1", str(3 * n + 1))
            n = 3 * n + 1
        count += 1
        if n == 1:
            print("The process took ", str(count), " steps to reach 1.")


if __name__ == '__main__':
    main()
