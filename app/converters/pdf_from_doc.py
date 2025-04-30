import subprocess
import os

def doc_to_pdf(input_path, output_path):
    input_path = os.path.abspath(input_path)
    output_dir = os.path.dirname(os.path.abspath(output_path))

    try:
        subprocess.run([
            "soffice",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            input_path
        ], check=True)

        # Soffice gera com mesmo nome do input
        generated_name = os.path.splitext(os.path.basename(input_path))[0] + ".pdf"
        generated_path = os.path.join(output_dir, generated_name)

        # Renomeia ou move para o nome correto (output_path)
        if os.path.exists(generated_path):
            os.rename(generated_path, output_path)
            return output_path
        else:
            raise FileNotFoundError(f"O arquivo {generated_path} não foi encontrado após a conversão.")
        
    except subprocess.CalledProcessError:
        print("Erro na conversão com LibreOffice.")
        raise
