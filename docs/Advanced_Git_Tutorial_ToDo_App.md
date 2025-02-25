# 📝 Advanced Git Hands-On Tutorial – Building a To-Do App  

This tutorial provides a **hands-on guide** to practicing **all advanced Git commands** by building a simple **To-Do App** while simulating real-world Git workflows.  

---  

## **1️⃣ Setting Up the Project**  

### **🔹 Step 1: Initialize a New Git Repository**  
```sh
mkdir todo-app && cd todo-app
git init
```  

### **🔹 Step 2: Create a Simple To-Do App File**  
```sh
echo "## To-Do List" > todo.md
echo "- [ ] Learn Git" >> todo.md
echo "- [ ] Build a To-Do App" >> todo.md
```  

### **🔹 Step 3: Track and Commit the First Version**  
```sh
git add todo.md
git commit -m "Initial commit - Added To-Do List"
```  

---  

## **2️⃣ Working with Branches**  

### **🔹 Step 4: Create a New Feature Branch for Adding Tasks**  
```sh
git branch add-tasks
git checkout add-tasks
```  

### **🔹 Step 5: Add More Tasks & Commit**  
```sh
echo "- [ ] Learn Interactive Rebase" >> todo.md
echo "- [ ] Use Git Bisect" >> todo.md
git add todo.md
git commit -m "Added tasks for advanced Git commands"
```  

---  

## **3️⃣ Using Git Rebase & Cherry-Picking**  

### **🔹 Step 6: Squash Small Commits into One**  
```sh
git rebase -i HEAD~2  # Squash the last two commits
```  

### **🔹 Step 7: Apply a Specific Commit to Main Using Cherry-Pick**  
```sh
git checkout main
git cherry-pick <commit-hash>  # Replace with actual commit hash
```  

---  

## **4️⃣ Debugging & Fixing Mistakes**  

### **🔹 Step 8: Find Who Modified a Line in To-Do List**  
```sh
git blame todo.md
```  

### **🔹 Step 9: Identify When a Bug Was Introduced Using Git Bisect**  
```sh
git bisect start
git bisect bad HEAD
git bisect good <commit-hash>  # Last known working commit
```  

---  

## **5️⃣ Handling Conflicts & Worktrees**  

### **🔹 Step 10: Merge Changes and Resolve a Conflict**  
```sh
git merge add-tasks  # If a conflict arises, resolve it manually
git add todo.md
git commit -m "Resolved merge conflict"
```  

### **🔹 Step 11: Use Git Worktree for Parallel Development**  
```sh
git worktree add ../hotfix-branch hotfix
cd ../hotfix-branch
echo "- [ ] Fix urgent bug" >> todo.md
git add todo.md
git commit -m "Added an urgent bug fix"
```  

---  

## **6️⃣ Managing Dependencies & Notes**  

### **🔹 Step 12: Add an External Git Submodule (Simulating a Dependency)**  
```sh
git submodule add https://github.com/example/dependency.git external/dependency
git submodule update --init --recursive
```  

### **🔹 Step 13: Attach a Git Note to a Commit**  
```sh
git notes add -m "Remember to refactor this later" <commit-hash>
git log --show-notes
```  

---  

## **7️⃣ Optimizing the Repository**  

### **🔹 Step 14: Run Git Garbage Collection to Optimize Storage**  
```sh
git gc
git repack -a -d
```  

### **🔹 Step 15: View Git Internals**  
```sh
git cat-file -p HEAD  # View commit details
git ls-tree HEAD  # See tree structure
```  

---  

## **🎯 Congratulations! You've Applied All Advanced Git Commands! 🎉**  

You've successfully used:  
✅ Git Branching & Merging  
✅ Interactive Rebase & Cherry-Picking  
✅ Git Bisect for Debugging  
✅ Git Worktrees for Parallel Development  
✅ Git Submodules for Dependencies  
✅ Git Notes for Commit Metadata  
✅ Git Packfiles for Optimization  
✅ Git Internals Exploration  

Now, try **contributing this To-Do App to GitHub** and practice **GitHub PRs, Rebasing, and Merge Strategies!** 🚀  

Happy Coding! 😊  
