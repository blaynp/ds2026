from xmlrpc.server import SimpleXMLRPCServer
import base64

def upload_file(filename, filedata):
    try:
        data = base64.b64decode(filedata.data)
        with open("recv_" + filename, "wb") as f:
            f.write(data)
        print(f"[SERVER] Saved file: recv_{filename}")
        return True
    except Exception as e:
        print("Error:", e)
        return False

def ping():
    return "RPC server alive"

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("0.0.0.0", 5001), allow_none=True)
    print("[SERVER] RPC Server listening on port 5001")

    server.register_function(upload_file, "upload_file")
    server.register_function(ping, "ping")

    server.serve_forever()
