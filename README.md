# AIdentity: Your Guide to Collaborative Coding with Git and GitHub

Welcome to AIdentity project! 🚀 This quick Git cheat sheet will assist you in smoothly navigating through your coding journey on GitHub while ensuring team collaboration is top-notch.

## 🌐 Understanding Key Terms:
- **Remote**: Refers to the repository hosted on GitHub's website.
- **Local**: The repository that resides on your personal computer.

## 🚀 To get started
### Clone the Repository(Automatically establish a link to your remote repo)
```
git clone [repo-link]
```
### To check which repo you're connected to you can use:
```
git remote --v
```

## Sync with Main
### Always make sure your local main branch is updated before starting your work.
### This step ensures you have all the updated code that might have been pushed by teammates.
```
git pull origin main
```
### Ensure you're always working on your branch to avoid conflicts and ensure a smooth workflow.

## Switching to Your Branch
## Replace YourBranchName with the actual name of your branch.

```
git checkout YourBranchName
```
## Check which branch you're on

```
git branch

```

## Push to your branch
```
git add .
git commit -m "something"
git push
```

## now you can go to the website create a pull request and merge into main
### normally at work there are people who review code before merging but here we're all admins of this repo so anyone can push into main as long as there are no conflicts

## NOTES for harmonius collaboration

### Always work on your branch and push on your branch first 
### always pull from main first so you're in sync with your team







