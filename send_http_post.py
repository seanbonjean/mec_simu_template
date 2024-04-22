import requests

# 定义目标 URL 和要发送的数据
url = 'http://localhost:5000/register'
data = {'node_name': 'edge-node-1'}
# data = {'key1': 'value1', 'key2': 'value2'}

# 发送 POST 请求
response = requests.post(url, data=data)  # 发送表单
# response = requests.post(url, json=data)  # 发送json

# 检查响应状态码
if response.status_code == 200:
    print('请求成功')
    print('响应内容:', response.text)
else:
    print('请求失败')
    print('响应状态码:', response.status_code)
