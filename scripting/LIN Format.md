LIN files are used as scripts for visual novel-style cutscenes ~~(please help me to come up with a better term)~~ as well as to define entity behavior in maps. While the base format is shared with DR1 and 2, UDG's opcode set is mostly different when compared to these games.

## LIN Header
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|Type|4|0|Set to 2 if the script contains a string array, 1 otherwise|
|Code Segment Offset|4|4||
|Code Segment Size/String Array Offset|4|8|Only present if the script type is set to 2|
|File Size|4|8 for type 1, 12 for type 2||

## UDG's Opcode Set

Every opcode is encoded as a big endian 16-bit integer. The same also applies to the opcode arguments if any of their size is larger than 1 byte.

Note: In the files every opcode is encoded with an added 0x7000 value.

|Name|ID|Argument Size (bytes)|
|---|---|---|
|TextCount|0x00|2|
|Text|0x01|2|
|Movie|0x05|3|
|FlashAnim|0x06|4|
|Voiceline|0x07|5|
|Music|0x08|3|
|SoundEffect|0x09|3|
|WaitForInput|0x0C|0|
|LoadNextScript|0x0E|6|
|Sprite|0x12|5|
|ScreenFlash|0x13|7|
|SetNametag|0x15|1|
|ScreenFade|0x16|3|
|SetFlag|0x17|3|
|DefineLabel|0x18|2|
|DisplayTextbox|0x19|1|
|ValueOperation|0x1A|4|
|GoToLabel|0x1B|2|
|LoadEV8|0x22|2|
|End|0x25|0|
|SpfCommand|0x30|8|
|FlagTest|0x32|4|
|ValueTest|0x33|5|
|SpfCommandParam|0x39|4|
|NoOp|0x4F|0|

## Opcodes
### TextCount
|Argument|Data Type|
|---|---|
|Text Count|uint16_t|

~~Defines the amount of strings in the file.~~<br/><br/>
The game ignores this opcode and skips the argument bytes when encountered. The actual amount of strings is defined at the beginning of the string array itself as a little endian 32-bit integer.<br/><br/>
Note that this opcode is also present in the scripts without any strings in them, in which case the text count is set to 0.

### Text
|Argument|Data Type|
|---|---|
|Index|uint16_t|

Defines index of a string in the string array, if present.

### Movie
|Argument|Data Type|
|---|---|
|Index|uint16_t|
|Unknown|uint8_t|

Plays a video file.

### Music
|Argument|Data Type|
|---|---|
|Index|uint8_t|
|Volume|uint8_t|
|Unknown|uint8_t|

Plays a music track. The indices of music tracks correspond to the `sound64.bnd` file.<br/><br/>
If the index is set to 255, this command changes the volume of the currently playing music track.

### WaitForInput
Pauses script execution until the game receives an input from the player.

### LoadNextScript
|Argument|Data Type|
|---|---|
|Category|uint16_t|
|Main|uint16_t|
|Sub|uint16_t|

Loads next script into the queue. The game will begin executing loaded script after the current one finishes.

### SetNametag
|Argument|Data Type|
|---|---|
|Index|uint8_t|

Sets the nametag on top of the textbox if its enabled. See `Nametags.md` for nametag indices.

### ScreenFade
|Argument|Data Type|
|---|---|
|Type|uint8_t|
|Color Index|uint8_t|
|Time|uint8_t|

`Type` defines the type of fade (`0` - In. `1` - Out.)<br/>
`Color Index` defines the index of the fade in the `params64.bnd` file at offset 952 in BGRX order.<br/>
`Time` defines the amount of time it takes for the fade to finish. 60 seems to make the fade last one second.<br/>

The script won't continue execution until the fade is finished.

#### Fade Colors in `params64.bnd`
|Index|Color (RGB)|
|---|---|
|0|(0, 0, 0)|
|1|(128, 0, 0)|
|2|(0, 0, 128)|
|3|(0, 128, 0)|
|4|(128, 0, 128)|
|5|(128, 128, 0)|
|6|(128, 128, 128)|
|7|(64, 0, 0)|
|8|(0, 0, 64)|
|9|(0, 64, 0)|

Note: Each color value is multiplied by 2 when the command is executed.

### SetFlag
|Argument|Data Type|
|---|---|
|Index|uint16_t|
|Value|bool (1 bit at the beginning, 7 padding bits afterwards)|

Sets the flag either to 0 or 1.

### DefineLabel
|Argument|Data Type|
|---|---|
|Index|uint16_t|

Defines a label than can be used with `GoToLabel` command for branching.

### DisplayTextbox
|Argument|Data Type|
|---|---|
|Type?|uint8_t|

### ValueOperation
|Argument|Data Type|
|---|---|
|Value Index|uint8_t|
|Operation Type Index|uint8_t|
|Operation Value|uint16_t|

Performs an operation on a script value.

#### Operation Types
*scriptValue is a value at index `Value Index`.*<br/>
*opValue is `Operation Value`.*

|Index|Operation|
|---|---|
|0|`scriptValue = opValue`|
|1|`scriptValue += opValue`|
|2|`scriptValue -= opValue`|
|3|`scriptValue *= opValue`|
|4|`scriptValue /= opValue` *(only if `opValue` is greater than 0)*|

### GoToLabel
|Argument|Data Type|
|---|---|
|Index|uint16_t|

Jumps to the next `DefineLabel` command with the same index.

### End
Ends script execution.

### SpfCommand
|Argument|Data Type|
|---|---|
|Command Type|uint16_t|
|Argument 1|int16_t|
|Argument 2|int16_t|
|Argument 3|int16_t|

Executes a game-specific command. See `SpfCommands.md` for details.

### FlagTest
|Argument|Data Type|
|---|---|
|Index|uint16_t|
|Should Not Be Equal|bool|
|Test Value|bool|

Tests a flag against a test value and skips the next command if the result is `true`. If the next command is `NoOp`, the game will also skip the command following it.

### ValueTest
|Argument|Data Type|
|---|---|
|Value Index|uint8_t|
|Test Type Index|uint8_t|
|Test Value|uint16_t|

Tests a script value against a test value and skips the next command if the result is `true`. If the next command is `NoOp`, the game will also skip the command following it.

#### Test Types
*scriptValue is a value at index `Value Index`.*<br/>
*testValue is `Test Value`.*

|Index|Test|
|---|---|
|0|`scriptValue == testValue`|
|1|`scriptValue != testValue`|
|2|`scriptValue > testValue`|
|3|`scriptValue < testValue`|
|4|`scriptValue >= testValue`|
|5|`scriptValue <= testValue`|

### SpfCommandParam
Chooses a parameter of an SpfCommand that the next LIN commands will apply to. See `SpfCommands.md` for more details.
