# Инна Власенко, 49-я когорта — Финальный проект. Инженер по тестированию расширенный
import requests

BASE_URL = " https://bf23512e-67a6-4a07-898e-3aa865743223.serverhub.praktikum-services.ru"

def test_create_and_get_order():
    # --- Шаг 1: Создание заказа ---
    order_payload = {
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "address": "ул. Сухарная, 1",
        "metroStation": 2,
        "phone": "+79991112233",
        "rentTime": 2,
        "deliveryDate": "2026-11-27",
        "comment": "Заказ для теста",
        "color": ["BLACK"]
    }
    
    response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_payload)
    assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
    
    # --- Шаг 2: Сохраняем трек ---
    track = response.json().get("track")
    assert track is not None, "Трек не найден в ответе!"
    print(f"Создан заказ с треком: {track}")
    
    # --- Шаг 3: Получение заказа по треку ---
    get_response = requests.get(f"{BASE_URL}/api/v1/orders/track", params={"t": track})
    
    # --- Шаг 4: Проверяем код ответа 200 ---
    assert get_response.status_code == 200, f"Ожидался код 200, получен {get_response.status_code}"
    print(f"Заказ успешно получен. Код ответа: {get_response.status_code}")

if __name__ == "__main__":
    test_create_and_get_order()