import os
chave = os.getenv('STREAMR_PRIVATE_KEY')
def minerar():
    if chave:
        print("✅ [BOT 02] Crachá validado! Somando forças na rede...")
    else:
        print("❌ [ERRO] Verifique o Secret deste repositório.")
if __name__ == "__main__":
    minerar()
