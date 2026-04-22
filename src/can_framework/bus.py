"""Helpers to open and manage a CAN bus connection."""

from __future__ import annotations


def open_bus(channel: str = "vcan0", interface: str = "socketcan"):
    """Open a CAN bus using python-can.

    Raises:
        RuntimeError: If python-can is not installed.
    """
    try:
        import can
    except ImportError as exc:  # pragma: no cover - import guard
        raise RuntimeError(
            "python-can is not installed. Install dependencies first."
        ) from exc

    return can.Bus(interface=interface, channel=channel)
