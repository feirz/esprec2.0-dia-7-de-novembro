import http.server
import socketserver
import os

PORT = 8080 #Porta que o servidor irá escutar.
OUTPUT_DIR = "C:\\Users\\diogo\\OneDrive - Instituto Federal Sul-rio-grandense\\Área de Trabalho\\esprec2.0 dia 7 de novembro\\images" #Diretório onde as fotos recebidas serão salvas.

class RequestHandler(http.server.SimpleHTTPRequestHandler): #Classe que trata as requisições do servidor.

    def do_POST(self): #Função que trata as requisições do tipo POST.
        
            content_length = int(self.headers['Content-Length']) #Obtém o tamanho dos dados da foto recebida.
            photo_data = self.rfile.read(content_length) #Lê os dados da foto recebida.

            if not os.path.exists(OUTPUT_DIR):
                #Se o diretório images não existir, ele é criado.
                
                os.makedirs(OUTPUT_DIR)
                #Cria o diretório images caso ele não exista.
                
            existing_files = os.listdir(OUTPUT_DIR)
            #A função listdir() retorna uma lista com o nome de todos os arquivos e diretórios dentro do diretório images.
                          
            next_number = 1 #Variável que será usada para nomear a foto recebida.
            while True: #Loop que verifica se o nome da foto recebida já existe no diretório images.
                file_name = f'{next_number}.jpg' #Nome da foto recebida.
                if file_name not in existing_files: #Verifica se o nome da foto recebida já existe no diretório images e se não existir, o loop é interrompido.
                    break
                next_number += 1 #Incrementa a variável next_number para que a foto recebida seja nomeada com um número que ainda não exista no diretório images.
                
            output_path = os.path.join(OUTPUT_DIR, file_name)
            #A função join() concatena o nome do arquivo com o diretório images.

            with open(output_path, 'wb') as f: #Abre o arquivo para escrita.
                f.write(photo_data) #Escreve a foto recebida no arquivo.
                
            self.send_response(200) #Envia uma resposta de sucesso.

            self.end_headers() #Finaliza o cabeçalho da resposta.

            self.wfile.write(b'Image received successfully') #Escreve na resposta que a imagem foi recebida com sucesso.

def run(): #Função que inicia o servidor.

    server_address = ('', PORT) #Define o endereço do servidor.

    httpd = socketserver.TCPServer(server_address, RequestHandler) #Cria o servidor.
    
    print(f'Iniciando o servidor na porta: {PORT}') #Exibe uma mensagem informando que o servidor foi iniciado.
    httpd.serve_forever() #Faz o servidor ficar rodando indefinidamente.

if __name__ == '__main__': #Verifica se o arquivo foi executado diretamente.
    run() #Chama a função run() para iniciar o servidor.
