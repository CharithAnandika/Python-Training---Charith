import ipaddress

def is_private_ip(ip_str):
    """
    Returns True if ip_str is a valid IP (v4 or v6) and it's private.
    Returns False if it's invalid or public.
    """
    try:
        ip = ipaddress.ip_address(ip_str)  # ← fixed typo: ipaddress.ip.ip_address → ipaddress.ip_address
        return ip.is_private
    except ValueError:
        return False  # Not a valid IP

# Demo usage
examples = ["192.168.1.1", "8.8.8.8", "fe80::1", "300.300.300.300"]
for ip in examples:
    print(f"{ip}: private? {is_private_ip(ip)}")



    