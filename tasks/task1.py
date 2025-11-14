# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input().split())
    is_equilateral = (a == b == c)
    print(is_equilateral)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()