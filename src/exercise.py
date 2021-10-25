from timer import Timer

def main():
    #write your code below this line
    timer = Timer()

    while True:
        print(timer)
        timer.advance()

if __name__ == '__main__':
    main()
