# SpfCommands
SpfCommands are used in LIN scripts as a way to perform actions related to the game itself, such as starting a timer, displaying subtitles, or defining passwords in puzzle rooms.

Some SpfCommands require additional LIN commands following the `SpfCommand` opcode to define (some of) their properties, in which case the next command should be a `GoToLabel` command with the same index as a `DefineLabel` command located after LIN commands required for an SpfCommand.

## SpfCommand IDs
Note: The number of additional LIN commands in the table does not include `GoToLabel` and `DefineLabel`.

|Name|ID|Number of additional LIN commands|
|---|---|---|
|Timer|0x18|0|
|SetChaser|0x19|0|
|DialogWindow_YesNo|0x2D|7|
|UnlockAchievement|0x34|0|
|ResultBonus|0x35|1|
|DialogWindow_OK|0x40|4|
|EnableManualCamera|0x46|0|

### Timer
|LIN Argument Index|Usage|
|---|---|
|1|Action|
|2|Time|
|3|Unknown|