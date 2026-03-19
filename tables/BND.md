BND files are used to define various things, such as map and cutscene IDs, initial player stats, file names of models to use for character entities and so on. While all BND files use the same header and are loaded through the same function, the specific format of each file depends on how the game uses said file, although all file offsets in file-specific table entries are still relative to the beginning of the file itself.

The Windows version of UDG has two versions of BND files: normal ones (32-bit) and 64-bit ones. The game will always load their 64-bit versions and will always assume entry counts and offsets to be 64 bits/8 bytes in size and completely ignore their 32-bit versions, including their existence.

**Only 64-bit versions of BND files are described here.**

## Common BND Header
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|Table Count|8|0||
|String(?) Offset Array Location|8|8|Strings can be encoded either in UTF-16 (usually any text that is displayed on screen) or Shift-JIS (developer strings). Even if the file doesn't have any string data, this field is still set to the file offset pointing towards the end of all tables.|
|Padding|8|16||
|Table Descriptors|16 * Table Count|24||

## Table Descriptor
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|Starting Offset|8|0||
|Entry Count|8|16||

## String Offset Array
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|String Count|8|0||
|String Offsets Locations|8 * String Count|8||