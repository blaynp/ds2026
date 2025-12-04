import xmlrpc.client
import base64

SERVER_URL = "http://127.0.0.1:5001"

def send_file(filepath):
    proxy = xmlrpc.client.ServerProxy(SERVER_URL, allow_none=True)

    filename = filepath.split("/")[-1]

    with open(filepath, "rb") as f:
        data = f.read()

    # encode binary data
    encoded = xmlrpc.client.Binary(base64.b64encode(data))

    print(f"[CLIENT] Sending {filename} to RPC server...")
    success = proxy.upload_file(filename, encoded)

    if success:
        print("[CLIENT] File uploaded successfully.")
    else:
        print("[CLIENT] File upload failed.")

if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    send_file(path)
