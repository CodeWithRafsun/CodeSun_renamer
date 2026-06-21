#!/usr/bin/env python3

import os
import sys
import time
import signal


sys.path.insert(
    0,
    os.path.dirname(os.path.abspath(__file__))
)


from core.renamer_logic import (
    batch_prefix_rename,
    find_replace_rename,
    add_date_rename,
    undo_last_rename,
    prefix_suffix_rename,
    convert_case_rename,
    remove_text_rename,
    change_extension
)


from utils.helpers import (
    validate_folder,
    validate_extension,
    validate_number,
    get_file_count
)



# Colors

CYAN="\033[0;36m"
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
PURPLE="\033[0;35m"
RESET="\033[0m"



BASE_DIR=os.path.dirname(__file__)




def decode_file(path):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            data=f.read()

            return data.encode().decode(
                "unicode_escape"
            )


    except:

        return ""




def clear():

    os.system("clear")




def loading(text):

    print(
        CYAN + text + RESET
    )


    for i in range(25):

        print(
            "█",
            end="",
            flush=True
        )

        time.sleep(0.03)


    print()




def show_banner():

    print(
        decode_file(
            os.path.join(
                BASE_DIR,
                "assets",
                "banner.txt"
            )
        )
    )





def show_success():

    print(
        decode_file(
            os.path.join(
                BASE_DIR,
                "assets",
                "success.txt"
            )
        )
    )





def handle_exit(sig,frame):

    print(
        GREEN +
        "\nThanks for using CodeSun Renamer ✓"
        +
        RESET
    )

    sys.exit()




signal.signal(
    signal.SIGINT,
    handle_exit
)





def show_menu():

    print(
        CYAN+
        """
================ MENU ================

[1] Batch Prefix Rename
[2] Find & Replace
[3] Add Date Rename
[4] Undo Rename

[5] Prefix + Suffix Rename
[6] Case Converter
[7] Remove Text
[8] Extension Converter


/help       Commands
/about      About
/version    Version
/clear      Clear
/quit       Exit

======================================

"""
        +
        RESET
    )





def folder_input():


    while True:


        folder=input(
            YELLOW+
            "\nFolder path: "
            +
            RESET
        ).strip()



        if folder=="/quit":

            return None



        valid,error=validate_folder(
            folder
        )



        if valid:


            print(
                GREEN+
                f"{get_file_count(folder)} files found"
                +
                RESET
            )


            return folder



        else:


            print(
                RED+
                error+
                RESET
            )







# ==========================
# BASIC MODES
# ==========================



def mode_1():


    folder=folder_input()


    if not folder:
        return



    prefix=input(
        "Prefix [file]: "
    ).strip() or "file"



    ext=input(
        "Extension(optional): "
    ).strip()



    valid,ext=validate_extension(
        ext
    )


    if not valid:

        print(
            RED+ext+RESET
        )

        ext=None



    batch_prefix_rename(
        folder,
        prefix,
        ext
    )






def mode_2():


    folder=folder_input()


    if not folder:
        return



    find=input(
        "Find text: "
    )


    replace=input(
        "Replace text: "
    )


    find_replace_rename(
        folder,
        find,
        replace
    )






def mode_3():


    folder=folder_input()


    if folder:

        add_date_rename(
            folder
        )






def mode_4():


    folder=folder_input()


    if folder:

        undo_last_rename(
            folder
        )





# ==========================
# ADVANCED MODES
# ==========================



def mode_5():


    folder=folder_input()


    if not folder:
        return



    prefix=input(
        "Prefix: "
    )


    suffix=input(
        "Suffix: "
    )



    prefix_suffix_rename(
        folder,
        prefix,
        suffix
    )







def mode_6():


    folder=folder_input()


    if not folder:
        return



    print("""
1. lowercase
2. UPPERCASE
3. Title Case
""")


    option=input(
        "Select: "
    )



    if option=="2":

        mode="upper"


    elif option=="3":

        mode="title"


    else:

        mode="lower"



    convert_case_rename(
        folder,
        mode
    )







def mode_7():


    folder=folder_input()


    if not folder:
        return



    text=input(
        "Remove text: "
    )


    remove_text_rename(
        folder,
        text
    )







def mode_8():


    folder=folder_input()


    if not folder:
        return



    ext=input(
        "New extension: "
    )


    change_extension(
        folder,
        ext
    )






# ==========================
# COMMAND SYSTEM
# ==========================



def command(cmd):


    if cmd=="/help":

        print("""
Commands:

/help
/about
/version
/clear
/quit
""")


    elif cmd=="/about":

        print("""
CodeSun Renamer v2.0.1

Advanced CLI File Rename Utility

Developer:
Mahedi Hasan Rafsun

Powered by CodeSun
""")


    elif cmd=="/version":

        print(
            GREEN+
            "CodeSun Renamer v2.0.1"
            +
            RESET
        )



    elif cmd=="/clear":

        clear()



    elif cmd=="/quit":

        handle_exit(
            None,
            None
        )



    else:

        print(
            RED+
            "Unknown command"
            +
            RESET
        )







def main():


    clear()


    loading(
        "Starting CodeSun Renamer..."
    )


    clear()


    show_banner()



    while True:


        show_menu()



        choice=input(
            "Select: "
        ).strip()



        if choice.startswith("/"):

            command(choice)



        elif choice=="1":

            mode_1()



        elif choice=="2":

            mode_2()



        elif choice=="3":

            mode_3()



        elif choice=="4":

            mode_4()



        elif choice=="5":

            mode_5()



        elif choice=="6":

            mode_6()



        elif choice=="7":

            mode_7()



        elif choice=="8":

            mode_8()



        else:

            print(
                RED+
                "Invalid option"
                +
                RESET
            )



        input(
            "\nPress Enter..."
        )


        clear()






if __name__=="__main__":

    main()
