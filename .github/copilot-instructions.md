## Development Practices

- Start with minimal, lean implementations focused on proof-of-concept
- Avoid implementing things from scratch
- Avoid defensive error handling for hypothetical failures
- Use print statements and logging sparingly, unless asked
- Avoid light wrappers and custom classes, unless asked
- Avoid `if __name__ == "__main__"` patterns in package code
- Skip unit tests unless explicitly requested
- Follow patterns in CONTRIBUTING.md when present
- Prefer writing Python if no language specified

## Git Operations

- When asked to remove all file changes, use `git checkout -- <filename>`
- Copy-paste commands you run and summarized execution status directly in your comment replies

## External Resources

- Validate and access link content using available MCP tools (Playwright and/or Perplexity)
- Search GitHub for relevant open-source alternatives to commercial tools
- Prioritize official package documentation over inferred usage

## Communication Style

- Use minimal emoji and special symbols
- Prioritize clarity and brevity in responses
- Ask clarifying questions when needed
- Don't infer requirements or create workarounds unless asked
- Put documentation content in comment replies, not separate files, unless asked
- Avoid sycophancy, favor objectiveness

## Change Logging

- Each time you generate code, note the changes in CHANGELOG.md
- Follow semantic versioning guidelines
- Include date and description of changes

## Coding Agent

- Set environment variables `PIP_TIMEOUT=100` and `PIP_RETRIES=2` prior to `conda` or `pip` installs
- Include plots directly in your comment reply via `![image name](https://github.com/<user/org>/<repo>/blob/<commit-id>/<filename>?raw=true)`. For provenance, ensure you use the specific commit, not the branch name


<!-- source: https://gist.github.com/sgbaird/2f3a60084e1a73868a1a7cc33baf6d06 -->

<!--- add as .github/copilot-instructions.md, see https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks for additional context --->
