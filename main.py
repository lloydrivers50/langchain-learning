# =============================================================================
# main.py — WHAT IS THIS FILE AND WHY IS IT HERE?
# =============================================================================
#
# Short answer: `uv init` generated this file automatically as a boilerplate
# entry point for your Python project. It's like the "Hello World" starter
# that npm init gives you a package.json — except this is your runnable script.
#
# You can DELETE it, IGNORE it, or REPURPOSE it. It does nothing important yet.
#
# But since it's here, let's use it to learn some Python fundamentals you'll
# see everywhere in this project.
# =============================================================================


# =============================================================================
# CONCEPT 1: Functions in Python
# =============================================================================
# In JavaScript you'd write:
#
#     function main() { console.log("Hello!") }
#
# In Python, we use `def` instead of `function`:
#
#     def main():
#         print("Hello!")
#
# Key differences from JS:
#   - No curly braces {} — Python uses INDENTATION to define blocks
#   - No semicolons needed
#   - print() instead of console.log()
#   - The colon : after the function signature is required
# =============================================================================

def main():
    print("Hello from langchain-learning!")


# =============================================================================
# CONCEPT 2: if __name__ == "__main__"
# =============================================================================
# This is the ONE thing in this file that trips up every JS dev. Let's break
# it down properly.
#
# __name__ is a special variable Python sets automatically:
#
#   - If you RUN this file directly (e.g. `python main.py`),
#     Python sets __name__ = "__main__"
#
#   - If another file IMPORTS this file (e.g. `from main import main`),
#     Python sets __name__ = "main" (the module name, not "__main__")
#
# So this block is saying:
#   "Only run main() if someone executed this file directly.
#    Don't run it if someone just imported a function from it."
#
# WHY DOES THIS MATTER?
# ---------------------
# In JS, if you write code at the top level of a file, it runs on import.
# Python works the same way — top-level code runs on import too.
#
# Without this guard, if another file did `from main import main`, it would
# ALSO print "Hello from langchain-learning!" as a side effect, which you
# almost never want.
#
# This pattern is so common in Python that you'll see it in almost every
# script. It's the Python equivalent of:
#
#     // JS equivalent (conceptually)
#     if (require.main === module) {
#         main()
#     }
#
# Or in ES modules, it's like the difference between:
#   - Running `node script.js` directly
#   - vs `import { something } from './script.js'`
#
# =============================================================================

if __name__ == "__main__":
    main()


# =============================================================================
# WHAT SHOULD YOU DO WITH THIS FILE?
# =============================================================================
# For your compliance agent project, you probably won't use this file at all.
# Your actual entry point will be in your LangGraph pipeline.
#
# Options:
#   1. Delete it — it's not wired into anything
#   2. Keep it as a scratch pad for testing Python snippets
#   3. Later, repurpose it as a CLI entry point for your agent
#
# No wrong answer here. It's scaffolding, not load-bearing code.
# =============================================================================
