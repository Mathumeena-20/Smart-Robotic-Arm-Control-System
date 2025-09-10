import sensor_interface

def test_read_position():
    pos = sensor_interface.read_position(1)
    assert isinstance(pos, float)

def test_get_all_positions():
    positions = sensor_interface.get_all_positions()
    assert isinstance(positions, dict)
    assert 1 in positions
