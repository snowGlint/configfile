#!/user/bin/python
import psutil
import pandas as pd
import argparse
import datetime
import socket
from colorama import init
from colorama import Fore
init(autoreset=True)  # This will reset the color after each print statement


# Parse command line arguments
parser = argparse.ArgumentParser(description="Query on servers' information")
parser.add_argument('-u', '--user', help='User to query')

args = parser.parse_args()

# Check if user argument is provided
if not args.user:
    parser.error(Fore.GREEN + "\nUser argument is required")

# Get the boot time of the system
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(Fore.RED + f'\nCurrent time is {current_time}; Machine was started at {boot_time}')

def get_ip_addresses():
    ip_addresses = []
    for interface, info in psutil.net_if_addrs().items():
        for addr in info:
            if addr.family == socket.AF_INET:
                ip_addresses.append(addr.address)
    return ip_addresses

ips = get_ip_addresses()
for ip in ips:
    print(Fore.GREEN + f"IP Address: {ip}")


# Get the user information
print(Fore.GREEN + '\n-- User information')
users = psutil.users()
users_data = []

for user in users:
    user_data = {
        'Username': user.name,
        'Login Time': datetime.datetime.fromtimestamp(user.started).strftime('%Y-%m-%d %H:%M:%S'),
        'Terminal': user.terminal,
        'Host': user.host
    }
    users_data.append(user_data)

users_df = pd.DataFrame(users_data)
print(users_df)

# Get CPU information
print(Fore.GREEN + "\n-- CPU information")
cpu_count = psutil.cpu_count()
print(f"CPU Count: {cpu_count}")

cpu_freq = psutil.cpu_freq()
print(f"CPU Frequency: {cpu_freq.current} MHz (min: {cpu_freq.min} MHz, max: {cpu_freq.max} MHz)")

cpu_percent = psutil.cpu_percent()
print(f"CPU Usage: {cpu_percent}%")

cpu_stats = psutil.cpu_stats()
cpu_stats_df = pd.DataFrame({
    'Context Switches': [cpu_stats.ctx_switches],
    'Interrupts': [cpu_stats.interrupts],
    'Soft Interrupts': [cpu_stats.soft_interrupts],
    'System Calls': [cpu_stats.syscalls]
})
print(Fore.BLUE + "\n-- Cpu Stats")
print(cpu_stats_df)

cpu_times = psutil.cpu_times()
cpu_times_df = pd.DataFrame({
    'User': [cpu_times.user],
    'System': [cpu_times.system],
    'Idle': [cpu_times.idle],
    'Nice': [cpu_times.nice],
    'IOWait': [cpu_times.iowait],
    'IRQ': [cpu_times.irq],
    'SoftIRQ': [cpu_times.softirq],
    'Steal': [cpu_times.steal],
    'Guest': [cpu_times.guest],
    'GuestNice': [cpu_times.guest_nice]
})
print(Fore.BLUE + "\n-- CPU times")
print(cpu_times_df)

cpu_times_percent = psutil.cpu_times_percent()
cpu_times_percent_df = pd.DataFrame({
    'User': [cpu_times_percent.user],
    'System': [cpu_times_percent.system],
    'Idle': [cpu_times_percent.idle],
    'Nice': [cpu_times_percent.nice],
    'IOWait': [cpu_times_percent.iowait],
    'IRQ': [cpu_times_percent.irq],
    'SoftIRQ': [cpu_times_percent.softirq],
    'Steal': [cpu_times_percent.steal],
    'Guest': [cpu_times_percent.guest],
    'GuestNice': [cpu_times_percent.guest_nice]
}, index=[0])
print(Fore.BLUE + "\n-- CPU times percent")
print(cpu_times_percent_df, end = "\n")

# Get disk partitions information
partitions = psutil.disk_partitions()
disk_data = []

for partition in partitions:
    usage = psutil.disk_usage(partition.mountpoint)
    disk_info = {
        'Disk': partition.device,
        'Mounts Point': partition.mountpoint,
        'File System Type': partition.fstype,
        'Total Size (GB)': usage.total / (1024 ** 3),
        'Used (GB)': usage.used / (1024 ** 3),
        'Free (GB)': usage.free / (1024 ** 3),
        'Percentage Used': usage.percent
    }
    disk_data.append(disk_info)

disk_df = pd.DataFrame(disk_data)
print(Fore.GREEN + '\n-- Disk information')
print(disk_df)

# Get virtual memory statistics
vmem = psutil.virtual_memory()
vmem_df = pd.DataFrame({
    'Total (GB)': vmem.total / (1024 ** 3),
    'Available (GB)': vmem.available / (1024 ** 3),
    'Percentage Used': vmem.percent,
    'Used (GB)': vmem.used / (1024 ** 3),
    'Free (GB)': vmem.free / (1024 ** 3)
}, index=[0])
print(Fore.GREEN + '\n-- Virtual Memory Information')
print(vmem_df)

# Get process information

all_process = [psutil.Process(pid).as_dict(attrs=('username', 'name', 'create_time', 'status', 'cwd', 'cmdline')) for pid in psutil.pids()]
all_process = pd.DataFrame(all_process)


try:
    result = all_process.query(f'username=="{args.user}"')
    print(Fore.GREEN + "\n-- Users task's Information")
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print(f"Total number of records: {len(all_process)}")


# Get network information
print(Fore.GREEN + '\n-- Network Information')
net_io = psutil.net_io_counters()
print("Network I/O statistics:")
print(f"  - Bytes sent: {net_io.bytes_sent}")
print(f"  - Bytes received: {net_io.bytes_recv}")
print(f"  - Packets sent: {net_io.packets_sent}")
print(f"  - Packets received: {net_io.packets_recv}")
print(f"  - Error in: {net_io.errin}")
print(f"  - Error out: {net_io.errout}")
print(f"  - Drop in: {net_io.dropin}")
print(f"  - Drop out: {net_io.dropout}")

net_cons = psutil.net_connections()
print(Fore.GREEN + "\nNetwork connections:")
for conn in net_cons:
    print(f"  - Family: {conn.family}, Type: {conn.type}, Local address: {conn.laddr}, Remote address: {conn.raddr}, Status: {conn.status}")


net_if_stats = psutil.net_if_stats()
print(Fore.GREEN + "\nNetwork interface statistics:")
for interface, stats in net_if_stats.items():
    print(f"Interface: {interface}")
    print(f"  - Is up: {stats.isup}")
    print(f"  - MTU: {stats.mtu}")
    print(f"  - Speed: {stats.speed} Mbps")
    print(f"  - Address: {psutil.net_if_addrs()[interface][0].address}")

net_if_addrs = psutil.net_if_addrs()
print(Fore.GREEN + "\nNetwork interface addresses:")
for interface, addresses in net_if_addrs.items():
    for address in addresses:
        print(f"Interface: {interface}, Address: {address.address}, Netmask: {address.netmask}, Broadcast: {address.broadcast}, Family: {address.family}")

# Get sensor information
print(Fore.GREEN + "\n sensors_battery:", str(psutil.sensors_battery()))
print(Fore.GREEN + "\n sensors_temperatures:", str(psutil.sensors_temperatures()))
print(Fore.GREEN + "\n sensors_fans:", str(psutil.sensors_fans().items()))


