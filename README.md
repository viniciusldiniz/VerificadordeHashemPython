# 🔐 Verificador de Hash

Este script em Python compara um hash alvo com uma lista de senhas, gerando hashes com os algoritmos `md5`, `sha1` ou `sha256`.

## 🚀 Como Usar

### 1. Pré-requisitos

- Python 3.x
- Wordlist com possíveis senhas (uma por linha)

### 2. Executando o script

```bash
python hash_checker.py <caminho_da_wordlist> <hash_alvo> <algoritmo>
```

#### Exemplo:

```bash
python hash_checker.py wordlist.txt 5d41402abc4b2a76b9719d911017c592 md5
```

## 📌 Exemplo de Saída

```
🔍 Iniciando verificação de hash usando MD5...

✅ Hash corresponde à senha: 'hello'
```

## ⚠️ Aviso Legal

> Este script é apenas para **estudo e prática pessoal**.  
> Não utilize em ambientes ou com dados sem autorização.

## 📄 Licença

Distribuído sob a licença MIT.
