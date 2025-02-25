# Sarcastic Commit 😂

A humorous project that generates sarcastic, frustrated, and witty commit messages based on the mood of the developer and the time of day. Ideal for adding a touch of humor to your codebase, making your commit history a lot more fun to review!

## Features 🚀

- Sarcastic Commit Messages: Generate sarcastic, frustrated, or optimistic commit messages with a simple command.

## Installation 📦

To use the `sarcastic-commit` tool, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/ip04/sarcastic-commit.git
```

2. Install dependencies (using setuptools):

```bash
cd sarcastic-commit
python3 setup.py install
```

# Usage

Once installed, you can generate sarcastic commit messages directly from the command line.

## Basic Command

To generate a random sarcastic commit message, simply run:

```bash
sarcastic-commit generate
```

## Generate Commit Message Based on Mood

You can also specify a mood to influence the generated message:

```bash
sarcastic-commit generate --mood sarcastic
sarcastic-commit generate --mood optimistic
sarcastic-commit generate --mood lazy
sarcastic-commit generate --mood frustrated
```

# Development

If you’d like to contribute or extend the project, feel free to fork the repo and submit pull requests. Here are some things you might want to work on:

- Add more moods or categories for commit messages.
- Integrate with GitHub or GitLab APIs to fetch commit messages directly from repositories.
