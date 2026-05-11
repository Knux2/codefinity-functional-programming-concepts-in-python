log_lines = [
    "2024-06-01 12:00:01 INFO User logged in",
    "2024-06-01 12:00:03 ERROR Invalid password attempt",
    "2024-06-01 12:00:05 INFO User logged out",
    "2024-06-01 12:00:07 WARN Disk space low",
    "2024-06-01 12:00:10 INFO User logged in",
]

def read_log_lines(log_lines):
    for line in log_lines:
         yield line
    


for line in read_log_lines(log_lines):
    print(line)