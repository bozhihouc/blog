# -*- coding: utf-8 -*-
import os
from docx2pdf import convert

def docx_to_pdf(docx_path, pdf_path):
    """使用 docx2pdf 将 DOCX 转换为 PDF"""
    if os.path.exists(pdf_path):
        return 'skip', os.path.basename(docx_path)
    
    try:
        convert(docx_path, pdf_path)
        return 'success', os.path.basename(docx_path)
    except Exception as e:
        return 'failed', (os.path.basename(docx_path), str(e))

def batch_convert_to_pdf(input_directory, output_directory):
    """批量转换 DOCX 文件为 PDF"""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    docx_files = [f for f in os.listdir(input_directory) if f.endswith(".docx")]
    total = len(docx_files)
    
    if total == 0:
        print(f"在目录 {input_directory} 中未找到 DOCX 文件")
        return
    
    print(f"找到 {total} 个 DOCX 文件，开始转换...\n")

    success_count = 0
    failed_count = 0
    skip_count = 0
    
    for current, filename in enumerate(docx_files, 1):
        docx_path = os.path.join(input_directory, filename)
        pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
        pdf_path = os.path.join(output_directory, pdf_filename)
        
        status, info = docx_to_pdf(docx_path, pdf_path)
        
        if status == 'success':
            success_count += 1
            print(f"[{current}/{total}] ✓ 转换成功: {info}")
        elif status == 'skip':
            skip_count += 1
            print(f"[{current}/{total}] ⊙ 跳过已存在: {info}")
        else:
            failed_count += 1
            fname, error = info
            print(f"[{current}/{total}] ✗ 转换失败: {fname} - {error}")

    print(f"\n{'='*50}")
    print(f"转换完成！")
    print(f"总计: {total} 个文件")
    print(f"成功: {success_count}")
    print(f"跳过: {skip_count}")
    print(f"失败: {failed_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    input_directory = r"C:\Users\jingshuai\Desktop\日报测试\2025-07-31份"
    output_directory = r"C:\Users\jingshuai\Desktop\日报测试\PDF"

    batch_convert_to_pdf(input_directory, output_directory)
