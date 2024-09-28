from collections import deque

def is_palindrome(s):
    # Преобробка рядка: перетворення в нижній регістр та видалення пробілів
    s = ''.join(s.lower().split())
    
    # Створення двосторонньої черги з символів рядка
    char_deque = deque(s)
    
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        if left_char != right_char:
            return False
    return True

# приклади використання
test_strings = [
    "Я несу сани",
    "Ротор",
    "Не паліндром",
    "Довод",
    "Тут",
    "Зірка наказ казан краз із",
    "123321"
]


for s in test_strings:
    if is_palindrome(s):
        print(f'"{s}" є паліндромом.')
    else:
        print(f'"{s}" не є паліндромом.')