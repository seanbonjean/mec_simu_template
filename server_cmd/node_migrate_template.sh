#!/bin/bash

start_time=$(date +%s%N)
docker commit v1_1 mec_mig
docker save -o mec_mig.tar mec_mig
end_time=$(date +%s%N)
execution_time=$(( (end_time - start_time) / 1000000 ))
echo "迁移时间：$execution_time ms (+200ms)"

rm mec_mig.tar
docker rmi mec_mig

docker stop v1_1
