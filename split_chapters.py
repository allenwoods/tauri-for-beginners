#!/usr/bin/env python3
"""
按H1标题拆分Markdown文件
将file.md按照一级标题拆分为多个章节文件
"""

import re
import os
from pathlib import Path

def extract_title_from_h1(line):
    """从H1标题行中提取标题文本"""
    # 匹配格式: # **[Title] **
    match = re.match(r'#\s*\*\*\[([^\]]+)\]\s*\*\*', line)
    if match:
        title = match.group(1).strip()
        # 转换为小写，空格替换为连字符
        filename = title.lower().replace(' ', '-')
        return filename
    return None

def is_in_code_block(lines, line_index):
    """检查指定行是否在代码块中"""
    code_block_count = 0
    for i in range(line_index):
        line = lines[i].strip()
        if line.startswith('```'):
            code_block_count += 1
    return code_block_count % 2 == 1

def find_h1_titles(file_path):
    """找到所有H1标题的位置和标题"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    h1_titles = []
    for i, line in enumerate(lines):
        # 检查是否是H1标题格式: # **[Title] **
        if re.match(r'#\s*\*\*\[[^\]]+\]\s*\*\*', line.strip()):
            # 确保不在代码块中
            if not is_in_code_block(lines, i):
                title = extract_title_from_h1(line.strip())
                if title:
                    h1_titles.append((i, title, line.strip()))
    
    return h1_titles, lines

def split_markdown_file(input_file, output_dir):
    """拆分Markdown文件"""
    print(f"正在处理文件: {input_file}")
    
    # 创建输出目录
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 找到所有H1标题
    h1_titles, lines = find_h1_titles(input_file)
    
    print(f"找到 {len(h1_titles)} 个H1标题:")
    for i, (line_num, title, full_line) in enumerate(h1_titles):
        print(f"  {i+1:2d}. {title} (行 {line_num+1})")
    
    # 拆分章节
    for i, (line_num, title, full_line) in enumerate(h1_titles):
        # 确定章节内容范围
        start_line = line_num
        if i + 1 < len(h1_titles):
            end_line = h1_titles[i + 1][0]
        else:
            end_line = len(lines)
        
        # 提取章节内容
        chapter_lines = lines[start_line:end_line]
        chapter_content = ''.join(chapter_lines)
        
        # 生成文件名
        chapter_num = i + 1
        filename = f"{chapter_num:02d}-{title}.md"
        output_file = output_path / filename
        
        # 保存章节文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(chapter_content)
        
        print(f"已保存: {output_file} ({len(chapter_lines)} 行)")

def main():
    """主函数"""
    input_file = "src_md/file.md"
    output_dir = "src_md/chapters"
    
    if not os.path.exists(input_file):
        print(f"错误: 找不到输入文件 {input_file}")
        return
    
    try:
        split_markdown_file(input_file, output_dir)
        print(f"\n拆分完成! 章节文件已保存到: {output_dir}")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == "__main__":
    main()
