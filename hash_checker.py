import hashlib
import sys

def gerar_hash(texto, algoritmo):
    if algoritmo == "md5":
        return hashlib.md5(texto.encode()).hexdigest()
    elif algoritmo == "sha1":
        return hashlib.sha1(texto.encode()).hexdigest()
    elif algoritmo == "sha256":
        return hashlib.sha256(texto.encode()).hexdigest()
    else:
        raise ValueError("Algoritmo não suportado. Use: md5, sha1 ou sha256.")

def verificar_hash(wordlist_path, hash_alvo, algoritmo):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            senhas = f.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo '{wordlist_path}' não encontrado.")
        sys.exit(1)

    print(f"🔍 Iniciando verificação de hash usando {algoritmo.upper()}...
")

    for senha in senhas:
        hash_gerado = gerar_hash(senha, algoritmo)
        if hash_gerado == hash_alvo:
            print(f"✅ Hash corresponde à senha: '{senha}'")
            return

    print("❌ Nenhuma correspondência encontrada na wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python hash_checker.py <caminho_da_wordlist> <hash_alvo> <algoritmo>")
        print("Exemplo: python hash_checker.py wordlist.txt 5d41402abc4b2a76b9719d911017c592 md5")
        sys.exit(1)

    wordlist_path = sys.argv[1]
    hash_alvo = sys.argv[2]
    algoritmo = sys.argv[3].lower()

    verificar_hash(wordlist_path, hash_alvo, algoritmo)
