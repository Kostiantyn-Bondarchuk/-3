import socket


# Функція для перевірки, чи порт відкритий
def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Таймаут у 1 секунду
    result = sock.connect_ex((host, port))  # Перевірка порту
    sock.close()
    return result == 0  # Якщо результат 0, то порт відкритий


# Основна функція для сканування портів
def scan_ports(host, start_port, end_port):
    print(f"Scanning host {host} for open ports between {start_port} and {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            open_ports.append(port)
            print(f"Port {port} is open")

    if not open_ports:
        print("No open ports found.")
    else:
        print("\nOpen ports found:", open_ports)


if __name__ == '__main__':
    # Введення хоста та діапазону портів
    host = input("Enter the host (e.g. 127.0.0.1 or example.com): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Перевірка портів
    scan_ports(host, start_port, end_port)
