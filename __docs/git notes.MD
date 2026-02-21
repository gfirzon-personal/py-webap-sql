If you want to delete a remote branch named `feature-branch`, you would run:

```sh
git push origin --delete feature-branch
```

This command tells Git to delete the `feature-branch` from the remote repository named `origin`.

List remote branches
```sh
git branch -r
```

List local branches
```sh
git branch -l
```

Delete local branch
```sh
git branch -D <local-branch-name>
```

To find the URL of the remote named origin for your Git repository, run this command in your project directory:
```sh
git remote get-url origin
```
https://GMFinancial@dev.azure.com/GMFinancial/GMFinancial/_git/core-globalarchitecture-ilab-policyhub-chatbot-syncher

Alternatively, to list all remotes and their URLs:
```sh
git remote -v
```

### When your local Git client still shows remote branches that have been deleted from the remote, you need to prune your references.
```sh
git remote prune origin
```

### Check installed version of Git
```sh
git --version
```

### For WINDOWS Check if newer version is available, install newer version if so choosen
```sh
git update-git-for-windows
```

### For Mac, update git using Homebrew
```sh
brew upgrade git
```

## set user name and email for git globally
```sh
git config --global user.name "Your Full Name"
git config --global user.email "your@email.com"
```

## verify user name and email for git globally
```sh
git config --global user.name
git config --global user.email
```

## Where This Is Stored
Mac / Linux: ~/.gitconfig
Windows: C:\Users\YourUser\.gitconfig