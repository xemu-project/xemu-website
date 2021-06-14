**Snapshots**, also often called *Save States*, are a representation of the entire machine state which can be saved or restored at any time. With snapshots you can virtually eliminate the need to rely on in-game checkpoints to save your progress. Save a snapshot, and load it up again later and it's as if you had just kept on playing.

**Warning:** Please be aware that snapshots are a brand new feature. While this feature works reliably in my testing, there may be some bugs. There is not a convenient interface yet, and there are some caveats to be aware of.

Saving and restoring snapshots is currently done using the Monitor. After you have launched your game in xemu, open the Monitor window by navigating to <kbd>Debug</kbd> &rarr; <kbd>Monitor</kbd>.

* **Save a snapshot:**  Enter the command `savevm my-snapshot`, where `my-snapshot` is a name you can give to this snapshot
* **List snapshots:** Enter the command `info snapshots`
* **Restore a snapshot:** Enter the command `loadvm my-snapshot`
* **Delete a snapshot:** Enter the command `delvm my-snapshot`

Snapshots are saved to the hard disk image that you started xemu with.

Important Notes
---------------
Before restoring a snapshot, you should:

* **Load your game disc image as normal.** Loading a snapshot will not re-mount the game disc, so if you load a snapshot and the game then tries to read from disc, it will fail. Launch xemu, load your game disc, then restore the snapshot.

* **Connect controllers to match the saved configuration.** For instance: if there was a controller connected to Port 1 when the snapshot was created, make sure there is a controller connected to Port 1 before loading the snapshot. If this configuration does not match, an error message will be displayed and the machine will be paused. Simply connect the appropriate controllers, load the snapshot again, and enter `cont` in the monitor to continue).
