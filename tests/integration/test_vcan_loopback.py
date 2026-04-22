import os

import pytest

from can_framework.bus import open_bus


@pytest.mark.integration
def test_open_vcan_bus() -> None:
    """Opt-in integration test for local vcan setup."""
    if os.getenv("RUN_VCAN_TESTS") != "1":
        pytest.skip("Set RUN_VCAN_TESTS=1 to run vcan integration tests.")

    can = pytest.importorskip("can")

    bus = open_bus(channel="vcan0", interface="socketcan")
    try:
        assert isinstance(bus, can.BusABC)
    finally:
        bus.shutdown()
