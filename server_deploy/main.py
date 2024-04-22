from flask import Flask, request
import requests
import json

app = Flask(__name__)

# 存储节点的名称和IP地址的字典
nodes = {}

# app.route()定义了访问方法：http://域名/service，并且规定http请求方式为POST


@app.route('/service', methods=['POST'])
def handle_service():
    data = request.json
    node_name = data.get('node')
    service_name = data.get('service')
    # 在此添加服务的任务逻辑
    return f"Service '{service_name}' handled by node '{node_name}'"


@app.route('/register', methods=['POST'])
def register_node():
    # 注意这里不太一样，其他接口的服务函数里是接收一个json数据，而本接口是接收一个表单
    node_name = request.form['node_name']
    node_address = request.remote_addr  # 这部分会获取到发送request的服务器的IP地址
    nodes[node_name] = node_address
    return f"Node '{node_name}' registered with address '{node_address}'"


@app.route('/communicate', methods=['POST'])
def communicate():
    # 在一个负责注册节点信息并控制所有通信的节点中使用这类接口，类似于ROS中的master节点
    # 简单一点就不要这个控制节点了，直接把IP地址写死在node字典里，去掉节点注册功能，节点之间直接点对点通信
    data = request.json
    sender = data.get('sender')
    receiver = data.get('receiver')
    message = data.get('message')
    if sender in nodes and receiver in nodes:
        receiver_address = nodes[receiver]
        requests.post(f"http://{receiver_address}/receive",
                      json={"sender": sender, "message": message})
        return "Message sent successfully"
    else:
        return "Sender or receiver not found"


@app.route('/receive', methods=['POST'])
def receive_message():
    data = request.json
    sender = data.get('sender')
    message = data.get('message')
    print(f"Received message from '{sender}': {message}")
    return "Message received"


if __name__ == '__main__':
    # host里的0.0.0.0代表监听所有IP地址
    # 任何IP发来的目的端口为5000的请求都会被处理
    app.run(host='0.0.0.0', port=5000)
