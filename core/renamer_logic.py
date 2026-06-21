import os
from datetime import datetime



def show_success_banner():

    path = os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        "assets",
        "success.txt"
    )

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            banner = f.read()

            print(
                banner.encode().decode(
                    "unicode_escape"
                )
            )


    except:

        print(
            "\n✓ Operation Completed Successfully\n"
        )




def get_files(folder_path, extension=None):

    if not os.path.isdir(folder_path):

        return None, "Folder not found"



    files = [

        f for f in os.listdir(folder_path)

        if os.path.isfile(
            os.path.join(
                folder_path,
                f
            )
        )

    ]



    files.sort()



    if extension:


        if not extension.startswith("."):

            extension = "." + extension



        files = [

            f for f in files

            if f.endswith(extension)

        ]



    return files, None





def save_log(folder_path, log_data):


    log_path = os.path.join(
        folder_path,
        "rename_log.txt"
    )



    with open(
        log_path,
        "w",
        encoding="utf-8"
    ) as f:



        for old,new in log_data:


            f.write(
                f"{new}|{old}\n"
            )





def load_log(folder_path):


    log_path=os.path.join(
        folder_path,
        "rename_log.txt"
    )


    if not os.path.exists(log_path):

        return None,"No history found"



    data=[]



    with open(
        log_path,
        "r",
        encoding="utf-8"
    ) as f:


        for line in f:


            new,old=line.strip().split("|")


            data.append(
                (new,old)
            )



    return data,None






def preview_and_execute(folder_path, log_data):


    print(
        "\n--- Preview ---\n"
    )



    for old,new in log_data:


        print(
            os.path.basename(old),
            "->",
            os.path.basename(new)
        )



    confirm=input(
        "\nContinue? (y/n): "
    ).lower().strip()



    if confirm!="y":

        print(
            "Cancelled"
        )

        return False




    for old,new in log_data:


        os.rename(
            old,
            new
        )



    save_log(
        folder_path,
        log_data
    )



    show_success_banner()



    print(
        f"\nRenamed: {len(log_data)} files"
    )



    return True







def batch_prefix_rename(
    folder_path,
    prefix="file",
    extension=None,
    start=1,
    padding=3
):


    files,error=get_files(
        folder_path,
        extension
    )


    if error:

        return error



    logs=[]


    count=start



    for filename in files:


        name,ext=os.path.splitext(
            filename
        )



        new_name=f"{prefix}_{str(count).zfill(padding)}{ext}"



        logs.append(
            (
                os.path.join(folder_path,filename),
                os.path.join(folder_path,new_name)
            )
        )


        count+=1



    preview_and_execute(
        folder_path,
        logs
    )







def find_replace_rename(
    folder_path,
    find_text,
    replace_text,
    extension=None
):


    files,error=get_files(
        folder_path,
        extension
    )


    if error:

        return error



    logs=[]



    for filename in files:


        if find_text in filename:



            new_name=filename.replace(
                find_text,
                replace_text
            )



            logs.append(
                (
                    os.path.join(folder_path,filename),
                    os.path.join(folder_path,new_name)
                )
            )



    preview_and_execute(
        folder_path,
        logs
    )







def add_date_rename(
    folder_path,
    extension=None
):


    files,error=get_files(
        folder_path,
        extension
    )


    if error:

        return error



    date=datetime.now().strftime(
        "%Y-%m-%d"
    )


    logs=[]



    for filename in files:


        logs.append(
            (
                os.path.join(folder_path,filename),
                os.path.join(
                    folder_path,
                    f"{date}_{filename}"
                )
            )
        )



    preview_and_execute(
        folder_path,
        logs
    )







def undo_last_rename(folder_path):


    logs,error=load_log(
        folder_path
    )


    if error:

        return error




    for new,old in logs:


        if os.path.exists(new):

            os.rename(
                new,
                old
            )



    os.remove(
        os.path.join(
            folder_path,
            "rename_log.txt"
        )
    )



    show_success_banner()




# =========================
# ADVANCED FEATURES
# =========================



def prefix_suffix_rename(
    folder_path,
    prefix="",
    suffix="",
    extension=None
):


    files,error=get_files(
        folder_path,
        extension
    )


    logs=[]



    for filename in files:


        name,ext=os.path.splitext(
            filename
        )


        new_name=f"{prefix}{name}{suffix}{ext}"



        logs.append(
            (
                os.path.join(folder_path,filename),
                os.path.join(folder_path,new_name)
            )
        )



    preview_and_execute(
        folder_path,
        logs
    )







def convert_case_rename(
    folder_path,
    mode="lower",
    extension=None
):


    files,error=get_files(
        folder_path,
        extension
    )


    logs=[]



    for filename in files:


        name,ext=os.path.splitext(
            filename
        )


        if mode=="upper":

            new_name=name.upper()+ext


        elif mode=="title":

            new_name=name.title()+ext


        else:

            new_name=name.lower()+ext




        logs.append(
            (
                os.path.join(folder_path,filename),
                os.path.join(folder_path,new_name)
            )
        )



    preview_and_execute(
        folder_path,
        logs
    )







def remove_text_rename(
    folder_path,
    remove_text,
    extension=None
):


    files,error=get_files(
        folder_path,
        extension
    )


    logs=[]



    for filename in files:


        if remove_text in filename:


            new_name=filename.replace(
                remove_text,
                ""
            )



            logs.append(
                (
                    os.path.join(folder_path,filename),
                    os.path.join(folder_path,new_name)
                )
            )



    preview_and_execute(
        folder_path,
        logs
    )







def change_extension(
    folder_path,
    new_extension
):


    if not new_extension.startswith("."):

        new_extension="."+new_extension



    files,error=get_files(
        folder_path
    )


    logs=[]



    for filename in files:


        name,_=os.path.splitext(
            filename
        )


        new_name=name+new_extension



        logs.append(
            (
                os.path.join(folder_path,filename),
                os.path.join(folder_path,new_name)
            )
        )



    preview_and_execute(
        folder_path,
        logs
    )
