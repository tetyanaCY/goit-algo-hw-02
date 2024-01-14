from queue import Queue
import time
import random

class Request:
    """Клас для представлення заявки."""
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Заявка ID {self.id}"

def generate_request(request_queue):
    """Функція для генерації нових заявок."""
    request_id = random.randint(1000, 9999)
    new_request = Request(request_id)
    request_queue.put(new_request)
    print(f"Створено {new_request}")

def process_request(request_queue):
    """Функція для обробки заявок з черги."""
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Обробляється {request}")
    else:
        print("Черга пуста")

# Створення черги заявок
request_queue = Queue()

# Демонстрація роботи програми
for _ in range(5):
    generate_request(request_queue)
    time.sleep(1)  # Імітація часу обробки
    process_request(request_queue)
