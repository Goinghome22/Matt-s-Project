# File Integrity Monitor

Compute MD5/SHA1 hashes at intervals to detect changes.

## Files
- `file_integrity_monitor.py`: main script
- `example_file.txt`: sample target file
- `file_integrity_report.txt`: generated report (after running)

## Run
```bash
python3 file_integrity_monitor.py
```

Adjust these variables in the script as needed:
- `file_to_monitor`
- `check_interval_seconds`
- `total_checks`

## Assessment / Rubric
- ✅ Detects and logs changes with previous vs current hashes
- ✅ Handles missing-file scenarios without crashing
- ✅ Uses functions for hashing and reporting

## Next Steps
- Add argparse for CLI configuration and multiple targets
- Switch to SHA-256 and add integrity baseline export/import
- Integrate simple alerting (email/Slack) and daily rotation 