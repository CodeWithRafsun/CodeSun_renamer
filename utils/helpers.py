import os
import re


def normalize_path(path):
    """
    Convert path into absolute path
    Supports ~ home directory
    """

    if not path:
        return ""

    return os.path.abspath(
        os.path.expanduser(
            path.strip()
        )
    )



def validate_folder(path):

    if not path or not path.strip():

        return False, "Error: Folder path cannot be empty"


    path = normalize_path(path)


    if not os.path.exists(path):

        return False, "Error: Folder does not exist"


    if not os.path.isdir(path):

        return False, "Error: Path is not a directory"


    if not os.access(path, os.R_OK):

        return False, "Error: Read permission denied"


    if not os.access(path, os.W_OK):

        return False, "Error: Write permission denied"



    return True, None




def validate_extension(ext):


    if not ext:

        return True, None



    ext = ext.strip().lower()



    if not ext.startswith("."):

        ext = "." + ext



    if not re.match(
        r"^\.[a-z0-9]+$",
        ext
    ):

        return False, (
            "Invalid extension. Example: .jpg"
        )


    return True, ext





def validate_number(
    value,
    default=1,
    min_val=1,
    max_val=9999
):


    if not value or not value.strip():

        return default, None



    try:

        number = int(
            value.strip()
        )


        if number < min_val or number > max_val:

            return default, (
                f"Number must be {min_val}-{max_val}. "
                f"Using default {default}"
            )


        return number, None



    except ValueError:


        return default, (
            f"Invalid number. "
            f"Using default {default}"
        )





def get_file_count(
    folder_path,
    extension=None
):


    folder_path = normalize_path(
        folder_path
    )


    if not os.path.isdir(folder_path):

        return 0



    count = 0



    for file in os.listdir(folder_path):


        full = os.path.join(
            folder_path,
            file
        )


        if not os.path.isfile(full):

            continue



        if file.startswith("."):

            continue



        if extension:


            if not extension.startswith("."):

                extension = "." + extension


            if not file.lower().endswith(
                extension.lower()
            ):

                continue



        count += 1



    return count





def get_folder_size(folder_path):


    total = 0


    for root, dirs, files in os.walk(folder_path):

        for file in files:

            try:

                total += os.path.getsize(
                    os.path.join(root,file)
                )

            except:

                pass



    return total





def format_size(size_bytes):


    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB"
    ]


    size = float(size_bytes)


    for unit in units:


        if size < 1024:

            return f"{size:.2f} {unit}"


        size /= 1024



    return f"{size:.2f} PB"





def clean_filename(name):

    """
    Remove unsafe characters
    """

    return re.sub(
        r'[\\/:*?"<>|]',
        "_",
        name
    )
