"""PDF File Splitter."""
# https://stackoverflow.com/questions/490195/split-a-multi-page-pdf-file-into-multiple-pdf-files-with-python
# https://stackoverflow.com/questions/14209214/reading-the-pdf-properties-metadata-in-python
# https://stackoverflow.com/questions/59909520/extracting-the-keywords-from-pdf-metadata-in-python
import os
import sys

from PyPDF2 import PdfFileReader, PdfFileWriter


def pdf_splitter(path, output_dir):
    """PDF File Splitter.

    Args:
        path (str): Full path to pdf file name to split.
        output_dir (str): Full path to output dir for generate the pdf splitted.
    """
    pdf = PdfFileReader(path)

    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        pdf_writer.addMetadata(
            {
                "/Author": "Ruben Dario Romero Chica, Comunidad Scrum LATAM",
                "/Creator": "Leonardo J. Caballero G.",
                "/Producer": "Indico Software, PyPDF2 (Debian GNU/Linux 10)",
                "/Subject": "First National Technology Congress from ACME Corporation",
                "/Title": "Certificate of Assistance to the First National Technology Congress from ACME Corporation",
                "/Keywords": "Anniversary, Event, ACME Corporation",
            }
        )

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
            print("Output Directory Created.")

        filename = os.path.basename(path)[0:-4]

        output_filename = '{}/{}_page_{}.pdf'.format(output_dir, filename, page+1)

        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(output_filename))

if __name__ == "__main__":

    # Security check, run only if 2 arguments are actually received
    if len(sys.argv) == 3:
        file = str(sys.argv[1])
        splitted_pdf_dir = str(sys.argv[2])
        pdf_splitter(file, splitted_pdf_dir)
    else:
        print("ERROR: Entered one (1) or more than two (2) arguments")
        print("SOLUTION: Enter the arguments correctly")
        print('Example: python pdf_splitter.py "file_name.pdf" "pdfs"')
