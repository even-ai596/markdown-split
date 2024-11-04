import json
from langchain.text_splitter import MarkdownHeaderTextSplitter, MarkdownTextSplitter

# 读取 .md 文件内容
def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 保存分割后的内容到 .json 文件
def save_chunks_to_json(chunks, output_path):
    # 将每个 Document 对象转换为其文本内容
    chunk_data = [chunk for chunk in chunks]
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(chunk_data, file, ensure_ascii=False, indent=4)

# 主函数
def split_markdown_to_json(input_md_path, output_json_path, use_header_splitter=False, chunk_size=100, chunk_overlap=10):
    # 读取 .md 文件
    markdown_text = read_markdown_file(input_md_path)

    # 选择分割器
    if use_header_splitter:
        # 使用 MarkdownHeaderTextSplitter 按标题进行分割，需要传入 headers_to_split_on 参数
        headers_to_split_on = [("#", "H1"), ("##", "H2"), ("###", "H3")]  # 指定要分割的标题级别
        splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    else:
        # 使用 MarkdownTextSplitter 按行分割，支持 chunk_size 和 chunk_overlap 参数
        splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    # 分割文本
    chunks = splitter.split_text(markdown_text)
    
    # 将分割结果保存为 JSON 文件
    save_chunks_to_json(chunks, output_json_path)

    print(f"分割完成，结果已保存到 {output_json_path}")




# 使用示例
input_md_path = 'zw.md'      # 输入的 .md 文件路径
output_json_path = 'output_MarkdownHeaderTextSplitter.json'  # 输出的 .json 文件路径
split_markdown_to_json(input_md_path, output_json_path, use_header_splitter=False)
