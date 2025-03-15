def error_scanner(file_name):
    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            if 'ERROR' in line:
                count += 1
        print(f"Found {count} occurrences of 'ERROR' in logs.")

if __name__ == '__main__':
    file_name = 'application.log'
    error_scanner(file_name)