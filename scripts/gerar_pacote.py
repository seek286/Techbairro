# ============================================================
# GERAR PACOTE DA VERSÃO (Aula 27)
# ============================================================
#
# Monta o arquivo .zip da versão que será publicada,
# deixando de fora arquivos e pastas que não devem ser distribuídos.

import os
import zipfile

# Caminhos do projeto
PASTA_DOS_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
PASTA_DO_PROJETO = os.path.dirname(PASTA_DOS_SCRIPTS)

# Versão que será publicada
VERSAO = "3.3.2"

# Pastas que não entram no pacote
PASTAS_FORA = ["dist", "__pycache__", ".git", ".venv", "venv"]

# Tipos de arquivo que não entram no pacote
EXTENSOES_FORA = [".db", ".pyc"]

# Pasta onde o pacote será salvo
PASTA_DIST = os.path.join(PASTA_DO_PROJETO, "dist")
os.makedirs(PASTA_DIST, exist_ok=True)

NOME_PACOTE = f"TechBairro-{VERSAO}"
CAMINHO_PACOTE = os.path.join(PASTA_DIST, NOME_PACOTE + ".zip")

print(f"Gerando {NOME_PACOTE}.zip")
print()

incluidos = 0
deixados_de_fora = 0

# Cria o arquivo ZIP
with zipfile.ZipFile(CAMINHO_PACOTE, "w", zipfile.ZIP_DEFLATED) as pacote:

    for pasta_atual, subpastas, arquivos in os.walk(PASTA_DO_PROJETO):

        # Impede que o os.walk entre nas pastas excluídas
        subpastas[:] = [
            pasta for pasta in subpastas
            if pasta not in PASTAS_FORA
        ]

        for nome in arquivos:
            caminho = os.path.join(pasta_atual, nome)
            relativo = os.path.relpath(caminho, PASTA_DO_PROJETO)
            extensao = os.path.splitext(nome)[1].lower()

            if extensao in EXTENSOES_FORA:
                print(f"  fora      {relativo}")
                deixados_de_fora += 1
                continue

            # Evita incluir o próprio ZIP dentro dele mesmo
            if os.path.abspath(caminho) == os.path.abspath(CAMINHO_PACOTE):
                continue

            pacote.write(
                caminho,
                os.path.join(NOME_PACOTE, relativo)
            )

            print(f"  incluído  {relativo}")
            incluidos += 1

print()
print(f"Arquivos incluídos: {incluidos}")
print(f"Arquivos deixados de fora: {deixados_de_fora}")
print(f"Pacote salvo em: {CAMINHO_PACOTE}")
