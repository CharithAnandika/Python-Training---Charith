import ipaddress

ips_list = ["192.168.1.1", "300.168.1.256", "fe80::1", "abc.def"]
valid_ips = []
invalid_ips = []

def validate_ip_address(ip_string):
    try:
        ip_obj = ipaddress.ip_address(ip_string)
        return True, ip_obj
    except ValueError as e:
        return False, str(e)

for addr in ips_list:
    is_valid, result = validate_ip_address(addr)
    if is_valid:
        valid_ips.append(result)           # store IP object
    else:
        invalid_ips.append((addr, result))  # store (ip, error)

print(" Valid IPs:")
for ip_obj in valid_ips:
    print(f"  * {ip_obj} (IPv{ip_obj.version})")

print("\n Invalid IPs:")
for ip_str, error in invalid_ips:
    print(f"  * {ip_str} — {error}")

