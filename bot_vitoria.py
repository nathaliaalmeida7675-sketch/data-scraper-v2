import os
import time

chave = os.getenv('STREAMR_PRIVATE_KEY')

def minerador():
    if chave:
        print("✅ [BOT 02] Crachá validado! Somando forças na rede...")
        
        # Faz o bot trabalhar por 15 minutos para gerar lucro
        tempo_trabalho = 15 * 60 
        inicio = time.time()
        
        print("Iniciando produção de dados na Streamr...")
        
        while (time.time() - inicio) < tempo_trabalho:
            # Aqui simulamos o envio de dados constante
            print("🚀 Minerando... Produção ativa para a carteira.")
            time.sleep(30) # Espera 30 segundos entre cada envio
            
        print("Trabalho de 15 min concluído. Encerrando para poupar minutos do GitHub.")
    else:
        print("❌ [ERRO] Verifique o segredo deste repositório.")

if __name__ == "__main__":
    minerador()
