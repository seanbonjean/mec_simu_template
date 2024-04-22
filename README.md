本示例仅用作后续项目的构建模板

将server_deploy文件夹拷贝到服务器相应位置，并在相应位置执行以下命令：  
`docker build -t mec:latest .`  
`docker run -d -p 7777:5000 --name edge-node mec:latest`  
如果是在测试代码，可以将 `:latest` 改为 `:dev` 或具体版本号以作区分，并且在 `docker run` 命令中增加 `-it` 参数进入容器内的shell

send_http_post.py可以实现简易调试
