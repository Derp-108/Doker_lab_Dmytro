import time
import random
import paho.mqtt.client as mqtt

# Функція для відправки повідомлення у топік
def send_message(topic, message):
    client = mqtt.Client()
    client.connect("mqtt-broker", 1883)  # Підставте адресу та порт вашого MQTT брокера
    client.publish(topic, message)
    client.disconnect()

# Головна функція
def main():
    while True:
        # Отримання поточного часу з точністю до секунди
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # Відправка повідомлення у топік "common" з поточним часом
        send_message("common", current_time)
        time.sleep(5)  # Затримка на 5 секунд

if __name__ == "__main__":
    main()
