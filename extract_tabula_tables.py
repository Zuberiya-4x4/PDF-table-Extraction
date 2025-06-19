import tabula
import os

# List of full file paths to your PDFs
pdf_types = {
    "sample_table_1.pdf": "table",
    "sample-invoice.pdf": "invoice",
    "statement_sample1.pdf": "statement",
    "fs023-sample-financial-statements.pdf": "financial-statement",
    "EDIT OoPdfFormExample.pdf": "forms"
}

# List of actual PDF file paths
pdfs = [
    r"C:\Users\SyedaZuberiya\Downloads\sample_table_1.pdf",
    r"C:\Users\SyedaZuberiya\Downloads\sample-invoice.pdf",
    r"C:\Users\SyedaZuberiya\Downloads\fs023-sample-financial-statements.pdf",
    r"C:\Users\SyedaZuberiya\Downloads\dummy_statement.pdf",
    r"C:\Users\SyedaZuberiya\Downloads\EDIT OoPdfFormExample.pdf"
]

# Output directory for CSVs
output_directory = "extracted_tabula_tables"
os.makedirs(output_directory, exist_ok=True)

# Loop through each PDF
for pdf in pdfs:
    filename = os.path.basename(pdf)  # e.g., sample_table_1.pdf
    # Extract all tables from all pages
    tables = tabula.read_pdf(pdf, pages='all', multiple_tables=True)

    # Save each extracted table as a separate CSV
    for i, table in enumerate(tables):
        out_path = os.path.join(output_directory, f"tabula_{filename[:-4]}_t{i+1}.csv")
        table.to_csv(out_path, index=False)

print("Table extraction complete.")