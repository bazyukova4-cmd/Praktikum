# Инна Власенко, 49-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request as api
import request_data as data

def test_create_order_get_track():
    # 1. Создаем заказ
    create_resp = api.post_new_order(data.order_body)
    assert create_resp.status_code in (200, 201)

    # 2. Сохраняем трек
    create_json = create_resp.json()
    assert "track" in create_json
    track = create_json["track"]

    # 3. Получаем заказ по треку и проверяем код 200
    track_resp = api.get_track_order(track)
    assert track_resp.status_code == 200