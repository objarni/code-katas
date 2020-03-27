Most Recently Used
==================

A popular feature of editors of all kinds (text, graphics, spreadsheets, ..) is the Recent file list, aka MRU list. It is often found as a sub-menu of the file menu in the GUI of the program, and called something like 'Open recent' or 'Recently
used files'.

Use TDD to grow this kind of behaviour. Some examples of the behaviour is

 * When the program is run for the first time, the list is empty
 * When a file is opened, it is added to the recent file list
 * If an opened file already exists in the recent file list, it is bumped to the top, not duplicated in the list
 * If the recent file list gets full (typical number of items is 15), the oldest item is removed when a new item is added


