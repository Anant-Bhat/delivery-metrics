from exporter import get_metric_value

def test_metric_value():
    val = get_metric_value()
    assert val < 0, f"Controlled failure: Expected < 0, got {val}"
