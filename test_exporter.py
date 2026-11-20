from exporter import get_metric_value

def test_metric_value():
    val = get_metric_value()
    assert val > 0, f"Expected positive metric value, got {val}"
