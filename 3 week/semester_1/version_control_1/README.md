# Module: Version Control (Git)

Learn core Git workflows for individual and collaborative development.

## Objectives
- Initialize repositories, stage/commit changes, and manage history
- Work with branches, merging, and resolving conflicts
- Push/pull with remote repositories (e.g., GitHub)
- Open pull requests and perform code reviews

## Suggested Exercises
```bash
# 1) Initialize and make commits
mkdir vc-playground && cd vc-playground
git init
printf "hello\n" > README.md
git add README.md && git commit -m "chore: init"

# 2) Branch & merge
git checkout -b feature/update-readme
echo "More details" >> README.md
git add README.md && git commit -m "docs: expand readme"
git checkout main && git merge feature/update-readme

# 3) Remote
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Materials
- PDFs and design artifacts in this folder support exercises and discussion.

## Outcomes
- Confidence using Git for day-to-day work and collaborating via pull requests. 

## Materials (Direct Links)
- [Matt Demystifying Cybersecurity Roles and Skills.pdf](./Matt%20Demystifying%20Cybersecurity%20Roles%20and%20Skills.pdf)
- [Figma Project (1).fig](./Figma%20Project%20(1).fig)

## Assessment / Rubric
- ✅ Initialize repo, make atomic commits with clear messages
- ✅ Create feature branch, open PR, request review
- ✅ Resolve a merge conflict cleanly
- ✅ Use `.gitignore` and basic branching strategy

## Next Steps
- Practice rebases and interactive rebase for commit hygiene
- Protect `main` with required reviews; try squash merges
- Configure CI to run lint/tests on PRs 