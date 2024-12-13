try:
    # Usando 'with' para garantir que o arquivo seja fechado automaticamente
    with open(r"/home/diniz/Downloads/exemplo.txt", "r") as stream:
        # Processamento do arquivo vai aqui.
        content = stream.read()
        print(content)  # Exemplo de como processar o conteúdo.
except FileNotFoundError as fnf_error:
    print("O arquivo não foi encontrado:", fnf_error)
except IOError as io_error:
    print("Erro de entrada/saída:", io_error)
except Exception as exc:
    print("Ocorreu um erro inesperado:", exc)
