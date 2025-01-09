# Exchange_Rate_API_Team2

## Background
Added this change to test update to main branch

## Exhange Rate API Source
[https://www.exchangerate-api.com/docs/standard-requests](https://www.exchangerate-api.com/docs/standard-requests)

## Documentation on working with your branch

Switch to your working branch: Open your terminal and navigate to your project directory. Then, switch to your working branch using:

git checkout your-working-branch
Or, if you're using a newer version of Git:

git switch your-working-branch
Fetch the latest changes: Before merging, it’s a good idea to ensure you have the latest updates from the remote repository. You can do this by fetching the latest changes:

git fetch origin
Merge the main branch into your working branch: Now, merge the main branch into your working branch using:

git merge origin/main
If your main branch is named something other than main (like master), replace main with the appropriate branch name.

Resolve any merge conflicts (if they occur): If there are any conflicts, Git will notify you. You will need to manually resolve these conflicts in the affected files. After resolving conflicts, stage the changes:

git add .
Then, commit the merge:

git commit -m "Merged main into your-working-branch"
Push your changes (if necessary): If you want to push the updated working branch back to the remote repository, you can do so with:

git push origin your-working-branch

## How to add a new branch

To create a new working branch in Git, follow these steps:

Open your terminal: Make sure you have your terminal open and navigate to your project directory using the cd command.

Ensure you are on the main branch (or the branch you want to base your new branch on): It's a good practice to create a new branch from the latest version of the main branch. Switch to the main branch using:

git checkout main
Or, if you're using a newer version of Git:

git switch main
Fetch the latest changes (optional but recommended): Before creating a new branch, you may want to ensure you have the latest updates. You can do this by fetching the latest changes:

git fetch origin
Then, pull the latest changes into your local main branch:

git pull origin main
Create and switch to the new branch: Now, you can create a new branch and switch to it in one command using:

git checkout -b new-branch-name
Or, if you're using a newer version of Git:

git switch -b new-branch-name
Replace new-branch-name with the desired name for your new branch.

Verify that you are on the new branch: You can verify that you have successfully switched to the new branch by running:

git branch will show you what branch you are on