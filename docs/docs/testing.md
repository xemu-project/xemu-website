## Resources
* [Testing Priority](https://xemu.app/testing_priority)
* [Top Issues](https://xemu.app/top_issues)
* Issues are [reported on GitHub](https://github.com/xemu-project/xemu/issues)

## Compatibility Reporting
* Anyone is welcome to submit an updated compatibility report.
* In order to submit a report, you will need an authorization token, which can be acquired after getting the Tester role on the xemu Discord server.
* To make reporting simple, reports are filed from within xemu. This lets us also include details about the game and the system the report is being made on.

### Testing guide
* Look at last report on the game's [compatibility page](https://xemu.app/#compatibility) for context. Take note of Known Issues section and last tester's description.
* Play the game for a while.
* If you find bugs,
  * If the issue was not reported yet (not shown on the Known Issues section of the compatibility page), create a [new issue](https://github.com/xemu-project/xemu/issues/new/choose).
    * Select the Title Issue template if you're reporting an issue with a game.
    * Issues should be about one specific thing. If you find multiple problems, you can file multiple issues.
    * Maybe this behavior looks like a bug but happens on real hardware. In this case, still file the bug and we'll tag it with `not-an-emulator-issue` so we don't waste time looking into it again in the future.
    * Your new issue will appear on the game's compatibility page within an hour.
  * If you see bugs listed on the report page that are fixed, help update them.
* If your experience is worse than the last reported status, try to figure out why:
  * Maybe your game dump is bad?
  * Maybe your cache is corrupt?
  * Maybe your hardware is too low end? See [here](https://xemu.app/docs/troubleshooting/#windows-performance-considerations) for some performance troubleshooting.
  * Maybe xemu regressed? Try the last tester's version of xemu for comparison on your machine.
* To create the report in xemu select <kbd>Help</kbd> &rarr; <kbd>Report Compatibility</kbd>.
  * Briefly describe your experience.
  * When selecting playability level:
    * Recall open issues for the game. If there's something that causes the game to crash in xemu, it should probably not be classified as Playable.
    * Playable is most likely the status you should pick unless the experience is very bad (Broken-Starts) or you completed the game and you believe the experience matches hardware (Perfect).
    * If the game is not in Playable/Perfect status, there should be at least one issue filed tracking whatever the problems are with the game.
  * Once your report is filed, it should appear on the site within an hour.

### On playing "100%" of a game
While thorough testing is appreciated, it's not practical to demand volunteer testers play a game entirely every time a new version of xemu is released. Therefore, for Playable status we do not require a complete playthrough of the game. Instead, we request that people report issues as they run into them and we will operate with available knowledge. If there are severe issues with a game, it will recieve a different label. If you do complete a game, we would like to know about it. Let us know on Discord.
