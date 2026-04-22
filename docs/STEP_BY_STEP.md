# Step-by-Step Build Plan (Simple Start)

1. Create a predictable project structure.
2. Add base dependencies (`pytest`, `python-can`, `cantools`).
3. Add small validation helpers for ID and timing checks.
4. Add smoke/unit tests that run without hardware.
5. Add an opt-in integration test using `vcan0`.
6. Add DBC decoding helpers.
7. Add test data and reusable fixtures.
8. Add CI execution for smoke/unit on each push.
