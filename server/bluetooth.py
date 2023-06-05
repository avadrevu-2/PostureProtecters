import asyncio
from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice


ESP_32_BLE_NAME = 'ESP32-PP'
UART_TX_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for TX
UART_RX_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e" #Nordic NUS characteristic for RX


class BLE():
    def __init__(self, notification_handler) -> None:
        self.notification_handler = notification_handler
        

    def ble_loop(self) -> None:
        ble_devices = asyncio.run(self.__discover())
        esp32_ble = self.__find_esp32(ble_devices)
        if esp32_ble is None:
            print("Couldn't find ESP32 Bluetooth Device")
            return

        print("Starting Data Collection")
        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.__run(esp32_ble, loop))
        except KeyboardInterrupt:
            print("Stopping Data Collection")


    async def __run(self, device: BLEDevice, loop):
        async with BleakClient(device, loop=loop) as client:
            await client.is_connected()
            await client.start_notify(UART_RX_UUID, self.notification_handler)
            while True:
                await asyncio.sleep(0.01)
    
    @staticmethod
    async def __discover() -> list[BLEDevice]:
        devices = await BleakScanner.discover()
        for d in devices:
            print(d)
        return devices


    @staticmethod
    def __find_esp32(ble_devices: list[BLEDevice]) -> BLEDevice | None:
        for device in ble_devices:
            if device.name == ESP_32_BLE_NAME:
                return device
        return None