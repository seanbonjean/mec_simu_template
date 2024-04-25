FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /running
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
ENV NODE_NAME="edge-node"
CMD ["sh", "-c", "python3 main.py & python3 post.py & python3 stress_cpu.py"]
