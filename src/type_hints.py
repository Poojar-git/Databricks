def calculate(a: int, b:int)->int:
    return a+b

def add(num1: int, num2: int) -> int:
    return num1 + num2

print(add(10, 20))

age: int = 23
price: float = 99.99
name: str = "Pooja"
is_active: bool = True

print(age)
print(price)
print(name)
print(is_active)

numbers: list[int] = [10, 20, 30, 40]

print(numbers)

employee: dict[str, int] = {
    "Pooja": 50000,
    "Rahul": 60000
}

print(employee)