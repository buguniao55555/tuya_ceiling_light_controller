control to the ceiling light mainly depends on sending messages to DP 51. 
RGB color is still to be tested. 

|command | pos | range |
|---|---|------|
| turn on white light| byte 2 bit 1 | 0-1|
| turn on RGB light | byte 2 bit 2 | 0-1 |
| adjust white brightness | byte 9 - byte 10 | 10-1000|
| adjust RGB brightness | byte 7 - byte 8 | 10-1000|
| adjust RGB color white level | byte 5 - byte 6 | 0-1000, 0 -> full white|
| adjust RGB color | byte 3-4 | unknown, needs more testing |
| adjust temperature | byte 11-12 | 0 - 1000|