import platform
import re
import subprocess


def get_arp_table():
    return subprocess.run(["arp", "-a"], capture_output=True, text=True, check=False).stdout


def parse_arp_table(output):
    entries = []
    ipv4_pattern = r"(?:\d{1,3}\.){3}\d{1,3}"
    mac_pattern = r"(?:[0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2}"
    for line in output.splitlines():
        ip = re.search(ipv4_pattern, line)
        mac = re.search(mac_pattern, line)
        if ip and mac:
            entries.append({"ip": ip.group(), "mac": mac.group().lower().replace("-", ":")})
    return entries


def find_unknown_devices(entries, trusted_macs):
    trusted = {mac.lower().replace("-", ":") for mac in trusted_macs}
    return [entry for entry in entries if entry["mac"] not in trusted]


def main():
    print("ARP Intrusion Detector")
    print("Use only on a network you own or are authorized to monitor.\n")
    trusted_input = input("Enter trusted MAC addresses separated by commas: ")
    trusted_macs = [mac.strip() for mac in trusted_input.split(",") if mac.strip()]
    output = get_arp_table()
    entries = parse_arp_table(output)
    if not entries:
        print("No ARP entries were found.")
        return
    print("\nDetected ARP entries:")
    for entry in entries:
        print(f'{entry["ip"]} -> {entry["mac"]}')
    unknown = find_unknown_devices(entries, trusted_macs)
    print("\nResult:")
    if unknown:
        print("Unknown MAC address(es) detected:")
        for entry in unknown:
            print(f'{entry["ip"]} -> {entry["mac"]}')
    else:
        print("No unknown MAC addresses detected.")


if __name__ == "__main__":
    main()
