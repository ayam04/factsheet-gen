from json2pdf_converter import generate
import json

options = {
    'encoding': 'UTF-8',
    'margin-top': '0px',
    'margin-right': '30px',
    'margin-bottom': '30px',
    'margin-left': '30px',
    'footer-right': "Page [page] of [topage]",
    'footer-font-size': "9",
    'orientation': 'Portrait',
    'page-size': 'A4',
}

data_variables = {
    "data": "data"
}

def add_content1(function1, name):
    print(function1, name)
    return f"AddedByFunction+{name}"
def add_content2(function2, age):
    return f"AddedByFunction+{age}"

custom_filter_functions = [ add_content1, add_content2 ]

template_directory = r'template'
template_name = "test.html"
output_html_path = r'results/output.html'
new_pdf_path = r'results/output.pdf'

generate(
    # json_file_path= json_file_path, 
    template_directory_path= template_directory, 
    output_html_path=output_html_path, 
    output_pdf_path=new_pdf_path, 
    options=options,
    template_name=template_name,
    data_variables=data_variables,
    custom_filter_functions=custom_filter_functions
)