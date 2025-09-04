# Module: Unix 2

Build on Unix 1 with more commands and multi-argument usage.

## Topics
- Directory management: `mkdir`, `cp`, `mv`, `rm`
- Viewing long files: `less`
- Searching: `grep -i`
- Environment: shells, aliases, prompt customization

## Practice
```bash
mkdir logs && mv expenses.txt logs/
cp vacation_budget.py vacation_budget_backup.py
grep -i "Flight" expenses.txt || true
```

## Outcomes
- Confident with everyday shell tasks and lightweight automation. 

## Assessment / Rubric
- ✅ Comfortable with `mkdir/cp/mv/rm` and `less`
- ✅ Can search effectively with `grep` and flags
- ✅ Uses aliases and environment variables

## Next Steps
- Learn `tar`, `zip`, and `rsync` for backups
- Use `cron` or `launchd` for scheduled tasks
- Explore `awk`/`sed` for text processing 