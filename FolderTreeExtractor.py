import PySimpleGUI as sg
import os
import shutil

sg.theme('LightGreen3')


# defining a function for the task
def create_dirtree_without_files(src, dst):
    # getting the absolute path of the source
    # direcrory
    src = os.path.abspath(src)

    # making a variable having the index till which
    # src string has directory and a path separator
    src_prefix = len(src) + len(os.path.sep)

    # doing os walk in source directory
    for root, dirs, files in os.walk(src):
        for dirname in dirs:
            # here dst has destination directory,
            # root[src_prefix:] gives us relative
            # path from source directory
            # and dirname has folder names
            dirpath = os.path.join(dst, root[src_prefix:], dirname)

            # making the path which we made by
            # joining all of the above three
            os.mkdir(dirpath)

# define the window layout for use in PySimpleGUI
layout = [
    [sg.Text('Folder Tree Extraction')],
    [sg.Text('Choice includes root all sub directories')],
    [sg.Text('Source Directory'), sg.Input("", key="in"), sg.FolderBrowse()],
    [sg.Text('Type in new desitination for folder tree if it doesnt exist')],
    [sg.Text('Destination Directory'), sg.Input("", key="out"), sg.FolderBrowse()],

    [sg.Button(button_text="Submit", key="sub"), sg.Text('Complete folder tree extraction')],
]

window = sg.Window('Folder Tree Extractor', layout)
while True:  # Event Loop
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break
    if event =="sub":
        dirName = values['in']
        destName = values['out']

        if not os.path.exists(destName):
            os.mkdir(destName)

        # calling the above function
        create_dirtree_without_files(dirName,
                                     destName)

        break

window.Close()