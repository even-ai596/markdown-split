from langchain.text_splitter import CharacterTextSplitter

# 读取文件内容
with open("markdown/30-40.md", 'r', encoding='utf-8') as file:
    text = file.read()

# 分块处理
text_splitter = CharacterTextSplitter(
    separator = "\n\n",  # 尝试 "\n" 或 None
    chunk_size = 100,  # 适当减小块大小
    chunk_overlap = 10
)
docs = text_splitter.create_documents([text])

# 打印分块结果
for doc in docs:
    print(doc.page_content)
print(docs)