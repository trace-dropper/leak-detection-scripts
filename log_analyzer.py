import sys
from utils.filters import detect_suspicious_patterns

def analyze_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    results = detect_suspicious_patterns(lines)
    for res in results:
        print(res)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <logfile>")
    else:
        analyze_log(sys.argv[1])
