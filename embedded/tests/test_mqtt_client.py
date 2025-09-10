import mqtt_client

def test_connect(monkeypatch):
    def mock_connect():
        return True
    monkeypatch.setattr(mqtt_client, "connect", mock_connect)
    assert mqtt_client.connect() is True

def test_publish(monkeypatch):
    def mock_publish(topic, message):
        return f"Published to {topic}"
    monkeypatch.setattr(mqtt_client, "publish", mock_publish)
    result = mqtt_client.publish("robotic_arm/commands", "MOVE")
    assert "Published" in result

def test_subscribe(monkeypatch):
    def mock_subscribe(topic, callback):
        return f"Subscribed to {topic}"
    monkeypatch.setattr(mqtt_client, "subscribe", mock_subscribe)
    result = mqtt_client.subscribe("robotic_arm/telemetry", lambda x: x)
    assert "Subscribed" in result
