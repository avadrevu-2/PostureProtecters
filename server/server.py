import json
import joblib
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from bluetooth import BLE


RANDOM_FOREST_FILENAME = 'random_forest_model.pkl'


rf_model = joblib.load(RANDOM_FOREST_FILENAME)
scaler = MinMaxScaler()


def preprocess_data(json_data: dict):
    data_values = list(json_data.values())
    data_array = np.array(data_values).reshape(1, -1)
    global scaler
    scaled_data = scaler.fit_transform(data_array)
    return scaled_data


def notification_handler(_, data: bytearray):
    str_data = data.decode("utf-8") + "}"
    json_data = json.loads(str_data)
    preprocessed_data = preprocess_data(json_data)
    global rf_model
    prediction = rf_model.predict(preprocessed_data)
    if prediction[0] == 1:
        print('Good Posture!')
    else:
        print('Bad Posture!')    


if __name__ == '__main__':
    ble = BLE(notification_handler)
    ble.ble_loop()
    print("Done")