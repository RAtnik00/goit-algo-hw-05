import sys

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    log_dict = {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }
    return log_dict

def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            log = parse_log_line(line)
            logs.append(log)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered = [log for log in logs if log['level'] == level]
    return filtered

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count:<8}")


logs = load_logs("c:\\Users\\yarem\\Documents\\goit-algo-hw-05\\ThirdTask\\logfile.log")
counts = count_logs_by_level(logs)
display_log_counts(counts)



