# Intermediate to Advanced Git Notes

## 1️⃣ Interactive Rebase (`git rebase -i`)
```sh
git rebase -i HEAD~3
```
Allows you to squash, reorder, and edit commits.

## 2️⃣ Cherry-Picking (`git cherry-pick`)
```sh
git cherry-pick <commit-hash>
```
Applies a specific commit from another branch.

## 3️⃣ Git Bisect (`git bisect`)
```sh
git bisect start
git bisect bad HEAD
git bisect good <commit-hash>
```
Helps find the commit that introduced a bug.

## 4️⃣ Git Rerere (`git rerere`)
```sh
git config --global rerere.enabled true
```
Automatically remembers and reuses previous conflict resolutions.

## 5️⃣ Git Subtree (`git subtree`)
```sh
git subtree add --prefix=subprojects/lib <repo-url> main --squash
```
Used to manage repositories inside another project without submodules.

## 6️⃣ Git Packfiles Optimization
```sh
git gc --aggressive  # Compresses and optimizes Git storage
git repack -a -d  # Manually repacks objects
```

## 7️⃣ Git Internals (`git cat-file`, `git hash-object`)
```sh
git cat-file -p <commit-hash>  # View Git objects
git hash-object -w <file>  # Manually store a file in Git
```
