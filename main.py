import urllib.request
import json
import time
import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- AUTOMAÇÃO 1: Scanner Espacial (Viajando para fora do Render) ---
def escutar_dados_espaciais():
    # API Pública Global que rastreia a Estação Espacial em tempo real
    url = "http://opennotify.org"
    print("🚀 Scanner Espacial Ativado. Viajando para fora do servidor...")
    
    ciclo = 0
    
    while True:
        try:
            ciclo += 1
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urllib.request.urlopen(req) as resposta:
                dados = json.loads(resposta.read().decode('utf-8'))
                
                # Se a viagem deu certo, extraímos as coordenadas direto do espaço
                if dados.get("message") == "success":
                    posicao = dados.get("iss_position", {})
                    lat = posicao.get("latitude")
                    lon = posicao.get("longitude")
                    timestamp = dados.get("timestamp")
                    
                    print(f"🛰️ ISS POSITION | Ciclo: #{ciclo} | Latitude: {lat} | Longitude: {lon} | Status: CONECTADO COM O ESPAÇO")
                else:
                    print("⚠️ Conexão estabelecida, mas os satélites estavam instáveis.")
                    
        except Exception as erro:
            print(f"❌ Falha na viagem de dados: {erro}")
            
        time.sleep(15) # Viaja para buscar novos dados a cada 15 segundos

# --- AUTOMAÇÃO 2: Servidor Web Nativo para o Render Grátis ---
class ServidorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Engine Espacial Online!")

def rodar_servidor_web():
    porta_render = int(os.environ.get("PORT", 10000))
    endereco = ('', porta_render)
    httpd = HTTPServer(endereco, ServidorHandler)
    print(f"🌐 Servidor Web escutando na porta {porta_render} de forma nativa.")
    httpd.serve_forever()

if __name__ == "__main__":
    # 1. Inicia o rastreador espacial em segundo plano
    thread_espacial = threading.Thread(target=escutar_dados_espaciais)
    thread_espacial.daemon = True
    thread_espacial.start()

    # 2. Mantém o Render estável em verde
    rodar_servidor_web()

