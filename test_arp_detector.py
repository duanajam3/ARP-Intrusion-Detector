from arp_detector import parse_arp_table, find_unknown_devices

sample = """
  192.168.1.1           aa-bb-cc-dd-ee-ff     dynamic
  192.168.1.20          11-22-33-44-55-66     dynamic
"""
entries = parse_arp_table(sample)
assert len(entries) == 2
assert entries[0]["mac"] == "aa:bb:cc:dd:ee:ff"
unknown = find_unknown_devices(entries, ["AA:BB:CC:DD:EE:FF"])
assert len(unknown) == 1
assert unknown[0]["mac"] == "11:22:33:44:55:66"
print("All ARP Intrusion Detector tests passed.")
