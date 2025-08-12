import hashlib
import time
from datetime import datetime

# Function: Compute MD5 and SHA1 hashes for a given file
def generate_file_hashes(file_path):
    """
    Returns the MD5 and SHA1 hashes of a file's contents.
    """
    md5_hash = hashlib.md5()
    sha1_hash = hashlib.sha1()

    try:
        with open(file_path, 'rb') as file:
            # Read and hash file in chunks
            for chunk in iter(lambda: file.read(4096), b""):
                md5_hash.update(chunk)
                sha1_hash.update(chunk)

        return md5_hash.hexdigest(), sha1_hash.hexdigest()
    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found.")
        return None, None

# Function: Append results to a report file
def log_report(report_lines, report_file_path):
    """
    Writes the report lines to the report file.
    """
    with open(report_file_path, 'a') as report_file:
        for line in report_lines:
            report_file.write(line + "\n")

# Initial setup
file_to_monitor = "example_file.txt"  # Change this to the file you want to monitor
report_file_path = "file_integrity_report.txt"
check_interval_seconds = 60  # Check every 60 seconds
total_checks = 5

# List to store hash history
hash_history = []

# Main monitoring loop
for check_number in range(total_checks):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    md5, sha1 = generate_file_hashes(file_to_monitor)

    if md5 is None or sha1 is None:
        break  # Exit if file not found

    current_hashes = {"md5": md5, "sha1": sha1, "time": current_time}
    report_lines = []

    if hash_history:
        # Compare with the last saved hash
        previous_hashes = hash_history[-1]
        if current_hashes["md5"] == previous_hashes["md5"] and current_hashes["sha1"] == previous_hashes["sha1"]:
            report_lines.append(f"[{current_time}] No change detected.")
        else:
            report_lines.append(f"[{current_time}] CHANGE DETECTED!")
            report_lines.append(f"  Previous MD5: {previous_hashes['md5']}")
            report_lines.append(f"  Current MD5 : {current_hashes['md5']}")
            report_lines.append(f"  Previous SHA1: {previous_hashes['sha1']}")
            report_lines.append(f"  Current SHA1 : {current_hashes['sha1']}")
            print("⚠️ ALERT: File change detected!")
    else:
        report_lines.append(f"[{current_time}] Initial hash generated.")

    # Save current hash to history
    hash_history.append(current_hashes)

    # Write to report file
    log_report(report_lines, report_file_path)

    # Wait for the next check
    if check_number < total_checks - 1:
        time.sleep(check_interval_seconds)

# Final summary
print("\n✅ File integrity monitoring completed. See report:", report_file_path)
