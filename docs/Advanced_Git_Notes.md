# 📝 Advanced Git Learning Notes

## **1️⃣ Introduction to Git**  
- Git is a **distributed version control system** that helps developers track changes in their code.  
- Stores data as **snapshots** rather than differences (like other VCS).  

## **2️⃣ Git Basics**  
- Initialize a repo: `git init`  
- Clone a repo: `git clone <repo-url>`  
- Check status: `git status`  
- Add changes: `git add <file>`  
- Commit changes: `git commit -m "message"`  
- View history: `git log`  

## **3️⃣ Git Branching & Merging**  
- Create branch: `git branch feature-branch`  
- Switch branch: `git checkout feature-branch`  
- Merge branch: `git merge feature-branch`  
- Resolve merge conflicts manually when necessary  

## **4️⃣ Git Rebase & Interactive Rebase**  
- Rebase: `git rebase main`  
- Interactive rebase: `git rebase -i HEAD~n`  
- Squashing commits: `git rebase -i --autosquash HEAD~n`  
- Undo rebase: `git rebase --abort`  

## **5️⃣ Git Cherry-Picking**  
- Apply specific commit: `git cherry-pick <commit-hash>`  
- Apply multiple commits: `git cherry-pick <commit1> <commit2>`  
- Undo cherry-pick: `git revert <commit-hash>`  

## **6️⃣ Git Bisect**  
- Start bisect: `git bisect start`  
- Mark good commit: `git bisect good <commit>`  
- Mark bad commit: `git bisect bad <commit>`  
- Automate with a test script: `git bisect run ./test-script.sh`  

## **7️⃣ Git Worktrees**  
- Work with multiple branches at the same time:  
  ```sh
  git worktree add ../hotfix-branch hotfix
  ```
- Remove worktree: `git worktree remove ../hotfix-branch`  

## **8️⃣ Git Submodules & Subtrees**  
- Add submodule: `git submodule add <repo-url>`  
- Update submodule: `git submodule update --init --recursive`  
- Add subtree: `git subtree add --prefix=subprojects/ui-library <repo-url> main --squash`  
- Update subtree: `git subtree pull --prefix=<subtree-path> <repo-url> <branch> --squash`  

## **9️⃣ Git Hooks**  
- Pre-commit hook (e.g., linting): `.git/hooks/pre-commit`  
- Enforce commit message format: `.git/hooks/commit-msg`  
- Run tests before push: `.git/hooks/pre-push`  

## **🔟 Git Debugging (`git blame` + `git bisect`)**  
- Find who modified a line: `git blame -L 25,30 filename.txt`  
- Find the commit introducing a bug: `git bisect start`  

## **11️⃣ Git Notes**  
- Add notes: `git notes add -m "This commit introduced a bug"`  
- View notes: `git log --show-notes`  
- Push notes to remote: `git push origin refs/notes/*`  

## **12️⃣ Git Packfiles & Repository Optimization**  
- Run garbage collection: `git gc`  
- Repack objects: `git repack -a -d`  
- Prune unused objects: `git prune`  

## **13️⃣ Git Internals (`.git/objects`, `git cat-file`, `git hash-object`)**  
- View commit internals: `git cat-file -p <commit-hash>`  
- Store object manually: `git hash-object -w file.txt`  
- View repository tree: `git ls-tree HEAD`  

---  

### **🎯 Congratulations! You’ve Completed Advanced Git! 🎉**  

You've covered **everything from Git basics to advanced workflows and internal storage!** 🚀  

For further learning:  
- Contribute to open-source projects using **GitHub/GitLab**  
- Explore **GitOps** for automation  
- Master **Git CI/CD pipelines**  

Happy Coding! 😊  
