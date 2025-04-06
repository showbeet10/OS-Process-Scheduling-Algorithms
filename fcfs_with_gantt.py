def fcfs_with_gantt(processes):
    processes.sort(key=lambda x: x['arrival_time'])
    time = 0
    gantt_chart = []

    for p in processes:
        start_time = max(time, p['arrival_time'])  #IF CPU IDLE THEN WAIT.
        time = start_time + p['burst_time']
        
        # COMPLETION TIME:--
        p['completion_time'] = time
        
        # TAT:--
        p['turnaround_time'] = p['completion_time'] - p['arrival_time']
        
        # WT:--(TAT-BT)
        p['waiting_time'] = p['turnaround_time'] - p['burst_time']
        
        
        # ADD TO GANTT CHART
        gantt_chart.append((p['pid'], start_time, time))

    return processes, gantt_chart


# Sample Input
processes = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 5},
    {'pid': 'P2', 'arrival_time': 2, 'burst_time': 3},
    {'pid': 'P3', 'arrival_time': 4, 'burst_time': 2},
]

result, gantt = fcfs_with_gantt(processes)

# Output
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in result:
    print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['completion_time']}\t{p['turnaround_time']}\t{p['waiting_time']}")

print("\nGantt Chart:")
for pid, start, end in gantt:
    print(f"| {pid} ", end='')
print("|")

for pid, start, end in gantt:
    print(f"{start}\t", end='')
print(f"{gantt[-1][2]}")
