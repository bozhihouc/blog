# -*- coding: utf-8 -*-
import os
from docx import Document
from docx2pdf import convert

def docx_to_pdf(docx_path, pdf_path):
    try:
        convert(docx_path, pdf_path)
        print(f"转换成功: {docx_path} -> {pdf_path}")
    except Exception as e:
        print(f"转换失败: {docx_path} -> {pdf_path}, 错误信息: {str(e)}")

def batch_convert_to_pdf(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".docx"):
            docx_path = os.path.join(input_directory, filename)
            pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
            pdf_path = os.path.join(output_directory, pdf_filename)
            docx_to_pdf(docx_path, pdf_path)

if __name__ == "__main__":
    input_directory = r"C:\Users\songjingshuai\Desktop\转换测试\2023下半年复测报告"
    output_directory = r"C:\Users\songjingshuai\Desktop\转换测试\03"

    batch_convert_to_pdf(input_directory, output_directory)
