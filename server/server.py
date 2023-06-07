import json
import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from bluetooth import BLE


RANDOM_FOREST_FILENAME = 'test_2_random_forest_model.pkl'


rf_model = joblib.load(RANDOM_FOREST_FILENAME)
scaler = MinMaxScaler()


def scale_data(json_data: dict):
    data_values = list(json_data.values())
    data_array = pd.DataFrame(data_values)
    global scaler
    scaled_data = scaler.fit_transform(data_array).reshape(1, -1)
    return scaled_data


def notification_handler(_, data: bytearray):
    global rf_model

    str_data = data.decode("utf-8")
    json_data = json.loads(str_data)
    # print(json_data)
    scaled_data = scale_data(json_data)
    # print(scaled_data)
    prediction = rf_model.predict(scaled_data)
    # print(prediction)
    if prediction[0] == 1:
        print('Good Posture!')
    else:
        print('Bad Posture!')    


if __name__ == '__main__':
    ble = BLE(notification_handler)
    ble.ble_loop()
    print("Done")