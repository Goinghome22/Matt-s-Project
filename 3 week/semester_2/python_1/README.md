# Module: Python — File Integrity Monitor

Automate basic file integrity checks using hashing.

## Project
- `FileIntegrityMonitor/`
  - `file_integrity_monitor.py`
  - `example_file.txt`
  - `file_integrity_report.txt` (created after runs)

## Run
```bash
cd "FileIntegrityMonitor"
python3 file_integrity_monitor.py
```

Optionally edit `file_integrity_monitor.py` to change `file_to_monitor`, `check_interval_seconds`, or `total_checks`.

## Outcomes
- Use Python to detect file changes and log results. 

## Assessment / Rubric
- ✅ Script runs successfully and logs state changes
- ✅ Variables configurable for target file and interval
- ✅ Report includes timestamps and hash deltas when changed

## Next Steps
- Add CLI args (argparse) for file path and intervals
- Write unit tests for `generate_file_hashes`
- Extend to monitor multiple files or directories 