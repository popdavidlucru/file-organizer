# run in terminal to create .exe
# pyinstaller --onefile --noconsole --distpath ./ --workpath ./temp main.py && rmdir /s /q temp && del main.spec
# pip install -r requirements.txt

#======= imports =======#
import os
import json
from File_class import File, BASE
#======= globals =======#
...
#======= classes =======#
...
#======= functions =======#
...
#======= main =======#

def main() -> None:
    desktop_contents: list[str] | list[File]
    desktop_contents = os.listdir(BASE)
    desktop_contents = [os.path.join(BASE, file) for file in desktop_contents]
    desktop_contents = [File(path) for path in desktop_contents]

    for element in desktop_contents:
        element.mvtocat()

if __name__ == "__main__":
    main()
