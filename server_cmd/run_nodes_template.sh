#!/bin/bash

docker run -d -p 7771:5000 --name v1_1 --env NODE_NAME=v1_1 --env DEST_IP=127.0.0.1:7777 --env CPU_LOAD=10 mec:latest
docker run -d -p 7772:5000 --name v1_2 --env NODE_NAME=v1_2 --env DEST_IP=127.0.0.1:7777 --env CPU_LOAD=10 mec:latest
docker run -d -p 7773:5000 --name v2_1 --env NODE_NAME=v2_1 --env DEST_IP=127.0.0.1:7777 --env CPU_LOAD=10 mec:latest
docker run -d -p 7774:5000 --name v2_2 --env NODE_NAME=v2_2 --env DEST_IP=127.0.0.1:7777 --env CPU_LOAD=10 mec:latest
