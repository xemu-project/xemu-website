# Development

There are opportunities for people of all skills levels to help improve the xemu
project! Join the xemu community Discord server to chat about ways to apply your
skills to improve the project.

## Contributing

### Patch submission guidelines

The xemu project generally (but not exclusively) follows the patch submission guidelines [established by the QEMU project](https://github.com/xemu-project/xemu/blob/master/docs/devel/submitting-a-patch.rst).

By following these guidelines, your patches will be easier to review and increases the speed at which your work can be incorporated into the project.

1. Patches must be submitted as Pull Requests on the xemu GitHub project at https://github.com/xemu-project/xemu.
1. Patch authors should check to see if there is an open PR that addresses the same goal.
   1. Note that an open PR does not disqualify new PRs from solving the same problem. For instance, if the original PR was in draft state for a while with no movement, or doesn't sufficiently solve the problem, it's okay to submit a PR that supersedes it.
1. If a patch fixes an Issue that was filed on xemu, mention `Fixes #XYZW` in the PR body to have GitHub auto-close the issue once the patch is merged.
   1. If an issue does not exist, it is usually worth creating one for documentation purposes.
   1. Compatibility pages that link to issues for the title will be updated automatically.
1. Patches that have multiple authors must credit them accordingly (e.g. with the `Co-authored-by: ` commit trailer).
1. Patches must be based on the latest version of the master branch at time of submission.
1. Patches must pass all CI checks to be considered for merge.
1. Patch authors must do some basic due diligence in testing of their patches, or organize with other people to get the patch tested.
   1. Providing test cases, for example as unit tests in xemu or as hardware tests in the [PGRAPH test suite](https://github.com/abaire/nxdk_pgraph_tests), greatly increases the confidence in merging your patch and builds lasting quality assurance for the project.
1. Patches should be split up into multiple commits when necessary.
1. Patches should avoid unrelated changes.
1. Patches should avoid unnecessary formatting changes mixed with logical changes.
1. Patches must have good commit messages. More on this below.
1. Patches that partially solve a problem *may* be accepted. In this case, the patch should include `FIXME` or `TODO` messages indicating points for improvement.
1. Submission of work in progress as a Pull Request Draft is encouraged for visibility.
   1. Note that if left idle for too long drafts may be superseded and/or closed.
1. Patches that are relatively smaller, targeted improvements with detailed and concise descriptions are preferred.

If you have questions about the process, feel free to ask questions in the xemu Discord server.

### Commit messages

Quality commit messages are essential for reviewing patches, navigating history, investigating issues, etc. Therefore, please follow these best practices when writing your commit messages:

1. Commit messages should be meaningful and should stand on their own as a historical record of why the changes you applied were necessary or useful.
1. The first line of the commit message should start with a `subsystem: ` prefix followed by a brief description of the change that begins with a capital letter and does not end with a period. The first line of a commit message will generally complete the sentence *This commit will...*
1. Do not use lines longer than 76 characters.
1. If a patch requires a more detailed explanation of the motivation behind the change, the first line should be followed by a blank line, then followed by a detailed description of why the change is necessary.

When in doubt, check the log of the files you're changing for general examples of acceptable commit messages.

### Review process

Once submitted to xemu-project on GitHub, the review process begins.

Please be patient in waiting for review, as reviews can take quite a lot of effort and the project has limited resources. Your contributions are valued, even if it takes a while to get to them.

It's not uncommon for patches to go through several rounds of refinement before being accepted. Please be prepared to work with the reviewer to adjust your patches accordingly.

To address review feedback, it is acceptable but not required to create a new commit addressing the review feedback. You are welcome to rebase and squash your commits as you wish.

If a reviewer leaves a comment, please respond to the comment. For example, if the reviewer requested a change, please let them know when you've made the requested changes. Please *do not* mark the conversation as resolved--leave this to the reviewer.

In general, the easier you make the reviewer's life, the faster your improvements can be adopted into the project.

### Formatting

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
