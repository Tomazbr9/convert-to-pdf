from fpdf import FPDF

def text_to_pdf(input_path: str, output_path: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    
    with open(input_path, 'r', encoding='utf-8') as file:
        for line in file:
            pdf.cell(0, 10, line.strip(), ln=True)

    pdf.output(output_path)