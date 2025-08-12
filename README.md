# Matt’s Project — Learning Tracks and Artifacts

![DAE Program](https://img.shields.io/badge/Program-DAE-blue) ![Goal: Junior Cybersecurity Analyst](https://img.shields.io/badge/Goal-Junior%20Cybersecurity%20Analyst-brightgreen) ![Timeline: SOC Simulation Sep–Nov](https://img.shields.io/badge/Timeline-SOC%20Simulation%20Sep%E2%80%93Nov-orange) ![Author: Matt Rich](https://img.shields.io/badge/Author-Matt%20Rich-black)

A structured portfolio of work across two tracks:

- 3-Week Track: Core foundations, design tools, security basics, Python scripting
- 6-Month Track: Unix proficiency, deeper Python projects, logic/planning, and SOC artifacts
- Docs: A small documentation site with About/Projects/Resume/Contact

## Structure

- `3 week/`
  - `semester_1/`: version control, prompt engineering, Figma, design
  - `semester_2/`: cybersecurity basics, threats & vulnerabilities, Python, SOC
- `6 month/`
  - `semester_1/`: Unix 1–2, Python 2 (CLI + GUI), Logic 1, FileIntegrityMonitor
  - `semester_2/`: FigJam flows, SOC project plan, role research
- `docs/`: Jekyll-compatible documentation site

## Quick Start

- File Integrity Monitor (either 3-week or 6-month track)
  ```bash
  # 3-week version
  cd "3 week/semester_2/python_1/FileIntegrityMonitor"
  python3 file_integrity_monitor.py

  # 6-month version
  cd "6 month/semester_1/FileIntegrityMonitor"
  python3 file_integrity_monitor.py
  ```

- Budget Calculator (CLI and GUI)
  ```bash
  cd "6 month/semester_1/python_2"
  # CLI
  python3 vacation_budget.py
  # GUI (Tkinter)
  python3 "import tkinter as tk.py"
  ```

## Documentation Site (optional)

If you use Jekyll locally:
```bash
cd docs
bundle install
bundle exec jekyll serve
```
Open http://localhost:4000 in your browser.

## Notes

- Many folders contain PDFs, scans, or design files. Open with Preview/Adobe (PDF), Excel/Numbers (XLSX), or Figma (FIG/JAM/HTML export).
- See the `README.md` inside each folder for tailored instructions and outcomes.

### Author & Program
- **Name**: Matt Rich
- **Program**: DAE

### Career Objective
- **Target Role**: Junior Cybersecurity Analyst
- **Focus Areas**: SOC operations, vulnerability management, Python automation, Unix proficiency

### In-Progress: SOC Simulation (Sep–Nov)
- Build a small-scale SOC simulation over 3 months
- Milestones:
  - Month 1: Log collection pipeline + basic detections
  - Month 2: Triage playbooks + enrichment
  - Month 3: Reporting/metrics + tabletop exercise

### Screenshots
- Logic/flow example:
  
  ![Flowchart Screenshot](6%20month/semester_1/logic_1/Screenshot%202025-07-10%20at%204.08.04%E2%80%AFPM.png)

### Key PDFs
- [Small-Scale SOC Simulation – Project Plan](6%20month/semester_2/Small-Scale%20SOC%20Simulation%20%E2%80%93%20Project%20Plan%20(1).pdf)
- [Matt Rich Cybersecurity Project](3%20week/semester_2/cybersecurity_basics_1/Matt%20Rich%20Cybersecurity%20Project.pdf)
