from src.calc import Calculator


def run_calc():
    x, y, op = input("please input two numbers and a op:").split()
    result = Calculator().compute(int(x), int(y), op)
    print(result)


if __name__ == '__main__':
    run_calc()

