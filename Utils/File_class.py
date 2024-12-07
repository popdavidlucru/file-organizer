#======= imports =======#
import os
import json
#======= globals =======#
with open(r"Data\config.json", "r") as open_file:
    config = json.load(open_file)

    RELS: dict[str, str] = config["categories"]
    BASE = config["base"].replace("{HOME}", os.path.expanduser("~"))
#======= classes =======#
class File:
    def __init__(self, path: str):
        self.path = path

    @property
    def name(self) -> str:
        return os.path.basename(self.path)

    def getext(self) -> str:
        return self.path.split(".")[-1] if "." in self.path else None

    def mvtocat(self) -> None:
        """
        Moves the file to a categorized folder based on its extension.
        If the category folder doesnt exist already, it creates it.
        """

        # Checking if the path exists
        if not os.path.exists(self.path):
            print(f"Error: File does not exist at the specified path -> {self.path}")
            return
        
        # Checking if the file has an extension
        ext = self.getext()
        if ext is None:
            print(f"Error: File at {self.path} has no extension.")
            return
        
        # Checking if the extension has a corresponding folder
        if ext not in RELS.keys():
            print(f"Error: No category (REL) found for the extension -> {ext}")
            return
        
        # Target category and its path
        cat: str = RELS.get(ext)
        cat_path: str = os.path.join(BASE, cat)

        # Creating the target category folder if not already created
        if not os.path.exists(cat_path):
            try:
                os.mkdir(cat_path)
                print(f"Info: The category folder was successfully created -> {cat_path}")
            except PermissionError as e:
                print(f"PermissionError: Unable to create the folder {cat_path} - {e}")
                return
            except Exception as e:
                print(f"Unexpected Error: Failed to create folder {cat_path} - {e}")
                return

        # Attempting to move the file
        try:
            new_path: str = os.path.join(cat_path, self.name)
            os.rename(self.path, new_path)
            print(f"Success: File '{self.name}' moved to category '{cat}'.")
            self.path = new_path
        except PermissionError as e:
            print(f"PermissionError: Unable to move file '{self.path}' to {cat_path} - {e}")
        except FileNotFoundError as e:
            print(f"FileNotFoundError: The file or folder was not found during the move operation - {e}")
        except Exception as e:
            print(f"Unexpected Error: Failed to move file '{self.path}' to {cat_path} - {e}")



