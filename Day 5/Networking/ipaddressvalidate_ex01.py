import ipaddress

def validate_ip_address(ip_string):
    try:
        ip_object = ipaddress.ip_address(ip_string)
        return True, ip_object
    except ValueError as e:
        return False, str(e)

def split_ip_list(ip_list):
    """
    Splits IPs into valid and invalid lists.
    Returns a tuple: (valid_ips, invalid_ips).
      - valid_ips: list of IPv4Address/IPv6Address objects
      - invalid_ips: list of (ip_string, error_message) tuples
    """
    valid_ips = []
    invalid_ips = []
    for ip in ip_list:
        is_valid, result = validate_ip_address(ip)
        if is_valid:
            valid_ips.append(result)
        else:
            invalid_ips.append((ip, result))
    return valid_ips, invalid_ips

# Example:
ips = ["192.168.1.1", "300.168.1.256", "fe80::1", "abc.def"]
valid, invalid = split_ip_list(ips)

# Display results:
print("Valid IPs:")
for ip_obj in valid:
    print(f" *{ip_obj} (IPv{ip_obj.version})")

print("\nInvalid IPs:")
for ip_str, error in invalid:
    print(f" *{ip_str} — {error}")
