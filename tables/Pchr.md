Table 0 contains model entries.
Table 1 contains model animation entries.

## Model Entry
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|File Name Offset|8|0||
|Texture File Name Offsets|8 * 10|8|If the model uses less than ten textures, the remaining offsets are set to 0|
|Unknown (Flag Set?)|64|88||
|Name Offset|8|152|Shift-JIS string|
|Unknown (Padding?)|64|160||

## Model Animation Entry
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|File Name Offset|8|0||
|Runtime Flags|8|8|Set by the game at runtime|
|Name Offset|8|16|Shift-JIS string|
|Data Size|8|24|Set by the game at runtime|
|Data Pointer|8|32|Set by the game at runtime|
|Copies Loaded|8|40|Set by the game at runtime|