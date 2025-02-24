import google.generativeai as genai
from . import api_prompt
from .api_settings import model
from ..models import SpeakingBook

# Path to the PDF file in the 'files' folder
file_path_C_1 = "./pdf/SpeakingC-1.pdf"
file_path_C_2 = "./pdf/SpeakingC-2.pdf"
file_path_C_3 = "./pdf/SpeakingC-3.pdf"
file_path_C_4 = "./pdf/SpeakingC-4.pdf"


# Day 1/ page 3( Part/Whole - Body parts,), 4-5( Concept Application )
def call_api():
    # C - 1
    file_C_1 = genai.upload_file(path=file_path_C_1, display_name="Speaking C - 1")
    print(f"Uploaded file '{file_C_1.display_name}' as: {file_C_1.uri}")
    response = model.generate_content([file_C_1, api_prompt.prompt_C_1])
    raw_tables_C_1 = divide_texts(response)

    # C - 2
    file_C_2 = genai.upload_file(path=file_path_C_2, display_name="Speaking C - 2")
    print(f"Uploaded file '{file_C_2.display_name}' as: {file_C_2.uri}")
    response = model.generate_content([file_C_1, api_prompt.prompt_C_2])
    raw_tables_C_2 = divide_texts(response)

    # C - 3
    file_C_3 = genai.upload_file(path=file_path_C_3, display_name="Speaking C - 3")
    print(f"Uploaded file '{file_C_3.display_name}' as: {file_C_3.uri}")
    response = model.generate_content([file_C_3, api_prompt.prompt_C_3])
    raw_tables_C_3 = divide_texts(response)

    # C - 4
    file_C_4 = genai.upload_file(path=file_path_C_4, display_name="Speaking C - 4")
    print(f"Uploaded file '{file_C_4.display_name}' as: {file_C_4.uri}")
    response = model.generate_content([file_C_4, api_prompt.prompt_C_4])
    raw_tables_C_4 = divide_texts(response)


    raw_tables = raw_tables_C_1 + raw_tables_C_2 + raw_tables_C_3 + raw_tables_C_4

    tables = []

    for raw_table in raw_tables:
        if len(raw_table) == 0: continue
        tables.append(raw_table)
    # Print the generated content
    return tables

def generate_table(filepath):
    file = genai.upload_file(path=filepath, display_name="SpeakingC")
    print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    response = model.generate_content([filepath, api_prompt.prompt_C_4])
    raw_tables = divide_texts(response)
    return raw_tables



def divide_texts(response):
    tables = response.text.split("\n")
    print('tables: ' + str(tables))
    return tables