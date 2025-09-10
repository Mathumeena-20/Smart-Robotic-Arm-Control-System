import utils
import json

def test_log_function(capsys):
    utils.log("Test message")
    captured = capsys.readouterr()
    assert "Test message" in captured.out

def test_to_json():
    data = {"key": "value"}
    json_str = utils.to_json(data)
    assert isinstance(json_str, str)
    assert json.loads(json_str) == data

def test_from_json_valid():
    json_str = '{"key": "value"}'
    result = utils.from_json(json_str)
    assert isinstance(result, dict)
    assert result["key"] == "value"

def test_from_json_invalid(capsys):
    result = utils.from_json("INVALID_JSON")
    captured = capsys.readouterr()
    assert result == {}
    assert "Invalid JSON received" in captured.out
