#PDF Merger 07/10/2024

import PyPDF2
from tkinter import Tk, filedialog

def merge_two_pdfs(pdf1, pdf2, output_filename):
    pdf_merger = PyPDF2.PdfMerger()
    
    try:
        pdf_merger.append(pdf1)
        print(f"Added: {pdf1}")
        pdf_merger.append(pdf2)
        print(f"Added: {pdf2}")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
        return
    except PyPDF2.errors.PdfReadError as e:
        print(f"Error reading {e.filename}, it might not be a valid PDF.")
        return

    # Write the merged PDF to the output file
    with open(output_filename, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)
    
    print(f"\nSuccessfully merged '{pdf1}' and '{pdf2}' into '{output_filename}'.")

def select_pdf(title="Select a PDF file"):
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Bring the file dialog to the front

    # Prompt the user to select a single PDF file
    pdf_file = filedialog.askopenfilename(
        title=title,
        filetypes=[("PDF Files", "*.pdf")]
    )
    return pdf_file

def main():
    print("Welcome to the PDF Merger!")
    print("Please select the first PDF file.")
    pdf1 = select_pdf("Select the first PDF file")
    
    if not pdf1:
        print("No PDF file selected. Exiting.")
        return

    print("Please select the second PDF file.")
    pdf2 = select_pdf("Select the second PDF file")
    
    if not pdf2:
        print("No second PDF file selected. Exiting.")
        return

    output_file = input("Enter the name of the output file (e.g., 'merged_output.pdf'): ")

    if not output_file.endswith('.pdf'):
        output_file += '.pdf'

    merge_two_pdfs(pdf1, pdf2, output_file)

if __name__ == "__main__":
    main()
