# Convert to PDF

Este projeto é um conversor simples que transforma arquivos como **.txt**, **.docx**, **.png** (entre outros) em **PDF**.  
Ele foi desenvolvido com **Flask** como parte do aprendizado e prática com o framework.  
Além disso, utiliza **LibreOffice** para ajudar na conversão de formatos como DOCX.

## Funcionalidades

- Upload de arquivos suportados (TXT, DOCX, PNG etc.)
- Conversão rápida e simples para PDF
- Uso do LibreOffice para conversão de documentos
- Interface web usando Flask

## Tecnologias usadas

- Python 3
- Flask
- LibreOffice
- Bibliotecas auxiliares (listadas no `requirements.txt`)

## Como rodar localmente

Clone o repositório:

    ```bash
    git clone https://github.com/Tomazbr9/convert-to-pdf.git
    cd convert-to-pdf

Instale as dependências:

    ```bash
    pip install -r requirements.txt

Certifique-se de ter o LibreOffice instalado em sua máquina.
Ele é necessário para a conversão de arquivos

Execute o projeto:

    ```bash
    python run.py

Abra no navegador:
Acesse http://localhost:5000

## Observações
Este projeto é voltado para aprendizado e prática, então pode conter melhorias futuras.
Sugestões e contribuições são bem-vindas!