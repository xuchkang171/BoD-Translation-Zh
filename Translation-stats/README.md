# Calculating Translation Progress

## How to use

If you don't have this tool yet, download it [here](https://github.com/xuchkang171/BoD-Translation-Zh/releases). For calculating translation progress, all you need is `Translation-stats` folder.
 
Place `Translation-stats` in the same folder which has your work folder (`bod_lang_**_demo` and `lang_**`), like:

    path\to\my\translation\bod_lang_zh_demo
    path\to\my\translation\lang_zh
    path\to\my\translation\Translation-stats 

Run `Translation-stats\Translation-stats.exe`, it'll write stats into Progress.txt (`path\to\my\translation\Translation-stats\Progress.txt`).

---

双击运行 `Translation-stats\Translation-stats.exe` 即可。它会将统计信息写入 Progress.txt （`path\to\my\translation\Translation-stats\Progress.txt`）。
## How to compile yourself

1. Clone or download this reop. Copy everything in `BoD-Translation-Zh` to your `Book of Demons` folder.
2. Install python and py2exe
3. Run `c:\Python26\python.exe setup.py py2exe` with `c:\Python26\python.exe` replaced by your `python.exe` path. Then two folders, `__pycache__` and `dist`, should have been built now.
4. In `dist`, copy `library.zip` and `Translation-stats.exe` to the folder of `make_exe.bat`
5. Done.

Actually, `Translation-stats.exe` just a conversion of `Translation-stats.py`. You can also run `Translation-stats.py` to do the same thing.