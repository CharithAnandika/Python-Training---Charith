# server.py

import socket
import os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
FILE_SAVE_DIR = 'received_files'  # Directory where received files will be saved

def start_server():
    # Create the directory to save received files if it doesn't exist
    os.makedirs(FILE_SAVE_DIR, exist_ok=True)
    print(f"Directory '{FILE_SAVE_DIR}' is ready.")

    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the host and port
        s.bind((HOST, PORT))
        print(f"Server listening on {HOST}:{PORT}")

        # Listen for incoming connections (allow up to 1 pending connection)
        s.listen(1)

        while True:
            # Accept a new connection
            conn, addr = s.accept()
            with conn:  # 'with' statement ensures the socket is closed automatically
                print(f"Connected by {addr}")
                try:
                    # Step 1: Receive the filename
                    filename_data = conn.recv(1024)  # Receive up to 1024 bytes for the filename
                    if not filename_data:
                        print(f"No filename data received from {addr}. Closing connection.")
                        continue  # Go back to listening for a new client

                    filename = filename_data.decode('utf-8').strip()
                    # Basic security: Sanitize the filename to prevent directory traversal
                    filename = os.path.basename(filename)
                    save_path = os.path.join(FILE_SAVE_DIR, filename)

                    print(f"Receiving file: '{filename}'")
                    print(f"Saving to: '{save_path}'")

                    # Step 2: Receive the file content and write it
                    with open(save_path, 'wb') as f:  # Open in binary write mode
                        while True:
                            data = conn.recv(1024)
                            if not data:
                                break  # No more data received
                            f.write(data)

                    print(f"Successfully received and saved '{filename}' from {addr}")

                except Exception as e:
                    print(f"Error during file transfer for {addr}: {e}")
                finally:
                    print(f"Connection from {addr} closed.")

if __name__ == "__main__":
    start_server()
