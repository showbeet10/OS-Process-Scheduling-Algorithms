# def fcfs_scheduling(processes):
#     processes.sort(key=lambda x: x['arrival_time'])
#     current_time=0;
    
#     for p in processes:
#         if current_time<p['arrival_time']:
            
#             current_time = p['arrival_time']
            
#         p['start_time'] = current_time
#         currnet_time += p['burst_time']
#         p['completion_time']= p['completion_time'] - p['arrival_time']
        
#         p['waiting_time'] = p['turnaround_time'] - p['burst_time']
        
        
#         return processes
    
    
    
#     processes = [
#         {'pid ': 'P1', 'arrival_time':0,'burst_time':5 },
#         {'pid': 'P2', 'arrival_time': 1, 'burst_time': 3},
#         {'pid': 'P3', 'arrival_time': 2, 'burst_time': 8},
        
#     ]
    
    
    
#     result = fcfs_scheduling(processes)
    
    
#     print("PID\tAT\tBT\tCT\tTAT\tWT")
#     for p in result:
        
#         print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['completion_time']}\t{p['turnaround_time']}\t{p['waiting_time']}")







def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival_time'])  # Sort by arrival time

    current_time = 0
    for p in processes:
        if current_time < p['arrival_time']:
            current_time = p['arrival_time']
        p['start_time'] = current_time
        current_time += p['burst_time']
        p['completion_time'] = current_time
        p['turnaround_time'] = p['completion_time'] - p['arrival_time']
        p['waiting_time'] = p['turnaround_time'] - p['burst_time']

    return processes

# Sample Input
processes = [
    {'pid': 'P1', 'arrival_time': 0, 'burst_time': 5},
    {'pid': 'P2', 'arrival_time': 1, 'burst_time': 3},
    {'pid': 'P3', 'arrival_time': 2, 'burst_time': 8},
]

result = fcfs_scheduling(processes)

# Print Output
print("PID\tAT\tBT\tCT\tTAT\tWT")
for p in result:
    print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['completion_time']}\t{p['turnaround_time']}\t{p['waiting_time']}")


