#!/bin/sh

# Total CPU usage

cpu_used=$( top -bn 1 | grep "Cpu" | awk '{print $2 + $4}')
cpu_free=$( top -bn 1 | grep "Cpu" | awk '{print $8}')

# Total memory usage (Free vs Used including percentage)

mem_used=$( top -bn 1 | grep "MiB Mem" | awk '{print $8}' )
mem_free=$( top -bn 1 | grep "MiB Mem" | awk '{print $4 - $8}' )

# Total disk usage (Free vs Used including percentage)

total_disk=$(df -h -x tmpfs -x devtmpfs -x loop | grep / | awk '{print $2}' | head --lines=1)
used_disk=$(df -h -x tmpfs -x devtmpfs -x loop | grep / | awk '{print $3}' | head --lines=1)
avail_disk=$(df -h -x tmpfs -x devtmpfs -x loop | grep / | awk '{print $4}' | head --lines=1)
use_percentage_disk=$(df -h -x tmpfs -x devtmpfs -x loop | grep / | awk '{print $5}' | head --lines=1)

# Top 5 processes by CPU usage

top_processes_cpu=$(top -b -n 1 | awk 'NR > 7 && NR <= 12 {print "PID:  " $1, " User: "$2, " Tool: "$12, " CPU Usage", $9}')

# Top 5 processes by memory usage

top_processes_ram=$(top -bn 1 -o %MEM | awk 'NR > 7 && NR <= 12 {print "PID:  " $1, " User: "$2, " Tool: "$12, " RAM Usage", $10}' )


# --- BEAUTIFIED OUTPUT START ---

echo "================================================================"
echo "                   SYSTEM PERFORMANCE REPORT                    "
echo "================================================================"
echo ""

echo "--- CPU STATUS ---"
echo "Used: $cpu_used% | Free: $cpu_free%"
echo ""

echo "--- MEMORY STATUS ---"
echo "Used: ${mem_used}MB | Free: ${mem_free}MB"
echo ""

echo "--- DISK STATUS (Root) ---"
echo "Total: $total_disk | Used: $used_disk | Avail: $avail_disk | Usage: $use_percentage_disk"
echo ""

echo "--- TOP 5 PROCESSES BY CPU ---"
echo "----------------------------------------------------------------"
echo "$top_processes_cpu"
echo ""

echo "--- TOP 5 PROCESSES BY RAM ---"
echo "----------------------------------------------------------------"
echo "$top_processes_ram"
echo ""

echo "================================================================"
echo "                REPORT GENERATED SUCCESSFULLY                  "
echo "================================================================"