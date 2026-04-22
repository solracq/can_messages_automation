#!/usr/bin/env bash
set -euo pipefail

# Creates a virtual CAN interface for local integration tests.
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan || true
sudo ip link set up vcan0
ip -details link show vcan0
