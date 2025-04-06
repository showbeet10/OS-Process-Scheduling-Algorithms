def priority_scheduling(processes):
    processes.sort(key=lambda x: (x['arrival_time'], x['priority']))  # Sort by arrival, then priority
    n = len(processes)
    current_time = 0
    completed = 0
    is_completed = [False] * n

    while completed != n:
        idx = -1
        highest_priority = float('inf')

        for i in range(n):
            if (processes[i]['arrival_time'] <= current_time) and not is_completed[i]:
                if processes[i]['priority'] < highest_priority:
                    highest_priority = processes[i]['priority']
                    idx = i
                elif processes[i]['priority'] == highest_priority:
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
            current_time += 1

    return processes   #RETURNING FINAL PROCESS LIST

# Sample Input
processes = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 5, 'priority': 2},
    {'pid': 'P2', 'arrival_time': 1, 'burst_time': 3, 'priority': 1},
    {'pid': 'P3', 'arrival_time': 2, 'burst_time': 8, 'priority': 3},
]

result = priority_scheduling(processes)

# Output
print("PID\tAT\tBT\tPR\tCT\tTAT\tWT")
for p in result:
    print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['priority']}\t{p['completion_time']}\t{p['turnaround_time']}\t{p['waiting_time']}")
