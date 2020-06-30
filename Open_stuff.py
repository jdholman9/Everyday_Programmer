

# Open a set of files/ folders/ web pages

# Move files? not sure if I want to include on this one
# Next video will be moving files and creating folders
# Video before this is installing Python

import os
import shutil
import webbrowser

# Starting Software
os.startfile('outlook')
os.startfile('RStudio')
os.startfile('Notepad++')

# Single word programs seem to work but multi name doesn't
#os.startfile('Acrobat Reader DC') # Doesn't work
# Right click program, select properties, copy target and paste in startfile
# Windows 10 right click, more, open file location, right click, properties, copy target
# Don't forget the r''
os.startfile(r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe") # Does work
#os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Remote Desktop Connection')


# Opening folder
os.startfile(r'C:\Users\jholman\Documents\Programming')

# Opening file
os.startfile(r'C:\Users\jholman\Documents\GFI\README.docx')

# copy file
shutil.copyfile(r'C:\Users\jholman\Documents\GFI\README.docx', r'C:\Users\jholman\Documents\Programming\Everyday_Auto\README.docx')



webbrowser.open('https://cerasis.com/transportation-technologies/', new = 2)
