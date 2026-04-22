# can_messages_automation
Simple automation framework to validate Contorller Area Network (CAN messages)

A Controller Area Network (CAN) is the nervous system inside vehicles. Every ECU (Electronic Control Unit), brake module, infotainment, etc broadcasts short messages overa a shared bus. 
Testing CAN messages means verifying that messages communication is correct, reliable and safe.

CAN messages contains:
- ID (messages priority)
- Data payload
- Timming (how often appears)

CAN testing goal:
- What is sent
- When is sent
- How systems react

Functional correctness
- Does the right message ID appear?
- Are the signal values encoded/decoded correctly?
- Do ECUs react correctly to received messages

Python tools:
- python-can (CAN iteraction in Python)
- cantools  (decoding/encoding CAN messages based on DBC files)
- pytest
- SocketCAN (create a virtual CAN)
     - sudo modprobe vcan
     - sudo ip link add dev vcan0 type vcan
     - sudo ip link set up vcan0 
- Simulated ECU or message responder
