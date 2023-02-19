class Calculator:
    def compute(self, x: int, y: int, op: str):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        return 0
