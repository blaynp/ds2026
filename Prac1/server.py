import socket
import os

HOST = "0.0.0.0"     # Listen on all interfaces
PORT = 5001
BUFFER = 4096

def start_server():
    # socket → bind → listen
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT} ...")

        # accept
        conn, addr = server_socket.accept()
        print(f"[SERVER] Connected by {addr}")

        # read file metadata first
        filename = conn.recv(BUFFER).decode().strip()
        conn.sendall(b"OK")      # ACK

        filesize = int(conn.recv(BUFFER).decode().strip())
        conn.sendall(b"OK")

        print(f"[SERVER] Receiving file: {filename} ({filesize} bytes)")

        # read loop → write to file
        with open("recv_" + filename, "wb") as f:
            received = 0
            while received < filesize:
                data = conn.recv(BUFFER)
                if not data:
                    break
                f.write(data)
                received += len(data)

        print("[SERVER] File received.")
        conn.close()
        print("[SERVER] Connection closed.")

if __name__ == "__main__":
    start_server()
