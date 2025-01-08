# Exchange_Rate_API_Team4

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