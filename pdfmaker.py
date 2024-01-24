import crawler
import pdfkit

# URL of the webpage you want to convert
url = 'https://docs.chia.net/networking-protocol/'

# Path to save the PDF
output_path = 'output.pdf'

# Convert webpage to PDF
pdfkit.from_url(url, output_path)
