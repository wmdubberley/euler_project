from typing import Generator

def fibonacci_generator() -> Generator[int,None,None]:
    a,b=0,1
    while True:
        yield a
        a,b = b, (a+b)
        
def main() -> None:
    fib_gen:  Generator[int,None,None] = fibonacci_generator()
    fib=0
    total=0
    while fib <4_000_000:
        fib = next(fib_gen)
        if fib %2 == 0:
            total += fib
    print(total)
        
if __name__ == '__main__':
    main()