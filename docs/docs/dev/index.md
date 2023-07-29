# Development

There are opportunities for people of all skills levels to help improve the xemu
project! Join the xemu community Discord server to chat about ways to apply your
skills to improve the project.

## Contributing

The xemu project accepts contributions by pull request on the github repository.

Please ensure code is correctly formatted before submitting a pull request.
This can be done automatically with `git-clang-format`, available with most clang distributions.

```sh
# Make some changes and stage them
git add -u

# Format and stage formatter's updates
git clang-format
git add -u

# Commit changes with an appropriate message
git commit -m "subsystem: Description of change"
```

If the changes have already been committed, the commit hashes can be passed into `git clang-format` as arguments:

```sh
# Format changes in the last commit
git clang-format HEAD~1

# Format all commits made on the branch since master
git clang-format master
```

After performing either of these commands, the formatting updates must be staged and committed. This can be done
by amending the commit that was just formatted:

```sh
git add -u
git commit --amend
```
