def detect_suspicious_patterns(lines):
    patterns = ['upload', 'sftp', 'wget', 'curl']
    return [line for line in lines if any(p in line.lower() for p in patterns)]
