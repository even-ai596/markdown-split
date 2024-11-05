import json
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. 加载模型
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# 2. 读取 JSON 文件
with open('output/output_CharacterTextSplitter.json', 'r', encoding='utf-8') as file:
    text_data = json.load(file)

# 3. 将字符串列表转换为向量
embeddings = model.encode(text_data, convert_to_tensor=False)

# 4. 将向量保存为 .npy 文件
np.save('output_CharacterTextSplitter1.npy', embeddings)