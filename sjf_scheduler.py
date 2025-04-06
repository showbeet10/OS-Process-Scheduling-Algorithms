def sjf_scheduling(processes):
    n = len(processes)    # N = NO. OF PROCESSES
    completed = 0
    current_time = 0
    is_completed = [False] * n

    for i in range(n):
        processes[i]['index'] = i  # Store original index

    while completed != n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            if (processes[i]['arrival_time'] <= current_time) and (not is_completed[i]):
                if processes[i]['burst_time'] < min_bt:
                    min_bt = processes[i]['burst_time']
                    idx = i
                elif processes[i]['burst_time'] == min_bt:
                    if processes[i]['arrival_time'] < processes[idx]['arrival_time']:
                        idx = i

        if idx != -1:
            processes[idx]['start_time'] = current_time
            processes[idx]['completion_time'] = current_time + processes[idx]['burst_time']
            processes[idx]['turnaround_time'] = processes[idx]['completion_time'] - processes[idx]['arrival_time']
            processes[idx]['waiting_time'] = processes[idx]['turnaround_time'] - processes[idx]['burst_time']
            current_time = processes[idx]['completion_time']
            is_completed[idx] = True
            completed += 1
        else:
            current_time += 1  # CPU is idle

    processes.sort(key=lambda x: x['index'])  # Restore original order
    return processes


# Sample Input
processes = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 7},
    {'pid': 'P2', 'arrival_time': 2, 'burst_time': 4},
    {'pid': 'P3', 'arrival_time': 4, 'burst_time': 1},
    {'pid': 'P4', 'arrival_time': 5, 'burst_time': 4},
]

result = sjf_scheduling(processes)

# Print Output
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in result:
    print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['completion_time']}\t{p['turnaround_time']}\t{p['waiting_time']}")
