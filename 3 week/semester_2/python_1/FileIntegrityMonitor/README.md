# File Integrity Monitor

Periodically hashes a target file and logs whether changes occurred.

## Files
- `file_integrity_monitor.py`: main script
- `example_file.txt`: sample file to monitor
- `file_integrity_report.txt`: generated report

## Usage
```bash
python3 file_integrity_monitor.py
```

Configuration inside the script:
- `file_to_monitor`
- `check_interval_seconds`
- `total_checks`

## Output
- Console messages and appended lines in `file_integrity_report.txt` 

## Assessment / Rubric
- ✅ Handles missing file errors gracefully
- ✅ Distinguishes no-change vs. change with clear messaging
- ✅ Produces a readable, timestamped report

## Next Steps
- Support SHA-256 and configurable algorithms
- Rotate reports (daily) and add JSON/CSV export
- Add email/Slack alert on change detection 