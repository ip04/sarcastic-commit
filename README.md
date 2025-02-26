# 😎 sarcastic-commit

## Because who has time for meaningful commit messages?

You know that moment—you’ve been coding for hours, debugging a nightmare, and just when you think you’ve finally fixed it (or at least made it someone else’s problem), you hit commit.

And then... **the dreaded commit message box appears.**

Yeah, we’ve all been there. You could write something useful like "Refactored the API for better performance", but let’s be real—you’re just gonna type `"fix"`, `"pls work"`, or `"final final final version"`.

Enter **sarcastic-commit**—your new best friend (or worst enabler).

---

## 🚀 What It Does

✅ Automatically generates commit messages full of sarcasm, frustration, and **blind optimism.**

✅ Saves you from having to think (thinking is overrated).

✅ Supports multiple **moods**—whether you're feeling optimistic, sarcastic, or just plain done with everything.

✅ Can be **integrated with Git hooks** to automate commit messages!

---

## 🎯 Sample Commit Messages

💡 "Fixed a bug. Probably created three more."

💡 "This commit is 90% hope and 10% actual code."

💡 "Committed at 3 AM. Future me, good luck figuring this out."

💡 "Refactored the code. Now it’s broken in new and exciting ways!"

---

## 📦 Installation & Usage

### 1️⃣ Installing `sarcastic-commit`

You can install it directly from GitHub:

```bash
pip install git+https://github.com/ip04/sarcastic-commit.git
```

Or install manually:

```bash
git clone https://github.com/ip04/sarcastic-commit.git
cd sarcastic-commit
pip install .
```

---

## 🔗 Integrating with Git Hooks

Want to **automate commit messages** so you never have to think about them again? Add `sarcastic-commit` to your Git hooks!

### 🔹 Repository-Level Git Hook

Run the following inside your Git repository:

```bash
echo 'sarcastic-commit generate > $1' > .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

Now, every time you commit, `sarcastic-commit` will generate a message for you automatically.

### 🌍 Global Git Hook (For All Repositories)

If you want `sarcastic-commit` to work across **all your Git repositories**, set up a global Git Hook:

1️⃣ Create a global hooks directory:

```bash
mkdir -p ~/.git-hooks
git config --global core.hooksPath ~/.git-hooks
```

2️⃣ Add the commit-msg hook:

```bash
echo 'sarcastic-commit generate > $1' > ~/.git-hooks/commit-msg
chmod +x ~/.git-hooks/commit-msg
```

Now, **every commit in any Git repository** will automatically get a sarcastic commit message. 🎉

---

## 🎯 Using sarcastic-commit Directly

If you don’t want to use Git Hooks, you can **manually generate** a commit message:

```bash
git commit -m "$(sarcastic-commit generate)"
```

Or specify a mood for the commit message:

```bash
git commit -m "$(sarcastic-commit generate --mood optimistic)"
```

---

## 🪟 Windows Users

If you're on Windows, follow these steps:

1️⃣ **Use Git Bash** – Run all commands inside **Git Bash**, not PowerShell or CMD.

2️⃣ **Ensure Python & Pip are Installed** – Run `python --version` and `pip --version` to check.

3️⃣ **Set Up the Commit Hook (Git Bash Command):**

```bash
echo 'sarcastic-commit generate > $1' > .git/hooks/commit-msg
chmod +x .git/hooks/commit-msg
```

If you run into issues, open `.git/hooks/commit-msg` with Notepad and manually paste this line:

```cmd
sarcastic-commit generate > %1
```

4️⃣ **Run Git Commands in Git Bash** – Example:

```bash
git commit -m "$(sarcastic-commit generate)"
```

---

## 👩‍💻 Development & Contributions

If you’d like to contribute or extend the project, feel free to **fork the repo and submit pull requests**. Here are some things you might want to work on:

🚀 Add more moods or categories for commit messages.

🚀 Implement **day-based commit messages**.

🚀 Allow users to **define custom sarcastic commit messages**.

🚀 Add **AI-powered message generation** based on code changes.

🚀 Improve **Windows support** for Git hooks in both Git Bash and PowerShell.

🚀 Create an **automatic setup script** to configure Git hooks easily.

🚀 Add **pre-push hook support** with messages like _"You’re really pushing this code? Bold move."_

🚀 Implement a **leaderboard for funny commit messages**.

🚀 Improve developer experience with **Docker support** and **unit tests (pytest)**.

---

## 🤷‍♂️ Why Use This?

✅ Because commit messages should be fun, not boring.

✅ Because debugging is more entertaining when past-you mocks you.

✅ Because writing "fix" for the 500th time isn't creative anymore.

---

## 📜 License

**MIT** – Use at your own risk. We are not responsible for sarcastic commit messages ruining your production history.

**Happy committing! 🚀**
