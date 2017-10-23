# Calculating Translation Progress

## How to use

Run Translation-stats.exe, it'll craete Progress.txt in the same folder. The result of translation progress stats is in it.

---

双击运行 Translation-stats.exe 即可。
它会在同目录下创建 Progress.txt，翻译进度的统计结果就在这个文件里了。

## How to compile yourself

1. Clone or download this reop. Copy everything in BoD-Translation-Zh to your Book of Demons folder.
2. Install python and py2exe
3. Run "c:\Python26\python.exe setup.py py2exe" with "c:\Python26\python.exe" replaced by your python.exe path. Then two folders, __pycache__ and dist, should have been built now.
4. In dist folder, copy library.zip and Translation-stats.exe to the folder of make_exe.bat
5. Completed.

Actually, the exe file just a conversion of Translation-stats.py. You can also run Translation-stats.py to do the same thing.