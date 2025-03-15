def error_scanner(file_name, level='ERROR'):
    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            if level in line:
                count += 1
        print(f"Found {count} occurrences of {level} in logs.")

if __name__ == '__main__':
    file_name = 'application.log'
    error_scanner(file_name)
    error_scanner(file_name, 'INFO')
    error_scanner(file_name, 'WARNING')