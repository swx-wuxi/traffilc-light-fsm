# # 看一下编译的时候内存的大小，便于程序优化



# # 各个内存区段的占用情况（单位：字节）
# # text: 程序代码  data: 初始化的全局变量  bss: 未初始化全局变量 heap: 动态内存分配
# sections = {'text': 10240, 'data': 512, 'bss': 2048, 'heap': 4096}

# # 绘制柱状图
# plt.bar(sections.keys(), sections.values(), color='skyblue')
# plt.ylabel('Bytes')
# plt.title('Memory Usage Distribution')

# # 显示图表
# plt.show()

import re
import matplotlib.pyplot as plt

def parse_map_file(filename):
    with open(filename) as f:
        content = f.read()
    sections = {}
    for sec in ['.text', '.data', '.bss', '.heap']:
        match = re.search(rf'{sec}\s+0x([0-9A-Fa-f]+)\s+0x([0-9A-Fa-f]+)', content)
        if match:
            start = int(match.group(1), 16)   # 起始地址（十六进制 → 十进制）
            size = int(match.group(2), 16)    # 大小（十六进制 → 十进制）
            sections[sec] = {"start": start, "size": size}
    return sections

sections = parse_map_file("Week2/input_files/hw5_part1_sample.map")
# print("Memory layout:", sections)
# 绘制柱状图
names = list(sections.keys())
sizes = [info["size"] for info in sections.values()]

plt.bar(names, sizes, color='skyblue')
plt.ylabel('Bytes')
plt.title('Memory Usage Distribution')

# 显示图表
plt.show()
