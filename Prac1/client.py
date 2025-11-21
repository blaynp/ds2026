import socket
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001
BUFFER = 4096

def send_file(filepath):
    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

        # connect
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"[CLIENT] Connected to server.")

        # send file metadata
        client_socket.sendall(filename.encode())
        client_socket.recv(BUFFER)          # Wait for ACK

        client_socket.sendall(str(filesize).encode())
        client_socket.recv(BUFFER)

        print(f"[CLIENT] Sending file: {filename} ({filesize} bytes)")

        # write loop
        with open(filepath, "rb") as f:
            while True:
                data = f.read(BUFFER)
                if not data:
                    break
                client_socket.sendall(data)

        print("[CLIENT] File sent.")
        client_socket.close()
        print("[CLIENT] Connection closed.")

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    send_file(path)
