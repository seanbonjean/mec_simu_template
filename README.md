# MEC_SIMULATOR

注意：本示例仅用作后续项目的构建模板

## 部署

本示例需要使用Docker部署，请先安装Docker

将server_deploy文件夹拷贝到服务器相应位置，并在相应位置执行以下命令：  
 `docker build -t mec:latest .`

 `docker run -d -p 7777:5000 --name edge-node --env NODE_NAME=edge-node --env DEST_IP=127.0.0.1:7777 --env CPU_LOAD=20 mec:latest`

在同一个服务器上多次执行 `docker run` 命令，部署多个vm，注意要修改 `-p` 参数为不同vm指定不同外部端口，避免物理机端口冲突；同时也要注意在 `--name` 修改容器名称，避免冲突  
DEST_IP表示通信的目标节点的IP地址和端口；可以输入多个IP:port，以逗号分隔，当一处地址下线时会前往寻找其他IP地址的节点  
CPU_LOAD表示模拟CPU负载的百分比，示例命令为20%，表示CPU忙转程度为20%，空转80%  
不需要向其他节点发送信息时，删去NODE_NAME和DEST_IP环境变量；不需要CPU负载时，删去CPU_LOAD环境变量  
如果是在测试代码，可以将 `:latest` 改为 `:dev` 或具体版本号以作区分，并且将 `docker run` 命令中 `-d` 改为 `-it` 参数进入容器内的shell

## 测试

send_http_post.py可以实现http协议POST请求，测试flask的接口

server_cmd文件夹中保存了一些shell脚本，方便使用  
使用前请先赋予运行权限： `chmod +x *.sh`

运行rm_every_container.sh时：如果没有正在运行中的容器，docker stop命令会报一下错；如果没有任何容器，docker rm命令也会报一下错。忽视即可

## 各文件功能

main.py实现flask的服务器接口，接收http请求  
post.py实现http协议POST请求，不断请求以模拟节点通信  
stress_cpu.py实现cpu压力测试，模拟CPU负载
