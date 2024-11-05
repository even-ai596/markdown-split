import numpy as np

# 加载 .npy 文件
data = np.load('output_CharacterTextSplitter.npy')

# 展示数据
print("向量数据：")
print(data)

# 展示数据的形状
print("\n数据形状：", data.shape)
