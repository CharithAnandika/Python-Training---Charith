import subprocess
import platform
import re
import logging
import time

import csv
from datetime import datetime

import smtplib
from email.mime.text import MIMEText

import schedule

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def ping_host(host, count=1, timeout=1):
    """
    Pings a given host and returns True if successful, False otherwise.
    Also returns the ping output for detailed analysis.

    Args:
        host (str): The IP address or hostname to ping.
        count (int): The number of packets to send (default: 1).
        timeout (int): Timeout in seconds for each packet (default: 1).

    Returns:
        tuple: (bool success, str raw_output)
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    timeout_param = '-w' if platform.system().lower() == 'windows' else '-W'

    command = ['ping', param, str(count), timeout_param, str(timeout), host]

    try:
        # Run the ping command
        result = subprocess.run(command, capture_output=True, text=True, timeout=timeout * (count + 2)) # Added buffer to timeout

        raw_output = result.stdout + result.stderr

        if result.returncode == 0:
            logging.info(f"Ping successful for {host}.")
            return True, raw_output
        else:
            logging.warning(f"Ping failed for {host}. Return code: {result.returncode}")
            logging.debug(f"Ping output for {host}:\n{raw_output}")
            return False, raw_output
    except subprocess.TimeoutExpired:
        logging.error(f"Ping command timed out for {host}.")
        return False, "TimeoutExpired"
    except FileNotFoundError:
        logging.error("Ping command not found. Make sure ping is installed and in your PATH.")
        return False, "FileNotFound"
    except Exception as e:
        logging.error(f"An unexpected error occurred while pinging {host}: {e}")
        return False, str(e)

# Example usage:
# ... (previous code for ping_host and imports) ...