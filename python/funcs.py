def square(x):
    return x * x + 5

def new():
    for i in range(42):
        print(f'{i} squared is {square(i)}')

if __name__ == '__main__':
    main()
