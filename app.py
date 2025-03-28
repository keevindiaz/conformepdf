from flask import Flask, render_template, request, send_file
import os
from docx import Document
import pdfkit

app = Flask(__name__)

WKHTMLTOPDF_PATH = os.path.join(os.getcwd(), "bin", "wkhtmltopdf")
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Obtener datos del formulario
    fecha = request.form.get('fecha', '').strip()
    cliente = request.form.get('cliente', '').strip()
    proyecto = request.form.get('proyecto', '').strip()
    trato = request.form.get('trato', '').strip()

    # Cargar la plantilla Word
    doc_path = os.path.join(os.path.dirname(__file__), 'plantilla.docx')
    output_doc_path = "temp.docx"
    output_pdf_path = f"{cliente} - {proyecto} - {trato}.pdf"

    doc = Document(doc_path)

    # Función para reemplazar texto en la plantilla
    def replace_text(doc, old_text, new_text):
        for para in doc.paragraphs:
            for run in para.runs:
                if old_text in run.text:
                    run.text = run.text.replace(old_text, new_text)
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for para in cell.paragraphs:
                        for run in para.runs:
                            if old_text in run.text:
                                run.text = run.text.replace(old_text, new_text)

    # Reemplazar los valores en la plantilla
    replace_text(doc, "{{FECHA}}", fecha)
    replace_text(doc, "{{CLIENTE}}", cliente)
    replace_text(doc, "{{PROYECTO}}", proyecto)
    replace_text(doc, "{{TRATO}}", trato)

    # Guardar el documento actualizado
    doc.save(output_doc_path)

    # Convertir Word a PDF usando pdfkit
    pdfkit.from_file(output_doc_path, output_pdf_path, configuration=config)

    # Enviar el archivo PDF generado
    return send_file(output_pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
