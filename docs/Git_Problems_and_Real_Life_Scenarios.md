# Git Problems & Real-Life Scenarios

## 1️⃣ Problem: You accidentally committed sensitive data
**Solution:**
```sh
git reset --soft HEAD~1
git rm --cached sensitive-file
git commit --amend -C HEAD
git push --force
```

## 2️⃣ Problem: Your branch is behind `origin/main`
**Solution:**
```sh
git pull origin main --rebase
```

## 3️⃣ Problem: You need to apply a commit from another branch
**Solution:**
```sh
git cherry-pick <commit-hash>
```

## 4️⃣ Problem: You want to recover a deleted branch
**Solution:**
```sh
git reflog
git checkout -b recovered-branch <commit-hash>
```
