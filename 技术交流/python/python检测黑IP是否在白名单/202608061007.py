#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : 202608061007.py
@Author  : 862897316@qq.com
@Time    : 2026/08/06 10:07
@Desc    : 
"""
'''
首先设置黑名单IP和白名单IP的文件
监测黑名单IP是否命中白名单IP的网段交集
如果命中，记录冲突IP
如果未命中，记录正常IP
导出冲突IP和正常IP到文件
'''
from ipaddress import ip_address, ip_network, summarize_address_range

def load_ip_list(file_path):
    """加载IP列表文件，支持三种格式（IPv4 和 IPv6 通用）：
    1. 单个IP：      192.168.1.1        或  ::1
    2. CIDR网段：    192.168.1.0/24     或  2001:db8::/32
    3. 起止IP范围：  192.168.1.1-100    或  2001:db8::1-2001:db8::100
    """
    ip_net_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                if "-" in line:
                    # --- 格式3：起止IP范围 ---
                    start_str, end_str = line.split("-", 1)
                    start_ip = ip_address(start_str.strip())
                    end_ip = ip_address(end_str.strip())
                    if start_ip.version != end_ip.version:
                        print(f"[错误] {line} 起止IP IPv版本不一致")
                        continue
                    sub_nets = list(summarize_address_range(start_ip, end_ip))
                    v = "IPv6" if start_ip.version == 6 else "IPv4"
                    print(f"[解析-{v}] 范围 {line} → {sub_nets}")
                    for net in sub_nets:
                        ip_net_list.append(net)
                else:
                    # --- 格式1 / 2：单个IP 或 CIDR网段 ---
                    net = ip_network(line, strict=False)
                    ip_net_list.append(net)
            except Exception as e:
                print(f"[错误] 无效IP地址 {line} , err:{e}")
    return ip_net_list

def is_ip_in_any_network(check_ip, net_list):
    for net in net_list:
        if net.version != check_ip.version:
            continue
        if check_ip in net:
            return True
    return False

def is_single_ip(net):
    """判断一个 ip_network 是否是单个IP（而非网段）"""
    return net.prefixlen == (32 if net.version == 4 else 128)

if __name__ == "__main__":
    # 黑名单文件
    black_file = "black_ip.txt"
    # 白名单文件
    white_file = "white_ip.txt"

    black_nets = load_ip_list(black_file)
    white_nets = load_ip_list(white_file)

    conflict_records = []   # 冲突记录
    normal_records = []     # 正常（无冲突）记录

    print("=====开始检测黑名单IP是否命中白名单=====")

    for b_net in black_nets:
        hit = False
        b_v = b_net.version  # 4 或 6

        if is_single_ip(b_net):
            # --- 黑名单是单个IP，检测是否落在同版本白名单网段内 ---
            check_ip = b_net.network_address
            for w_net in white_nets:
                if w_net.version != b_v:
                    continue
                if check_ip in w_net:
                    conflict_records.append(
                        f"[单个IP命中网段] 黑名单IP {check_ip} "
                        f"属于白名单网段 {w_net}"
                    )
                    hit = True
                    break
        else:
            # --- 黑名单是网段，检测是否与同版本白名单网段有重叠 ---
            for w_net in white_nets:
                if w_net.version != b_v:
                    continue
                if b_net.overlaps(w_net):
                    overlap_net = b_net.intersection(w_net)
                    conflict_records.append(
                        f"[网段重叠] 黑名单网段 {b_net} "
                        f"与白名单网段 {w_net} 存在交集: {overlap_net}"
                    )
                    hit = True
                    break

        if not hit:
            normal_records.append(str(b_net))

    if conflict_records:
        print(f"\n>>>>>>检测到 {len(conflict_records)} 条冲突:")
        for item in conflict_records:
            print(f"  ❌ {item}")
        with open("ip_conflict_result.txt", "w", encoding="utf-8") as out:
            out.write(f"冲突IP/网段 共 {len(conflict_records)} 条\n")
            out.write("=" * 50 + "\n")
            for c in conflict_records:
                out.write(c + "\n")
        print("\n冲突结果已保存至 ip_conflict_result.txt")
    else:
        print("✅ 未发现黑名单IP存在于白名单，无冲突")

    if normal_records:
        print(f"\n>>>>>>正常IP/网段 共 {len(normal_records)} 条:")
        for item in normal_records:
            print(f"  ✅ {item}")
        with open("ip_normal_result.txt", "w", encoding="utf-8") as out:
            out.write(f"正常IP/网段 共 {len(normal_records)} 条\n")
            out.write("=" * 50 + "\n")
            for n in normal_records:
                out.write(n + "\n")
        print("\n正常结果已保存至 ip_normal_result.txt")