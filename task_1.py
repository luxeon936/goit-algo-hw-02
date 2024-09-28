from queue import Queue
import time

# Створити чергу заявок
queue = Queue()

# Лічильник для унікальних ідентифікаторів заявок
request_id = 0

def generate_request():
    global request_id
    request_id += 1
    request = f"Заявка {request_id}"
    queue.put(request)
    print(f"Створено {request}")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробляється {request}")
        # Імітація часу обробки
        time.sleep(1)
        print(f"Оброблено {request}")
    else:
        print("Черга пуста.")

def main():
    try:
        while True:
            generate_request()
            process_request()
            # Пауза перед наступною ітерацією
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nПрограму завершено користувачем.")

if __name__ == "__main__":
    main()