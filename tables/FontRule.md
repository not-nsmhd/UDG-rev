Each table contains font display rules for the Japanese, English, Chinese and Korean languages, respectively.

## Font Rule
|Field|Size (bytes)|Offset (bytes)|Notes|
|---|---|---|---|
|Font Index|1|0|See "Font Indices" table below for accepted values.|
|Dipslay Outline|1|1||
|Character Size|2|2|This value is used to determine both width and height of each text character.<br><br>The size is calculated using this equation: `100 * charSize / 30`.<br>|
|Line Spacing Offset|2|4|This value can be negative.|
|Unknown|2|6||
|Text Color|4|8|Color is defined in BGRX format. Each value is multiplied by 2 before being used.|
|Unknown (Color?)|4|12||
|Unknown (Color?)|4|16||
|Outline Color|4|20||

## Font Indices
|Index|Font|Usage|
|---|---|---|
|0|FontNormal|Used for most text in the game.|
|1|FontDeco|Used for picked-up file titles when reading them.|
|2|FontKids|Used for child characters dialog, as well as labels in the main menu (except for the Gallery).|

## Font Rule Usage
|Index|Usage|
|---|---|
|1|Normal dialogue text in the textbox in cutscenes.|
|2|Highlighted dialogue text in the textbox in cutscenes.|
|5|Child characters' dialogue text in the textbox in cutscenes.|
|6|Highlighted child characters' dialogue text in the textbox in cutscenes.|