from sentence_transformers import SentenceTransformer
import json

# 指定模型的本地路径
model_path = 'paraphrase-MiniLM-L6-v2'

# 加载 SentenceTransformer 模型
model = SentenceTransformer(model_path)

# 示例 JSON 数据
json_data = """
{
    "sentences": [
        "这是一个句子。",
        "这是一个句子。"
    ]
}
"""

# 将 JSON 字符串解析为字典
data = json.loads(json_data)

# 提取句子列表
sentences = data['sentences']

# 使用模型将句子转化为向量
sentence_embeddings = model.encode(sentences)

# 输出每个句子的向量
for i, embedding in enumerate(sentence_embeddings):
    print(f"Sentence {i+1} embedding:", embedding)
