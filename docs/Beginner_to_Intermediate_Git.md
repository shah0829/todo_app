# Beginner to Intermediate Git Notes

## Introduction
Git is a distributed version control system that allows multiple people to work on a project without conflicts. This document covers fundamental and intermediate Git concepts.

## 1️⃣ Setting Up Git
```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 2️⃣ Initializing a Repository
```sh
git init
```

## 3️⃣ Cloning a Repository
```sh
git clone <repository-url>
```

## 4️⃣ Basic Git Workflow
- `git add <file>` – Stages changes
- `git commit -m "Message"` – Saves changes
- `git push` – Uploads commits to a remote

## 5️⃣ Branching and Merging
```sh
git branch feature-branch
git checkout feature-branch
git merge feature-branch
```

## 6️⃣ Undoing Changes
```sh
git reset --soft HEAD~1  # Undo last commit but keep changes
git reset --hard HEAD~1  # Undo last commit and remove changes
```

## 7️⃣ Working with Remote Repositories
```sh
git remote add origin <url>
git push -u origin main
git pull origin main
```

## 8️⃣ Handling Merge Conflicts
When merging branches, if a conflict occurs:
1. Open the conflicting file.
2. Resolve differences.
3. Stage the resolved file (`git add <file>`).
4. Commit the resolution (`git commit -m "Resolved conflict"`).
