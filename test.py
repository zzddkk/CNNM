import torch
a = torch.randn(4, 3, 28, 28)
print('a.shape\n', a.shape)
print('第0维前加1维')
print(a.unsqueeze(0))