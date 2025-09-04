# Module: Unix 1

Practice core shell commands tied to the budgeting project.

## Key File
- `unix_notes.txt`: commands, options, editors, permissions, environment, and aliases used

## Practice
```bash
# Explore
pwd
ls -la

# View files
cat vacation_budget.py
cat -n vacation_budget.py

# Edit
nano vacation_budget.py

# Permissions
ls -l vacation_budget.py
chmod +x vacation_budget.py
```

## Assessment / Rubric
- ✅ Confident navigation and file inspection
- ✅ Edited files via terminal editor (nano/vim)
- ✅ Understood permissions and made a script executable

## Next Steps
- Write a small `setup.sh` that creates folders and copies files
- Add an alias and function to your shell profile to run the budget tool
- Explore `find`, `xargs`, and `grep -R` for project-wide searches 