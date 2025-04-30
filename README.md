## Descrição do Código

O código `ScannPort-py` é uma ferramenta simples em Python que escaneia portas de um IP ou domínio especificado, verificando se estão abertas. Ele utiliza a biblioteca `socket` para tentar estabelecer uma conexão com as portas e retorna quais estão abertas.

### Como funciona:

1. O script solicita que o usuário insira um endereço IP ou domínio a ser escaneado.
2. O código tenta se conectar às portas de 1 a 1024 no alvo especificado.
3. Se a conexão for bem-sucedida, a porta é identificada como "aberta" e a informação é exibida no terminal.
4. Ao final, o tempo total do escaneamento é exibido.

### Funções principais:

- `scan_port(ip, port)`: Tenta conectar à porta especificada do IP e exibe se a porta está aberta ou não.
- `main()`: Função principal que solicita o alvo, realiza o escaneamento e calcula o tempo total.

### Exemplo de execução:

```bash
Digite o IP ou domínio a ser escaneado: 127.0.0.1
[+] Porta 22 aberta
[+] Porta 80 aberta
[+] Porta 443 aberta
Tempo total: 1.23 segundos