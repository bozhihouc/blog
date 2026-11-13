#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 202609101133.py
@Author  : 862897316@qq.com
@Time    : 2026/09/10 11:33
@Desc    : 
"""
'''
在修复漏洞时经常需要打开html对获取到的2.1的漏洞概述中的banner信息进行分析，
文件过大时加载过慢，采用python读取主机报表的2.1章节，获取banner信息中的版本号。
'''
from bs4 import BeautifulSoup
import csv
import json
import os
import re

def parse_html_file(html_path):
    """解析单个ip.html，返回漏洞列表"""
    results = []
    if not os.path.exists(html_path):
        print(f"[WARN] 文件不存在: {html_path}")
        return results

    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    # 新版JS单页报表：数据在 <script>window.data=...</script> 的JSON中，优先解析
    json_results = parse_html_json(html_path)
    if json_results:
        return json_results

    vul_table = soup.find("table", id="vuln_list")
    if not vul_table:
        print(f"[WARN] 未找到旧版漏洞表格，尝试新版解析 {html_path}")
        return parse_html_v2(soup, html_path)

    tbody = vul_table.find("tbody")
    rows = tbody.find_all("tr", class_="even")
    for tr in rows:
        port_td = tr.find("td", class_="vul_port")
        if not port_td:
            continue
        port = port_td.get_text(strip=True)
        tds = tr.find_all("td")
        if len(tds) < 5:
            continue
        protocol = tds[1].get_text(strip=True)
        service = tds[2].get_text(strip=True)
        vul_td = tds[3]
        protect_td = tds[4]

        vul_items = vul_td.find_all("div", class_="vul_summary")
        protect_items = protect_td.find_all("li")

        for idx, vul_div in enumerate(vul_items):
            # 漏洞名称
            vul_name_span = vul_div.find("span")
            vul_name = vul_name_span.get_text(strip=True) if vul_name_span else ""
            # 提取CVE编号，正则匹配 CVE-数字-数字
            cve_pattern = re.compile(r"CVE-\d{4}-\d+")
            cve_match = cve_pattern.search(vul_name)
            cve_id = cve_match.group() if cve_match else ""
            # 版本详情
            detail_div = vul_div.find("div", class_="detail")
            version_info = detail_div.get_text(strip=True) if detail_div else ""
            # 漏洞等级：判断图片文件名
            img_tag = vul_div.find("img", {"src": lambda x: "vuln_" in x})
            level = "未知"
            if img_tag:
                src = img_tag["src"]
                if "vuln_high.gif" in src:
                    level = "高危"
                elif "vuln_medium.gif" in src:
                    level = "中危"
                elif "vuln_low.gif" in src:
                    level = "低危"
                elif "vuln_info.gif" in src:
                    level = "信息"

            # NF已防护
            protect_status = "-"
            if idx < len(protect_items):
                protect_status = protect_items[idx].get_text(strip=True)

            results.append({
                "ip": os.path.basename(html_path).replace(".html", ""),
                "port": port,
                "protocol": protocol,
                "service": service,
                "vul_name": vul_name,
                "cve_id": cve_id,
                "level": level,
                "version": version_info,
                "nf_protect": protect_status
            })
    return results


def parse_html_v2(soup, html_path):
    """解析新版RSAS主机报表(vulnOverview结构)，返回漏洞列表"""
    results = []
    overview_list = soup.find_all("div", class_="vulnOverview")
    if not overview_list:
        print(f"[WARN] 未找到新版漏洞表格 {html_path}")
        return results

    for overview in overview_list:
        table = overview.find("table")
        if not table:
            continue
        tbody = table.find("tbody")
        if not tbody:
            continue
        rows = tbody.find_all("tr", class_=lambda c: c and "ant-table-row" in c)
        for tr in rows:
            tds = tr.find_all("td", class_="ant-table-cell")
            if len(tds) < 5:
                continue
            port = tds[0].get_text(strip=True)
            protocol = tds[1].get_text(strip=True)
            service = tds[2].get_text(strip=True)
            vul_td = tds[3]
            protect_td = tds[4]

            vul_items = vul_td.find_all("div", class_="vulnItem")
            protect_items = protect_td.find_all("li")

            for idx, vul_div in enumerate(vul_items):
                # 漏洞名称：在 div.title 下的 span
                title_div = vul_div.find("div", class_="title")
                vul_name_span = title_div.find("span") if title_div else None
                vul_name = vul_name_span.get_text(strip=True) if vul_name_span else ""
                # 提取CVE编号
                cve_pattern = re.compile(r"CVE-\d{4}-\d+")
                cve_match = cve_pattern.search(vul_name)
                cve_id = cve_match.group() if cve_match else ""
                # 版本详情
                detail_div = vul_div.find("div", class_="detail")
                version_info = detail_div.get_text(strip=True) if detail_div else ""
                # 漏洞等级：新版等级图片为 .levelImg（high_zh/mid_zh/low_zh svg）
                img_tag = vul_div.find("img", class_="levelImg")
                level = "未知"
                if img_tag:
                    src = img_tag.get("src", "")
                    if "high_" in src:
                        level = "高危"
                    elif "mid_" in src:
                        level = "中危"
                    elif "low_" in src:
                        level = "低危"
                    elif "info_" in src:
                        level = "信息"

                # NF已防护
                protect_status = "-"
                if idx < len(protect_items):
                    protect_status = protect_items[idx].get_text(strip=True)

                results.append({
                    "ip": os.path.basename(html_path).replace(".html", ""),
                    "port": port,
                    "protocol": protocol,
                    "service": service,
                    "vul_name": vul_name,
                    "cve_id": cve_id,
                    "level": level,
                    "version": version_info,
                    "nf_protect": protect_status
                })
    return results


def parse_html_json(html_path):
    """解析新版JS单页RSAS报表：数据在 <script>window.data=...</script> 的JSON中"""
    results = []
    if not os.path.exists(html_path):
        return results
    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    m = re.search(r"window\.data\s*=\s*\{", content)
    if not m:
        return results
    try:
        start = content.index("{", m.start())
        data, _ = json.JSONDecoder().raw_decode(content[start:])
    except Exception:
        return results

    ip = os.path.basename(html_path).replace(".html", "")
    level_map = {"high": "高危", "middle": "中危", "low": "低危", "info": "信息"}

    def handle_items(items):
        if not isinstance(items, list):
            return
        for it in items:
            if not isinstance(it, dict):
                continue
            port = it.get("port", "")
            service = it.get("service", "")
            protocol = it.get("protocol", "")
            for vul in it.get("vuls") or []:
                if not isinstance(vul, dict):
                    continue
                vm = vul.get("vul_msg") or {}
                level_raw = str(vul.get("vul_level", "") or "").lower()
                results.append({
                    "ip": ip,
                    "port": port,
                    "protocol": protocol,
                    "service": service,
                    "vul_name": vm.get("i18n_name") or "",
                    "cve_id": vm.get("cve_id") or "",
                    "level": level_map.get(level_raw, level_raw or "未知"),
                    "version": "\n".join(vul.get("mess_string") or []),
                    "nf_protect": vul.get("if_defend", "-")
                })

    def walk(cats):
        if not isinstance(cats, list):
            return
        for cat in cats:
            if not isinstance(cat, dict):
                continue
            d = cat.get("data")
            if isinstance(d, dict):
                if "vul_info" in d and isinstance(d["vul_info"], dict):
                    handle_items(d["vul_info"].get("vul_items"))
                if isinstance(d.get("vul_items"), list):
                    handle_items(d["vul_items"])
            walk(cat.get("children"))

    if isinstance(data, dict):
        walk(data.get("categories"))
    return results


def main():
    # ===================== 这里修改配置 =====================
    ip_file = "name.txt"          # ip清单文件，放在脚本同目录
    #html_dir = "./html_reports"   # html存放目录，修改成你的目录
    html_dir = r"C:\Users\222\host"  # html存放目录，修改成你的目录
    out_csv = "scan_result.csv"   # 输出csv结果文件
    # =======================================================

    all_data = []
    unique_key_set = set() # 用于去重，存放已经见过的唯一主键

    if not os.path.exists(ip_file):
        print(f"[ERROR] 找不到{ip_file}，请把name.txt放在脚本同目录！")
        return

    # html目录不存在则提示
    if not os.path.isdir(html_dir):
        print(f"[ERROR] html目录不存在：{html_dir}")
        return

    with open(ip_file, "r", encoding="utf-8") as f:
        ip_lines = [line.strip() for line in f if line.strip()]

    for ip in ip_lines:
        html_filename = f"{ip}.html"
        html_full_path = os.path.join(html_dir, html_filename)
        print(f"[PROCESS] 正在解析 {html_full_path}")
        vul_list = parse_html_file(html_full_path)
        for vul in vul_list:
            # 复合唯一键：ip+端口+漏洞名称+CVE，相同则判定为重复漏洞
            unique_key = (vul["ip"], vul["port"], vul["vul_name"], vul["cve_id"])
            if unique_key not in unique_key_set:
                unique_key_set.add(unique_key)
                all_data.append(vul)
            else:
                print(f"[SKIP 重复] {vul['ip']}:{vul['port']} {vul['vul_name']}")

    # 写入csv，新增CVE字段
    headers = ["IP", "端口", "协议", "服务", "漏洞名称", "CVE编号", "漏洞等级", "版本信息", "NF已防护"]
    with open(out_csv, "w", encoding="utf-8-sig", newline="") as csvf:
        writer = csv.DictWriter(csvf, fieldnames=headers)
        writer.writeheader()
        for row in all_data:
            writer.writerow({
                "IP": row["ip"],
                "端口": row["port"],
                "协议": row["protocol"],
                "服务": row["service"],
                "漏洞名称": row["vul_name"],
                "CVE编号": row["cve_id"],
                "漏洞等级": row["level"],
                "版本信息": row["version"],
                "NF已防护": row["nf_protect"]
            })
    print(f"\n[FINISH] 解析完成！总有效漏洞条目：{len(all_data)}，输出文件：{out_csv}")


if __name__ == "__main__":
    main()