import pandas as pd

def parse_logs(file_path):
    data = []
    
    with open(file_path, "r") as f:
        for line in f:
            parts = line.strip().split(" ", 1)
            if len(parts) == 2:
                level, message = parts
                data.append([level, message])
    
    df = pd.DataFrame(data, columns=["level", "message"])
    return df