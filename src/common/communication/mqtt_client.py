import paho.mqtt.client as mqtt
import time

class MQTTClient:
    def __init__(self, broker_address, port=1883, client_id="python_mqtt_client"):
        self.broker_address = broker_address
        self.port = port
        self.client_id = client_id
        self.client = mqtt.Client(client_id=self.client_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.message_callback = None

    def _on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}\n")

    def _on_message(self, client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if self.message_callback:
            self.message_callback(msg.topic, msg.payload.decode())

    def connect(self):
        try:
            self.client.connect(self.broker_address, self.port)
            self.client.loop_start() # Start a non-blocking loop
        except Exception as e:
            print(f"Error connecting to MQTT broker: {e}")

    def publish(self, topic, message):
        result = self.client.publish(topic, message)
        status = result[0]
        if status == 0:
            print(f"Sent `{message}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def subscribe(self, topic, callback=None):
        self.client.subscribe(topic)
        if callback:
            self.message_callback = callback

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        print("Disconnected from MQTT Broker.")

if __name__ == "__main__":
    # Example Usage:
    # You would typically run an MQTT broker (e.g., Mosquitto) locally or use a public one.
    # For testing, you can install Mosquitto: sudo apt-get install mosquitto mosquitto-clients
    # Then run: mosquitto -v

    broker = "localhost" # Replace with your MQTT broker address
    client = MQTTClient(broker)
    client.connect()

    def my_message_handler(topic, message):
        print(f"Custom handler: Topic: {topic}, Message: {message}")

    client.subscribe("traffic/signals", my_message_handler)
    client.subscribe("traffic/data")

    # Publish some messages
    client.publish("traffic/signals", "change_to_green_north")
    client.publish("traffic/data", "density_north: 15")

    try:
        while True:
            time.sleep(1) # Keep the script running to receive messages
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        client.disconnect()


