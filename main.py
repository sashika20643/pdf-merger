from flask import Flask, render_template, request, redirect, send_file
import PyPDF2
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    # Get uploaded files
    uploaded_files = request.files.getlist('pdf_files')

    merger = PyPDF2.PdfMerger()
    for file in uploaded_files:
        merger.append(file)

    # Generate unique filename for merged PDF
    output_filename = 'merged.pdf'
    i = 1
    while os.path.exists(output_filename):
        output_filename = f'merged_{i}.pdf'
        i += 1

    # Write merged PDF to disk
    merger.write(output_filename)
    merger.close()

    # Return merged PDF for download
    return send_file(output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

