# 读取 .md 文件内容
file_path = "markdown_split.md"

with open(file_path, 'r', encoding='utf-8') as file:
    markdown_text = file.read()

# 使用 MarkdownTextSplitter 进行分块
from langchain.text_splitter import MarkdownTextSplitter

markdown_splitter = MarkdownTextSplitter(chunk_size=100, chunk_overlap=20)
docs = markdown_splitter.split_text ([markdown_text])
for i, doc in enumerate(docs):
    print(f"块 {i+1}:\n{doc.page_content}\n{'-'*50}")
    
import json

# 提取每个块的内容
chunks = [doc.page_content for doc in docs]

# 保存到 JSON 文件
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, ensure_ascii=False, indent=4)
