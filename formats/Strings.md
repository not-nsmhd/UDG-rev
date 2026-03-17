**All described field offsets are relative to the location of the table in the file itself**

## Common Strings (Table 0)
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|String Count|8|0||
|Localized String Entry|32 * String Count|8||

Each entry is a set of four 8 bytes long file offsets pointing towards the Japanese, English, Chinese and Korean variants of the string, respectively. All strings are encoded in UTF-16. The string indices are 1-based - 0th entry only contains offsets which are all set to 0, although it's also included in the string count.