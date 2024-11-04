'''
CharacterTextSplitter,RecursiveCharacterTextSplitter分块
'''
import json
from langchain_text_splitters.character import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)
# 定义函数来读取 .md 文件
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 定义函数来将分割后的内容保存为 .json 文件
def save_chunks_to_json(chunks, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(chunks, file, ensure_ascii=False, indent=4)

# 主函数
def split_markdown_to_json(input_md_path, output_json_path, use_recursive=False, chunk_size=100, chunk_overlap=10):
    # 读取 .md 文件
    markdown_text = read_markdown_file(input_md_path)

    # 选择分割器
    if use_recursive:
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    else:
        splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    # 分割文本
    chunks = splitter.split_text(markdown_text)

    # 将分割结果保存为 JSON
    save_chunks_to_json(chunks, output_json_path)

    print(f"分割完成，结果已保存到 {output_json_path}")

# 使用示例
input_md_path = 'zw.md'      # 输入的 .md 文件路径
output_json_path = 'output_RecursiveCharacterTextSplitter.json'  # 输出的 .json 文件路径
split_markdown_to_json(input_md_path, output_json_path, use_recursive=True)
