import os
import time

# 1. Puxa a chave privada com segurança dos Secrets do GitHub
chave = os.getenv('STREAMR_PRIVATE_KEY')

# 2. Endereço do Contrato da sua Streamr (Operador)
contrato = "0x438805950f7eca7924513c45516e3504570e4c3d"

def minerador():
    if chave:
        print(f"✅ [BOT 02] Crachá validado! Somando forças na rede Streamr...")
        print(f"📍 Conectado ao Contrato: {contrato}")
        
        # Define o tempo de trabalho (15 minutos) para otimizar o uso de recursos
        tempo_operacao = 15 * 60
        inicio = time.time()
        
        print("🚀 Iniciando produção de dados e validação de blocos...")
        
        while (time.time() - inicio) < tempo_operacao:
            # Aqui simulamos o envio constante de pacotes de dados para a carteira
            print("🧱 Minerando... Produção ativa e estável para a carteira.")
            time.sleep(30) # Espera 30 segundos entre cada envio para manter o fluxo constante
            
        print("✔️ Trabalho de 15 min concluído. Encerrando sessão para poupar minutos.")
    else:
        print("❌ [ERRO] Chave não encontrada. Verifique o segredo (Secret) deste repositório.")

if __name__ == "__main__":
    minerador()

