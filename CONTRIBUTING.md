# Contributing to LeetCode Apps

This guide shows you how to contribute explanations and solutions for LeetCode problems.

## File Structure

Each LeetCode problem should have two files:

1. **Explanation file**: `explanations/<problem-number>/en.md`
2. **Solution file**: `solutions/<problem-number>/01.py`

## Explanation File Template

Create the explanation file at `explanations/<problem-number>/en.md`:

```markdown
<Full problem statement with examples, constraints, and any images as direct links>

## Explanation

### Strategy

<Restate the problem in your own words, as if explaining to a beginner>
<Identify the type of problem (array, string, dynamic programming, graph, etc.)>
<List out what is being asked and what is given>
<Note any constraints or edge cases>
<Outline a general approach or high-level plan before diving into code>
<Break the problem into smaller subproblems or steps>
<Provide hints or guiding questions that lead toward the solution>
<Use simple, concrete examples to illustrate the approach>
<Show how to decompose the problem from general to specific>
<If applicable, discuss brute-force vs. optimized strategies>

### Steps

<Walk through the solution incrementally>
<Start with the simplest possible case or a small example>
<Build up the logic step by step, explaining each decision>
<For complex logic, use diagrams, tables, or pseudo-code as needed>
<Highlight common pitfalls and how to avoid them>
<Use clear, plain language and avoid jargon>

> **Note:** <if helpful, as a highlight block within the explanation>

**Time Complexity:** <analysis>
**Space Complexity:** <analysis>
```

## Solution File Template

Create the solution file at `solutions/<problem-number>/01.py`:

```python
from typing import List  # Add other imports as needed

# If any Python feature introduced after 3.11 is used, add this block:
# Good to know: <explain the feature simply>

def functionName(params) -> returnType:
    # Your solution here
    # Use 'res' as the result variable name (not 'ans')
    
    return res
```

## Key Rules

### Explanation File Rules
- Use highlight blocks (`> **Note:**`) for key insights within the explanation
- Follow the exact structure: Header → Problem Description → Explanation (Strategy + Steps)
- Make explanations beginner-friendly with step-by-step examples
- Use Stanford/Google teaching style: clear, incremental, no unexplained jumps

### Solution File Rules
- **Use functions, not classes** - Only use classes if the problem specifically requires them
- Use `res` as the result variable name (never use `ans`)
- Add a "Good to know" block if using Python features introduced after 3.11
- Include type hints and docstrings
- Provide example usage at the bottom
- Use modern Python features and idioms where possible

### General Rules
- All explanations must be clear, step-by-step, and use concrete examples
- Target audience: students and beginners (easy to medium skill)
- Use simple, plain language and avoid jargon
- When multiple solutions exist, prefer the one easiest to understand for beginners
- Optimizations can be discussed after the basic approach is clear

## Example Files

See these files for complete examples:
- `explanations/1/en.md` - Two Sum problem explanation
- `explanations/48/en.md` - Rotate Image problem explanation  
- `solutions/27/01.py` - Remove Element problem solution

## File Naming Convention

- **Explanation files**: `explanations/<problem-number>/en.md`
- **Solution files**: `solutions/<problem-number>/01.py`
- Use leading zeros for problem numbers < 100 (e.g., `01`, `02`, `10`, `100`)

## Getting Started

1. Choose a LeetCode problem that doesn't have an explanation yet
2. Create the explanation file following the template above
3. Create the solution file following the template above
4. Test your solution to ensure it works correctly
5. Submit a pull request with your contribution
