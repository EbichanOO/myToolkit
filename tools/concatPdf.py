import PyPDF2

def ConcatPdfTwo(A_pdf_path1, A_pdf_path2, out_path_and_name):
    merger = PyPDF2.PdfFileMerger()
    merger.append(A_pdf_path1)
    merger.append(A_pdf_path2)
    merger.setPageLayout("/SinglePage")
    merger.write(out_path_and_name)
    merger.close()

def ConcatPdfSome(pdf_paths, out_path_and_name):
    merger = PyPDF2.PdfFileMerger()
    for A_pdf_path in pdf_paths:
        merger.append(A_pdf_path)
    merger.setPageLayout("/SinglePage")
    merger.write(out_path_and_name)
    merger.close()

if __name__ == '__main__':
    ConcatPdfSome(["./tmps/A.pdf", "./tmps/B.pdf", "./tmps/C.pdf"], "./tmps/D.pdf")