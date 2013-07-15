FolderUpdateChecker
===================

This python script once run will check every x number of minutes to see if any change to the directory passed in has occured. If a change has occured then the script zips up the folder and saves in the same directory as the python script.

Example usage:

If the file is placed in the directory test and has a subfolder test1 then to have the script check every 10 minutes if any change has happen in the folder test1 enter the following on your terminal.

python fileSaver.py test1 10

License
===================

FolderUpdateChecker is released under the <a href="http://opensource.org/licenses/GPL-3.0">GNU General Public License, version 3</a>
