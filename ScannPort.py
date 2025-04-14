import socket
import time

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((ip,port))
            print(f"[+] Porta {port} aberta")
    except socket.gaierror:
        print("Endereço inválido.")
        pass
    
def main():
    alvo = input("Digite o IP ou domínio a ser escaneado: ")
    inicio = time.time()

    for porta in range(1, 1025):
        scan_port(alvo, porta)
    
    fim = time.time()
    print(f"\nTempo total: {round(fim - inicio, 2)} segundos")

if __name__ == "__main__":
    main()