from collections import deque

def is_palindrome(input_string):
    """
    Функція, що перевіряє, чи є рядок паліндромом.
    
    Args:
    input_string (str): Рядок для перевірки.

    Returns:
    bool: True, якщо рядок є паліндромом, інакше False.
    """
    # Видалення пробілів та перетворення рядка до нижнього регістру
    formatted_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(formatted_string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Тестування функції
test_strings = ["Madam, I'm Adam", "racecar", "Hello, World!", "A man, a plan, a canal, Panama"]
results = {s: is_palindrome(s) for s in test_strings}
results

