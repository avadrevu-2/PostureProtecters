import json
import csv
from bluetooth import BLE


FILENAME = 'real_data_bad_2.csv'
wrote_header_row = False


def write_to_csv(data_row: dict):
    global wrote_header_row
    if not wrote_header_row:
        with open(FILENAME, 'w+', newline='') as f:
            csv_writer = csv.writer(f)
            header = data_row.keys()
            csv_writer.writerow(header)
            wrote_header_row = True
    else:
        with open(FILENAME, 'a', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(data_row.values())


def notification_handler(_, data: bytearray):
    str_data = data.decode("utf-8")
    print(str_data)
    json_data = json.loads(str_data)
    print(json_data)
    write_to_csv(json_data)



if __name__ == "__main__":
    ble = BLE(notification_handler)
    ble.ble_loop()
    print("Done")