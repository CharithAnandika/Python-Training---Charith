# server.py
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def start_server():
    # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind((HOST, PORT))
        print(f"Server listening on {HOST}:{PORT}")

        # Listen for incoming connections, allow up to 5 queued connections
        s.listen(5)

        # Accept a connection when a client connects
        conn, addr = s.accept() # conn is a new socket object for this connection
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Receive data from the client (up to 1024 bytes)
                data = conn.recv(1024)
                if not data:
                    break # If no data, client has closed connection

                decoded_data = data.decode('utf-8')
                print(f"Received from client: {decoded_data}")

                # Prepare a response
                response = f"Server received: {decoded_data.upper()}"
                conn.sendall(response.encode('utf-8')) # Send all data
                
                if decoded_data.lower() == "bye":
                    print("Client requested to close connection.")
                    break
    print("Server closed.")

if __name__ == "__main__":
    start_server()