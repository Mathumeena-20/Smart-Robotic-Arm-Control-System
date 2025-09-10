import motor_control

def test_set_speed():
    result = motor_control.set_speed(1, 50)
    assert result == "Motor 1 speed set to 50"

def test_stop_motor():
    result = motor_control.stop_motor(1)
    assert result == "Motor 1 stopped"

def test_get_motor_status():
    status = motor_control.get_motor_status(1)
    assert isinstance(status, dict)
    assert "speed" in status
    assert "status" in status
