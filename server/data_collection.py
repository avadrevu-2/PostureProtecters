import asyncio
import json
import csv
from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice


FILENAME = 'data.csv'
ESP_32_BLE_NAME = 'ESP32-PP'
UART_TX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for TX
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for RX

wrote_header_row = False


async def discover() -> list[BLEDevice]:
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)
    return devices


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


def notification_handler(_, data):
    str_data = data.decode("utf-8") + "}"
    print(str_data)
    json_data = json.loads(str_data)
    print(json_data)
    write_to_csv(json_data)


async def run(device: BLEDevice, loop):
    async with BleakClient(device, loop=loop) as client:
        await client.is_connected()
        await client.start_notify(UART_RX_UUID, notification_handler)
        while True:
            await asyncio.sleep(0.01)



def find_esp32(ble_devices: list[BLEDevice]) -> BLEDevice | None:
    for device in ble_devices:
        if device.name == ESP_32_BLE_NAME:
            return device
    return None


if __name__ == "__main__":
    ble_devices = asyncio.run(discover())
    esp32_ble = find_esp32(ble_devices)
    if esp32_ble is None:
        print("Couldn't find ESP32 Bluetooth Device")
        while True: 1

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run(esp32_ble, loop))
