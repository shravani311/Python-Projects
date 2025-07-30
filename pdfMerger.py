#install PyPDF2 using :- pip install PyPDF2
import PyPDF2
import os

def merge_pdfs(pdf_list, output_file):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf = pdf.strip()
        if not pdf.lower().endswith('.pdf'):
            print(f"Skipping non-PDF file: {pdf}")
            continue
        if not os.path.isfile(pdf):
            print(f"File not found: {pdf}")
            continue

        try:
            with open(pdf, 'rb') as f:
                merger.append(f)
            print(f"Added: {pdf}")
        except Exception as e:
            print(f"Error adding {pdf}: {e}")

    try:
        with open(output_file, 'wb') as f_out:
            merger.write(f_out)
        print(f"\nSuccessfully merged into: {output_file}")
    except Exception as e:
        print(f"Failed to write merged PDF: {e}")
    finally:
        merger.close()

def main():
    print("PDF Merger Tool")
    file_input = input("Enter PDF file paths separated by commas:\n> ")
    pdf_files = file_input.split(',')

    output_filename = input("Enter name for merged PDF (e.g., merged.pdf): ").strip()
    if not output_filename.endswith('.pdf'):
        output_filename += '.pdf'

    merge_pdfs(pdf_files, output_filename)

if __name__ == "__main__":
    main()
