import os

BASE_PATH: str = r"C:\users\popda\desktop"
    
def extof(file_path: str) -> str | None:
    """
    Returns the extension of a given file path if one exists,
    otherwise returns None if the file is missing an extension.
    
    :param file_path: The path to the file (as a string) from which to extract the extension.
    :type file_path: str

    :return: The file extension (including the leading dot) if it exists, otherwise None.
    :rtype: str | None
    """

    return file_path.split(".")[-1] if "." in file_path else None

def mvtocat(file_path: str) -> None:

    # if the provided file does not exist
    if not os.path.exists(file_path):
        print(f"The provided file does not exist or is at another location... {file_path=}")
        return

    # if the file has no extension
    if (file_extension := extof(file_path)) is None:
        print(f"{file_path=} does not have an extension")
        return

    # if there is no relationship for the extension in ext_file_rel
    if (file_category := ext_file_rel.get(file_extension)) is None:
        print(f"There is no relation for {file_extension=}...")
        return

    # if the category folder has not yet been created
    category_path: str = os.path.join(BASE_PATH, file_category)
    if not os.path.exists(category_path):
        try:
            os.mkdir(category_path)
            print(f"{category_path} folder has been created...")
        except PermissionError as e:
            print(f"PermissionError: Unable to create the folder at {category_path}. Check your permissions. Details: {e}")
            return
        except Exception as e:
            print(f"UnexpectedError: An unexpected error occurred while creating {category_path}. Details: {e}")
            return

    # if everything is fine we can create the new location for our file
    file_name: str = os.path.basename(file_path)
    new_location: str = os.path.join(category_path, file_name)
    try:
        os.rename(file_path, new_location)
        print(f"{category_path=}")
        print(f"Successfully moved {file_name=} to {file_category}")
    except PermissionError as e:
        print(f"PermissionError: Unable to move the file {file_path} to {new_location}. Check your permissions. Details: {e}")
        return
    except Exception as e:
        print(f"UnexpectedError: An unexpected error occurred while moving the file {file_path} to {new_location}. Details: {e}")
        return

    
ext_file_rel: dict[str, str] = {
    "py": "Python Code",
    "cpp": "Cpp Code",
    "txt": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "xls": "Spreadsheets",
    "xlsx": "Spreadsheets",
    "ppt": "Presentations",
    "pptx": "Presentations",
    "pdf": "Documents",
    "jpg": "Images",
    "png": "Images",
    "gif": "Images",
    "mp3": "Audio",
    "wav": "Audio",
    "ogg": "Audio",
    "mp4": "Videos",
    "mkv": "Videos",
    "mov": "Videos",
    "avi": "Videos",
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "csv": "Data Files",
    "json": "Data Files",
    "xml": "Data Files",
    "html": "Web Files",
    "css": "Web Files",
    "js": "Web Files",
}

def main() -> None:
    desktop: list[str] = os.listdir(BASE_PATH)
    desktop = [os.path.join(BASE_PATH, file_name) for file_name in desktop]

    for file in desktop:
        mvtocat(file)

if __name__ == "__main__":
    main()
