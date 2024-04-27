#!/bin/bash

# 检查文件是否存在
if [ -f "docker_ps_output.txt" ]; then
    # 如果文件存在，则将 docker ps -a 命令的输出追加到文件末尾
    docker ps -a >> docker_ps_output.txt
else
    # 如果文件不存在，则创建新文件并将 docker ps -a 命令的输出写入其中
    docker ps -a > docker_ps_output.txt
fi

# 输出消息
echo "docker ps -a 命令结果已经写入到 docker_ps_output.txt"
