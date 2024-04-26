import psutil
import time
from collections import defaultdict

def get_python_processes():
    python_processes = []
    for process in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        if process.info['name'] == 'python3':
            python_processes.append(process.info)
    return python_processes

def get_container_id(pid):
    try:
        with open(f"/proc/{pid}/cgroup", "r") as f:
            for line in f:
                if "docker" in line:
                    parts = line.split("/")
                    container_id = parts[-1].strip()
                    return container_id[:7]  # 只返回前7位容器ID
    except Exception as e:
        print(f"Error getting container ID for PID {pid}: {e}")
    return None

def record_process_stats(file_path, num_records, delay):
    for i in range(num_records):
        python_processes = get_python_processes()  # 先获取一次，避免第一次记录异常
        time.sleep(delay)
        print(f"Recording {i+1}/{num_records}...")
        with open(file_path, 'a') as file:
            file.write(f"Record {i+1}:\n")
            python_processes = get_python_processes()
            container_stats = defaultdict(lambda: {'cpu_percent': 0.0, 'memory_percent': 0.0})
            if python_processes:
                file.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
                for process in python_processes:
                    container_id = get_container_id(process['pid'])
                    if container_id:
                        container_stats[container_id]['cpu_percent'] += process['cpu_percent']
                        container_stats[container_id]['memory_percent'] += process['memory_percent']
                    file.write(f"Container ID: {container_id or 'Unknown'} - PID: {process['pid']} - CPU: {process['cpu_percent']:.2f}% - Memory: {process['memory_percent']:.2f}%\n")
                for container_id, stats in container_stats.items():
                    file.write(f"Container {container_id}: Total CPU: {stats['cpu_percent']:.2f}%, Total Memory: {stats['memory_percent']:.2f}%\n")
                file.write("\n")
            else:
                file.write(time.strftime("%Y-%m-%d %H:%M:%S") + " - No Python3 processes found\n\n")


if __name__ == "__main__":
    # 监控并记录python3进程的CPU利用率和内存占用率
    print("Recording process status...")
    file_path = "process_stats.txt"  # 保存记录的文件路径
    num_records = 10  # 记录次数
    delay = 30  # 记录间隔（秒）
    record_process_stats(file_path, num_records, delay)
