import PyPDF2

input_file = 'tarak rupesh.pdf'
output_file = 'tarakResume.pdf'
page_number_to_remove = 1  # Index starts from 0

with open(input_file, 'rb') as file:
    pdf = PyPDF2.PdfReader(file)
    output_pdf = PyPDF2.PdfWriter()

    num_pages = len(pdf.pages)

    for page_number in range(num_pages):
        if page_number != page_number_to_remove:
            page = pdf.pages[page_number]
            output_pdf.add_page(page)

    with open(output_file, 'wb') as output:
        output_pdf.write(output)
