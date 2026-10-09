# ARP Intrusion Detector

**AVIP 2026 Cybersecurity — Task 10**

## Objective
Read the local ARP table and identify MAC addresses that are not in a trusted allowlist.

## Features
- Reads the local ARP table using `arp -a`.
- Extracts IPv4/MAC pairs.
- Compares detected MAC addresses with trusted MAC addresses.
- Reports unknown MAC addresses.
- Includes automated tests.
- Does not perform packet injection or active network attacks.

## Requirements
Python 3.x. Standard-library modules only.

## Run
```bash
python arp_detector.py
```

The actual devices and addresses depend on your authorized local network.

## Tests
```bash
python tests/test_arp_detector.py
```
Expected:
```text
All ARP Intrusion Detector tests passed.
```

## How It Works
1. Read the local ARP table.
2. Extract IP/MAC pairs.
3. Ask for trusted MAC addresses.
4. Compare detected MACs with the allowlist.
5. Report unknown entries for further investigation.

## Security Concept
ARP maps local IPv4 addresses to MAC addresses. An unexpected MAC can be an indicator for investigation, but an unknown MAC does not automatically mean an intrusion.

## Limitations
This is an educational detector and does not prove that an attack occurred. Production monitoring needs additional validation and controls.

## Ethics
Use only on your own computer/network or a network for which you have explicit authorization to monitor.
