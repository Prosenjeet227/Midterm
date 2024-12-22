def fibonacci_series(n):

    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def sum_of_fibonacci(series):

    return sum(series)

def main():

    n = int(input("Enter the number of terms for the Fibonacci series: "))

    series = fibonacci_series(n)


    total_sum = sum_of_fibonacci(series)


    print("Fibonacci series:", series)
    print("Sum of the Fibonacci series:", total_sum)

if __name__ == "__main__":
    main()
