import os
import sys
import requests
import time

env_node = os.environ.get('NODE_NAME')
if env_node:
    node_name = env_node
else:
    node_name = 'edge-node'

# 环境变量获取通信的目标IP，用逗号分隔
env_ip = os.environ.get('DEST_IP')
ip_list = list()
if env_ip:
    ip_list = [s.strip() for s in env_ip.split(',')]
    print("dest IP config: ")
    print(ip_list)
else:
    print("dest IP NOT configured")
    sys.exit()

while True:
    # 轮询所有IP尝试注册
    for ip in ip_list:
        url = 'http://' + ip + '/register'
        form = {'node_name': node_name}
        try:
            response = requests.post(url, data=form)  # 发送表单进行注册
            print('节点成功注册')
            while response.status_code == 200:
                print('响应内容:', response.text)
                url = 'http://' + ip + '/receive'
                data = {'sender': node_name, 'message': 'hello'*1000}
                response = requests.post(url, json=data)  # 发送json消息数据
        except requests.exceptions.RequestException as e:
            print(f'请求失败，发生异常: {e}')
            print('3s后将尝试连接其他IP...')
            time.sleep(3)
