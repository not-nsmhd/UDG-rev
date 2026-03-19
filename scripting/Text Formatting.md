# Text Formatting/Styling

Text format/appearance can be changed by writing format specifiers in the string itself.
Each format specifier consists of the following:
- introductory `#` character;
- text format specifier;
- numerical value, if applicable (in some cases the value can be prefixed with a `-` to make it negative);
- terminating `#` character, if the numerical value is not set to a fixed length.

|Format Specifier|Explanation|Value Usage/Effect|Example|
|---|---|---|---|
|`#`|Displays `#` character as is. The full format specifier must be `##`.||`##`|
|`c`|Text Color|3 hexadecimal values defining text color in RGB form. Each value is multiplied by 16 before being used.|`#cF00Text` ("Text" will be displayed in red color)|
|`p`|Predefined Text Color|1 value in `0` to `2` range<br>- `0` - white;<br>- `1` - red;<br>- `2` - green;<br>- `3` - blue.|`#p1Text`|
|`d`|Outline Color|3 hexadecimal values defining outline color in RGB form. Each value is multiplied by 16 before being used.|`#dF00Text`|
|`i`|Character Spacing|Additional value added after each text character along with the character's advance value. Negative values reduce the character spacing.|`#i-2#Text`|
|`z`|Character Size|Changes text character width and height.|`#z32#Text`|
|`R`|Font Rule Index|Determines which font rule to use to display the text.<br>Font rules are defined in the `Font_Rule64.bnd` file. See `tables/FontRule.md` for more information|`#R1#Text`|
|`x`|Text X Offset|Offsets the X coordinate at which the text is displayed. This value can be negative.|`#x25#Text`|
|`y`|Text Y Offset|Offsets the Y coordinate at which the text is displayed. This value can be negative.|`#y25#Text`|
|`e`|Enable Text Outline|Enables text outline. If the text outline color is not defined with a `#d` specifier, the color from the current font rule is used.|`#eText`|
|`u`|Character Width|Changes the width of text characters.|`#u60#Text`|