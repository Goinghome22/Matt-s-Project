# Module: Prompt Engineering

Develop reliable prompting strategies for LLMs.

## Objectives
- Use role, goal, and constraint framing
- Provide step-by-step tasks and evaluation criteria
- Iterate: test, inspect outputs, refine prompts

## Patterns to Try
- Role + Task + Constraints + Examples
- Ask for structure (bullets, JSON, tables) to standardize outputs
- Chain of thought: ask for reasoning steps (when appropriate)
- Self-checks: request validation against acceptance criteria

## Template
```text
You are a <role> helping with <goal>.
Constraints: <time/format/scope>.
Inputs: <data/context>.
Task: <what to produce>.
Output format: <exact structure>.
Quality bar: <acceptance criteria>.
```

## Materials
- Refer to PDFs for exercises and case studies.

## Outcomes
- Consistent, high-quality results with minimal rework. 

## Assessment / Rubric
- ✅ Prompts include role, constraints, and explicit output format
- ✅ Iterative refinement demonstrated with 2–3 prompt versions
- ✅ Self-checks or acceptance criteria included

## Next Steps
- Build a small prompt library (patterns + examples)
- Add evaluation harness: sample inputs → expected structured outputs
- Experiment with temperature and system vs. user role instructions 