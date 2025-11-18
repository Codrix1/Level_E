import socket

def test_port(address: str, dest_port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            print("waiting for connection")
            if sock.connect_ex((address, dest_port)) == 0:
                print("connected")
                return True

        return False
    except (OSError, ValueError) as e:
        print(f"⚠️ Error: {e}")
        return False
    
def main():
    address = "64.233.160.0"
    port = 23

    if test_port(address=address , dest_port=port):
        print("connection")
    else:
        print("no connection")


if __name__ == "__main__":
    main()