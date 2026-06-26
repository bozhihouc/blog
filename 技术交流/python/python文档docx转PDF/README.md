```markdown
# DOCX 转 PDF 批量转换工具

## 📝 项目简介

一个简单易用的批量 DOCX 转 PDF 工具，支持进度显示和文件去重，适用于 Windows 系统。

## ✨ 功能特性

- ✅ 批量转换文件夹中的所有 DOCX 文件
- ✅ 实时显示转换进度 `[当前/总数]`
- ✅ 自动跳过已存在的 PDF 文件（避免重复转换）
- ✅ 详细的统计报告（成功/跳过/失败）
- ✅ 友好的状态图标（✓ ⊙ ✗）

## 📋 依赖要求

- Python 3.6+
- Windows 操作系统（需要安装 Microsoft Word）
- docx2pdf 库

## 🔧 安装步骤

### 1. 安装依赖库

```
bash
pip install docx2pdf
```
### 2. 确认 Microsoft Word 已安装

本工具依赖 Microsoft Word 进行转换，请确保系统已安装 Office 2010 或更高版本。

## 🚀 使用方法

### 基本使用

1. 编辑脚本中的输入输出路径：

```
python
if __name__ == "__main__":
    input_directory = r"C:\Users\你的用户名\Desktop\DOCX文件夹"
    output_directory = r"C:\Users\你的用户名\Desktop\PDF输出文件夹"
    
    batch_convert_to_pdf(input_directory, output_directory)
```
2. 运行脚本：

```
bash
python 02-docx转pdf.py
```
## ⚡ 性能优化（可选）

如果需要更快的转换速度，可以使用多线程版本。修改脚本添加以下依赖：

```
bash
pip install pywin32
```
然后在代码开头添加：

```
python
import pythoncom
from concurrent.futures import ThreadPoolExecutor
```
**注意**：多线程版本需要在每个线程中初始化 COM：

```
python
def docx_to_pdf(docx_path, pdf_path):
    try:
        pythoncom.CoInitialize()  # 初始化 COM
        if os.path.exists(pdf_path):
            return 'skip', os.path.basename(docx_path)
        convert(docx_path, pdf_path)
        return 'success', os.path.basename(docx_path)
    except Exception as e:
        return 'failed', (os.path.basename(docx_path), str(e))
    finally:
        pythoncom.CoUninitialize()  # 释放 COM
```
## ❓ 常见问题

### Q1: 提示 "尚未调用 CoInitialize" 错误？

**A**: 这是多线程环境下的 COM 初始化问题，请参考上方"性能优化"部分添加 `pythoncom.CoInitialize()`。

### Q2: 转换速度慢？

**A**: 
- 单个文件转换通常需要 1-3 秒
- 可以使用多线程版本提升速度（见上方优化方案）
- 确保没有其他程序占用 Word

### Q3: 转换失败怎么办？

**A**:
- 检查 DOCX 文件是否损坏（尝试用 Word 打开）
- 确保文件没有被其他程序占用
- 检查输出目录是否有写入权限

### Q4: 如何跳过已转换的文件？

**A**: 脚本已内置此功能，如果 PDF 文件已存在会自动跳过。如需重新转换，请先删除对应的 PDF 文件。

## 📂 目录结构

```

python文档docx转PDF/
├── 02-docx转pdf.py      # 主脚本
└── README.md             # 说明文档
```
## 📄 许可证

本脚本仅供学习和个人使用。

## 📮 反馈与建议

如有问题或建议，欢迎提出！

---

**最后更新**: 2026-06-26
```
