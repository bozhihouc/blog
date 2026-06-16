我来为这个脚本创建一个README文档。

```markdown
# Python绿盟RSAS端口信息提取工具

## 项目简介

这是一个用于批量提取绿盟RSAS（远程安全评估系统）扫描报告中端口信息的Python工具。该工具可以从多个Excel格式的扫描报告中，自动提取指定sheet中的端口数据，并整合成统一的格式输出。

## 功能特性

- ✅ 批量处理多个.xls格式的扫描报告文件
- ✅ 自动从文件名中提取IP地址
- ✅ 智能定位"远程端口信息"和"安装软件信息"之间的数据区域
- ✅ 在提取的数据中自动添加IP列
- ✅ 将结果导出为TAB分隔的文本文件，方便导入Excel查看
- ✅ 实时显示处理进度和数据预览

## 环境要求

- Python 3.6+
- xlrd库

## 安装依赖

```
bash
pip install xlrd
```
## 使用方法

### 1. 准备数据

将所有需要处理的主机报表`.xls`文件放入 `xls_all` 文件夹中。

文件命名建议包含IP地址，例如：
- `x.x.x.x.xls`
- `x.x.x.x.xls`
- `x.x.x.x.xls`

### 2. 运行脚本

```
bash
python 20260060160835.py
```
### 3. 查看结果

脚本执行完成后，会在当前目录生成 `端口信息提取结果.txt` 文件，包含所有提取的数据。

## 配置说明

### 修改Sheet索引

如果需要提取其他sheet的数据，可以修改代码中的 `sheet_index` 参数：

```
python
# 默认提取第5个sheet（索引为4）
all_data = batch_process_xls_files(xls_dir, sheet_index=4, output_file="端口信息提取结果.txt")
```
### 修改输出文件名

```
python
all_data = batch_process_xls_files(xls_dir, sheet_index=4, output_file="自定义输出文件名.txt")
```
## 输出格式

输出的文本文件采用TAB分隔，第一列为IP地址，后续列为原始Excel中的数据列。可以直接用Excel打开进行查看和分析。

示例：
```

IP	端口	协议	状态	服务	...
x.x.x.x	80	TCP	open	http	...
x.x.x.x	443	TCP	open	https	...
x.x.x.x	22	TCP	open	ssh	...
```
## 注意事项

1. **Excel格式**：仅支持`.xls`格式（Excel 97-2003），不支持`.xlsx`格式
2. **Sheet结构**：确保目标sheet中包含"远程端口信息"和"安装软件信息"标记
3. **编码问题**：如果读取失败，可能是文件编码问题，建议确认文件为标准的xls格式
4. **空数据处理**：脚本会自动跳过空行和无法识别的文件

## 常见问题

### Q: 提示找不到xlrd模块？
A: 运行 `pip install xlrd` 安装依赖库。

### Q: 提取的数据为空？
A: 检查以下几点：
- 确认sheet索引是否正确（索引从0开始）
- 确认文件中包含"远程端口信息"和"安装软件信息"标记
- 确认标记在第一列（A列）

### Q: 如何提取其他位置的数据？
A: 修改 `extract_port_info` 函数中的标记查找逻辑，调整 `start_row` 和 `end_row` 的定位条件。

## 作者

862897316@qq.com

## 更新时间

2026/06/16

## 许可证

本工具仅供学习和内部使用。
```


这个README包含了项目的完整说明、使用方法、配置选项和常见问题解答。你可以根据实际需求进行调整。