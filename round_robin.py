def round_robin(processes, time_quantum):
    n = len(processes)
    queue = []
    current_time = 0
    remaining_bt = [p['burst_time'] for p in processes]
    completed = 0
    
    # TO STORE START_TIME ADN CT
    process_info = {p['pid']: {'start': -1, 'completion': 0} for p in processes}
    
    
# INITIALISATION:--
    for i in range(n):
        processes[i]['waiting_time'] = 0   
        processes[i]['turnaround_time'] = 0
        processes[i]['arrival_index'] = i

    visited = [False] * n
    queue.append(0)       #PHELE PROCESS KO ADD KIYA
    visited[0] = True

    while queue:
        
        # PROCESS EXECUTION:--
        idx = queue.pop(0)
        process = processes[idx]

        if process_info[process['pid']]['start'] == -1:
            process_info[process['pid']]['start'] = max(current_time, process['arrival_time'])

        exec_time = min(time_quantum, remaining_bt[idx])
        start_time = max(current_time, process['arrival_time'])
        current_time = start_time + exec_time
        remaining_bt[idx] -= exec_time


# CHECK NEW ARRIVAL IF NEW PROCESS COME THEN IT WILL GO TO  READY QUEUE
        for i in range(n):
            if (not visited[i]) and (processes[i]['arrival_time'] <= current_time):
                queue.append(i)
                visited[i] = True

        if remaining_bt[idx] > 0:
            queue.append(idx)
        else:
            process_info[process['pid']]['completion'] = current_time
            completed += 1

    for i, p in enumerate(processes):
        p['completion_time'] = process_info[p['pid']]['completion']
        p['turnaround_time'] = p['completion_time'] - p['arrival_time']
        p['waiting_time'] = p['turnaround_time'] - p['burst_time']

    return processes


# Sample Input
processes = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 5},
    {'pid': 'P2', 'arrival_time': 1, 'burst_time': 3},
    {'pid': 'P3', 'arrival_time': 2, 'burst_time': 8},
]

time_quantum = 3

result = round_robin(processes, time_quantum)

# Output
print(f"Time Quantum: {time_quantum}")
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in result:
    print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['completion_time']}\t{p['turnaround_time']}\t{p['waiting_time']}")
