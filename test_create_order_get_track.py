# Инна Власенко, 49-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request as api
import request_data as data

def test_create_order_get_track():
    # 1. Выполнить запрос на создание заказа
    create_resp = api.post_new_order(data.order_body)
    
    # 2. Сохранить номер трека заказа
    create_json = create_resp.json()
    track = create_json["track"]

    # 3. Выполнить запрос на получение заказа по треку
    track_resp = api.get_track_order(track)

    # 4. Проверить, что код ответа равен 200 
    assert track_resp.status_code == 200