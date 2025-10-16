#!/usr/bin/env python3
"""
修复Markdown文件中的HTML标签
将HTML标签转换为行内代码格式，但保持代码块中的内容不变
"""

import re
import os
import glob
from pathlib import Path


def find_code_blocks(content):
    """
    找到所有代码块的起止位置
    返回代码块位置列表 [(start, end), ...]
    """
    code_blocks = []
    # 匹配三个反引号包围的代码块
    pattern = r'```[\s\S]*?```'
    
    for match in re.finditer(pattern, content):
        start = match.start()
        end = match.end()
        code_blocks.append((start, end))
    
    return code_blocks


def is_in_code_block(position, code_blocks):
    """
    检查指定位置是否在代码块内
    """
    for start, end in code_blocks:
        if start <= position < end:
            return True
    return False


def is_already_inline_code(text, position):
    """
    检查HTML标签是否已经被转换为行内代码
    检查标签前后是否有反引号
    """
    # 向前查找反引号
    before_pos = position - 1
    while before_pos >= 0 and text[before_pos] in ' \t':
        before_pos -= 1
    
    if before_pos >= 0 and text[before_pos] == '`':
        return True
    
    # 向后查找反引号
    after_pos = position
    while after_pos < len(text) and text[after_pos] not in ' \n\t':
        after_pos += 1
    
    if after_pos < len(text) and text[after_pos] == '`':
        return True
    
    return False


def fix_html_tags_in_content(content):
    """
    修复内容中的HTML标签
    """
    # 找到所有代码块
    code_blocks = find_code_blocks(content)
    
    # 找到所有HTML标签
    html_pattern = r'<[^>]+>'
    matches = list(re.finditer(html_pattern, content))
    
    # 从后往前替换，避免位置偏移
    replacements = []
    
    for match in reversed(matches):
        start = match.start()
        end = match.end()
        tag = match.group()
        
        # 检查是否在代码块内
        if is_in_code_block(start, code_blocks):
            continue
        
        # 检查是否已经是行内代码
        if is_already_inline_code(content, start):
            continue
        
        # 转换为行内代码格式
        new_tag = f'`{tag}`'
        replacements.append((start, end, new_tag))
    
    # 应用替换
    for start, end, new_tag in replacements:
        content = content[:start] + new_tag + content[end:]
    
    return content, len(replacements)


def process_markdown_file(file_path):
    """
    处理单个markdown文件
    """
    try:
        # 读取文件
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 修复HTML标签
        new_content, tag_count = fix_html_tags_in_content(content)
        
        # 如果有修改，保存文件
        if tag_count > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ 处理完成: {file_path} (修复了 {tag_count} 个HTML标签)")
            return tag_count
        else:
            print(f"- 跳过: {file_path} (无需修复)")
            return 0
            
    except Exception as e:
        print(f"✗ 错误: {file_path} - {str(e)}")
        return 0


def main():
    """
    主函数
    """
    print("开始修复Markdown文件中的HTML标签...")
    print("=" * 50)
    
    # 获取所有markdown文件
    chapters_dir = Path("src_md/chapters")
    if not chapters_dir.exists():
        print("错误: src_md/chapters 目录不存在")
        return
    
    # 查找所有markdown文件
    markdown_files = list(chapters_dir.rglob("*.md"))
    
    if not markdown_files:
        print("未找到markdown文件")
        return
    
    print(f"找到 {len(markdown_files)} 个markdown文件")
    print()
    
    # 处理文件
    total_files = 0
    total_tags = 0
    
    for file_path in sorted(markdown_files):
        tag_count = process_markdown_file(file_path)
        if tag_count > 0:
            total_files += 1
            total_tags += tag_count
    
    print()
    print("=" * 50)
    print(f"处理完成!")
    print(f"修改了 {total_files} 个文件")
    print(f"总共修复了 {total_tags} 个HTML标签")


if __name__ == "__main__":
    main()
