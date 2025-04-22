
# IMPORTING REQUIRED MODULES FOR GUI AND DATA HANDLING

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



#FCFS(FIRST COME FIRST SSERVE) ALGO:-

def fcfs_scheduler(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    gantt = []
    
    for p in processes:
        
        #CPU STARTS WHEN EITHER IT'S  FREE ORPROCESS ARRIVES:-
        
        start = max(time, p['arrival'])
        time = start + p['burst']
        
        
        # CALCULATING METRICS
        
        p['completion'] = time
        p['tat'] = p['completion'] - p['arrival']
        p['wt'] = p['tat'] - p['burst']
        
        
        
        # STORE PROCESS INFO FOR GANTT CHART
        gantt.append((p['pid'], start, time))
    return processes, gantt



# SJF (SHORTEST JOB FIRST) NP (Non Primitive):-
def sjf_scheduler(processes):
    # 
    processes.sort(key=lambda x: (x['arrival'], x['burst']))
    time, completed = 0, 0
    n = len(processes)
    is_done = [False]*n
    gantt = []

    while completed != n:
        idx = -1
        min_bt = float('inf')
        
        
        
        # CHOOSE THE SHORTEST JOB AVAILABLE AT CURRENT TIME:--
        
        for i in range(n):
            if processes[i]['arrival'] <= time and not is_done[i] and processes[i]['burst'] < min_bt:
                min_bt = processes[i]['burst']
                idx = i
                
                
        if idx != -1:
            start = time
            time += processes[idx]['burst']
            processes[idx]['completion'] = time
            processes[idx]['tat'] = time - processes[idx]['arrival']
            processes[idx]['wt'] = processes[idx]['tat'] - processes[idx]['burst']
            gantt.append((processes[idx]['pid'], start, time))
            is_done[idx] = True
            completed += 1
        else:
            time += 1
             # IF NO PROCESS AVAILBALE , INCREASE TIME 
        
    return processes, gantt



# ROUND  ROBIN SCHEDULING:---

def rr_scheduler(processes, tq):
    queue = []
    processes.sort(key=lambda x: x['arrival'])
    n = len(processes)
    remaining = [p['burst'] for p in processes]
    time = 0
    idx = 0
    gantt = []
    completed = 0
    visited = [False]*n

    while completed != n:
        for i in range(n):
            if processes[i]['arrival'] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True
        if not queue:
            time += 1
            continue
        idx = queue.pop(0)
        start = time
        
        
        # IF MORE BURST REMAINS THAN QUANTUM:--
        if remaining[idx] > tq:
            time += tq
            remaining[idx] -= tq
            gantt.append((processes[idx]['pid'], start, time))
            
            
            # RECHECK ARRIVALS AND REINSERT UNFINISHED PROCESS:--
            for i in range(n):
                if processes[i]['arrival'] <= time and not visited[i]:
                    queue.append(i)
                    visited[i] = True
            queue.append(idx)
        else:
            
            # PROCESS FINISHES HERE:--
            time += remaining[idx]
            gantt.append((processes[idx]['pid'], start, time))
            processes[idx]['completion'] = time
            processes[idx]['tat'] = time - processes[idx]['arrival']
            processes[idx]['wt'] = processes[idx]['tat'] - processes[idx]['burst']
            remaining[idx] = 0
            completed += 1
    return processes, gantt



# PRIORITY SCHEDULING (NP):-
def priority_scheduler(processes):
    processes.sort(key=lambda x: (x['arrival'], x['priority']))
    time, completed = 0, 0
    n = len(processes)
    is_done = [False]*n
    gantt = []

    while completed != n:
        idx = -1
        min_pr = float('inf')
        
        
        #  FIND PROCESS WITH HIGHEST PRIORITY AVAILABLE:--
        for i in range(n):
            if processes[i]['arrival'] <= time and not is_done[i]:
                if processes[i]['priority'] < min_pr:
                    min_pr = processes[i]['priority']
                    idx = i
        if idx != -1:
            start = time
            time += processes[idx]['burst']
            processes[idx]['completion'] = time
            processes[idx]['tat'] = time - processes[idx]['arrival']
            processes[idx]['wt'] = processes[idx]['tat'] - processes[idx]['burst']
            gantt.append((processes[idx]['pid'], start, time))
            is_done[idx] = True
            completed += 1
        else:
            time += 1
            # WAIT IF NO PROCESS IS READY
    return processes, gantt



# MAIN FUNCTION TRIGGERED ON BUTTON CLICK:--
def run_scheduler():
    try:
        selected_algo = algo_var.get()
        rows = text_input.get("1.0", tk.END).strip().split("\n")
        processes = []
        
        
        # READING I/P LINE BY LINE:--
        for row in rows:
            parts = row.strip().split()
            if selected_algo == "Priority":
                pid, at, bt, pr = parts[0], int(parts[1]), int(parts[2]), int(parts[3])
                processes.append({'pid': pid, 'arrival': at, 'burst': bt, 'priority': pr})
            else:
                pid, at, bt = parts[0], int(parts[1]), int(parts[2])
                processes.append({'pid': pid, 'arrival': at, 'burst': bt})


# RUN BASED ON SELELLCTED ALGO:-
        if selected_algo == "FCFS":
            result, chart = fcfs_scheduler(processes)
        elif selected_algo == "SJF":
            result, chart = sjf_scheduler(processes)
        elif selected_algo == "Round Robin":
            tq = int(tq_entry.get())
            result, chart = rr_scheduler(processes, tq)
        elif selected_algo == "Priority":
            result, chart = priority_scheduler(processes)
        else:
            raise Exception("Unsupported algorithm")


# DISPLAY RESULT:--
        output.delete("1.0", tk.END)
        output.insert(tk.END, "PID\tAT\tBT\tCT\tTAT\tWT\n")
        for p in result:
            output.insert(tk.END, f"{p['pid']}\t{p['arrival']}\t{p['burst']}\t{p['completion']}\t{p['tat']}\t{p['wt']}\n")


#  DISPLAY GANTT CHART:--
        gantt = "| "
        times = ""
        for pid, start, end in chart:
            gantt += f"{pid} | "
            times += f"{start}\t"
        times += f"{chart[-1][2]}"
        output.insert(tk.END, "\nGantt Chart:\n" + gantt + "\n" + times)

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or selection.\n\n{e}")


# SHOW/HIDE TIME QUANTUM :--
def toggle_tq(*args):
    if algo_var.get() == "Round Robin":
        tq_label.pack()
        tq_entry.pack()
    else:
        tq_label.pack_forget()
        tq_entry.pack_forget()

# GUI Layout STARTS:--
window = tk.Tk()
window.title("Intelligent CPU Scheduler Simulator")


# LABELS:--
tk.Label(window, text="Enter Process Data:").pack()
tk.Label(window, text="For Priority: PID AT BT PR | Else: PID AT BT").pack()


# I/P BOX FOR PROCESS DATA:--
text_input = tk.Text(window, height=6, width=40)
text_input.pack()


# DROPDOWN FOR SCHEDULING ALGO:--
algo_var = tk.StringVar()
algo_var.set("FCFS")
algo_var.trace("w", toggle_tq)
tk.Label(window, text="Select Algorithm:").pack()
algo_menu = ttk.Combobox(window, textvariable=algo_var, values=["FCFS", "SJF", "Round Robin", "Priority"])
algo_menu.pack()

tq_label = tk.Label(window, text="Enter Time Quantum:")
tq_entry = tk.Entry(window)

# BUTTON TO RUN THE SCHEDDULER:---
tk.Button(window, text="Run Scheduler", command=run_scheduler).pack(pady=5)


# O/P DISPLAY BOX:--
output = tk.Text(window, height=18, width=70)
output.pack()

# START GUI:---
window.mainloop()
