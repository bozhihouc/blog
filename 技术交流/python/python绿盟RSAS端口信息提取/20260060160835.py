#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 20260060160835.py
@Author  : 862897316@qq.com
@Time    : 2026/06/16 08:35
@Desc    : 
"""
import xlrd
import os
import re


def extract_ip_from_filename(filename):
    """从文件名中提取IP地址"""
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    match = re.search(ip_pattern, filename)
    if match:
        return match.group()
    return None


def extract_port_info(file_path, sheet_index=4):
    """提取远程端口信息到安装软件信息之间的数据"""
    try:
        workbook = xlrd.open_workbook(file_path)
        sheet_names = workbook.sheet_names()
        
        if sheet_index >= len(sheet_names):
            print(f"错误: 索引{sheet_index}超出范围,该文件只有{len(sheet_names)}个sheet")
            return []
        
        sheet_name = sheet_names[sheet_index]
        sheet = workbook.sheet_by_name(sheet_name)
        
        # 从文件名提取IP
        filename = os.path.basename(file_path)
        ip_address = extract_ip_from_filename(filename)
        
        # 查找"远程端口信息"和"安装软件信息"的行号
        start_row = None
        end_row = None
        
        for row_idx in range(sheet.nrows):
            first_cell_value = str(sheet.cell_value(row_idx, 0)).strip()
            
            if "远程端口信息" in first_cell_value and start_row is None:
                start_row = row_idx
            
            if "安装软件信息" in first_cell_value and end_row is None:
                end_row = row_idx
                break
        
        if start_row is None:
            print(f"警告: {filename} 未找到 '远程端口信息' 标记")
            return []
        
        if end_row is None:
            end_row = sheet.nrows
        
        # 提取数据(不包含起始和结束标记行)
        data_start = start_row + 1
        data_end = end_row
        
        extracted_data = []
        
        # 获取表头,在最前面添加IP列
        if data_start < sheet.nrows:
            headers = ["IP"]
            
            for col_idx in range(sheet.ncols):
                header_value = sheet.cell_value(data_start, col_idx)
                headers.append(str(header_value).strip())
            
            # 提取数据行(跳过表头)
            for row_idx in range(data_start + 1, data_end):
                row_data = [ip_address]
                
                for col_idx in range(sheet.ncols):
                    cell_value = sheet.cell_value(row_idx, col_idx)
                    value_str = str(cell_value).strip()
                    row_data.append(value_str)
                
                # 只添加非空行
                if any(v for v in row_data[1:] if v):
                    extracted_data.append(row_data)
        
        return extracted_data
        
    except Exception as e:
        print(f"读取文件 {os.path.basename(file_path)} 失败: {e}")
        return []


def batch_process_xls_files(xls_dir, sheet_index=4, output_file="提取结果.txt"):
    """批量处理所有xls文件"""
    xls_files = [f for f in os.listdir(xls_dir) if f.endswith('.xls')]
    
    if not xls_files:
        print("未找到xls文件")
        return
    
    print("=" * 80)
    print(f"开始批量处理 {len(xls_files)} 个文件")
    print("=" * 80)
    
    all_data = []
    headers = None
    
    for idx, filename in enumerate(sorted(xls_files), 1):
        file_path = os.path.join(xls_dir, filename)
        print(f"\n[{idx}/{len(xls_files)}] 处理文件: {filename}")
        
        data = extract_port_info(file_path, sheet_index)
        
        if data:
            print(f"  提取到 {len(data)} 条数据")
            if headers is None and len(data) > 0:
                # 第一条数据的长度作为参考
                headers = ["IP"] + [f"列{i+1}" for i in range(len(data[0]) - 1)]
            all_data.extend(data)
        else:
            print(f"  未提取到数据")
    
    print("\n" + "=" * 80)
    print(f"批量处理完成! 共提取 {len(all_data)} 条数据")
    print("=" * 80)
    
    # 保存结果到文件
    if all_data:
        output_path = os.path.join(os.path.dirname(__file__), output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            # 写入表头
            if headers:
                f.write('\t'.join(headers) + '\n')
            
            # 写入数据
            for row in all_data:
                f.write('\t'.join(row) + '\n')
        
        print(f"\n结果已保存到: {output_path}")
        
        # 显示前几条数据预览
        print("\n数据预览 (前5条):")
        print("-" * 80)
        if headers:
            print('\t'.join(headers))
            print("-" * 80)
        
        for row in all_data[:5]:
            print('\t'.join(row))
        
        if len(all_data) > 5:
            print(f"... 还有 {len(all_data) - 5} 条数据 ...")
    
    return all_data


if __name__ == "__main__":
    # xls_all文件夹路径
    xls_dir = os.path.join(os.path.dirname(__file__), "xls_all")
    
    # 批量处理所有文件,提取第5个sheet (索引为4)的数据
    all_data = batch_process_xls_files(xls_dir, sheet_index=4, output_file="端口信息提取结果.txt")
