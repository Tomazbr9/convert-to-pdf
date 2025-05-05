from PIL import Image

import subprocess

import os

def convert_to_pdf(input_path, output_path):
    input_path = os.path.abspath(input_path)
    output_dir = os.path.dirname(os.path.abspath(output_path))

    try:
        # usa LibreOffice (soffice) em modo headless para converter arquivos suportados em PDF
        subprocess.run([
            "soffice",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            input_path
        ], check=True)

        # obtém nome gerado automaticamente pelo soffice (mantém nome base + .pdf)
        generated_name = os.path.splitext(os.path.basename(input_path))[0] + ".pdf"
        generated_path = os.path.join(output_dir, generated_name)

        if os.path.exists(generated_path):
            os.rename(generated_path, output_path)  # renomeia para manter nome padronizado no sistema
            return output_path
        else:
            raise FileNotFoundError(f"O arquivo {generated_path} não foi encontrado após a conversão.")
        
    except subprocess.CalledProcessError:
        print("Erro na conversão")
        raise

def convert_img_to_pdf(input_path, output_path):
    with Image.open(input_path) as img:
        if img.mode != 'RGB':
            img = img.convert('RGB')  # garante modo RGB para salvar como PDF corretamente
        img.save(output_path, format='PDF')
