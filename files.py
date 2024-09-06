import os
import shutil



picture = [
    '.jpg',
    '.jpeg',
    '.png',
    '.gif',
    '.bmp',
    '.tiff',
    '.svg',
    '.webp',
    '.raw'
]

music = [
    '.mp3',
    '.wav',
    '.aac',
    '.flac',
    '.ogg',
    '.wma',
    '.m4a',
    '.opus'
]


video = [
    '.mp4',
    '.avi',
    '.mov',
    '.mkv',
    '.wmv',
    '.flv',
    '.webm',
    '.mpeg',
    '.mpg'
]


code = [
    '.py',   # Python
    '.java', # Java
    '.cpp',  # C++
    '.c',    # C
    '.rb',   # Ruby
    '.go',   # Go
    '.swift' # Swift
]


document = [
    '.doc',      # Microsoft Word
    '.docx',     # Microsoft Word
    '.xls',      # Microsoft Excel
    '.xlsx',     # Microsoft Excel
    '.ppt',      # Microsoft PowerPoint
    '.pptx',     # Microsoft PowerPoint
    '.pdf',      # Portable Document Format
    '.txt',      # Text File
    '.rtf',      # Rich Text Format
    '.odt',      # OpenDocument Text
    '.csv',      # Comma-Separated Values
]


archive = [
    '.zip',
    '.rar',
    '.tar',
    '.gz',
    '.7z',
    '.xz'
]

# پسوندهای وب
web = [
    '.html',
    '.htm',
    '.css',
    '.js',
    '.json',
    '.xml',
    '.php',
    '.asp',
    '.jsp',
    '.svg'
]

# پسوندهای متن
text = [
    '.txt',
    '.md',   # Markdown
    '.log',
    '.xml',
    '.json',
    '.yaml',
    '.ini'
]




folder = input("Enter directory to tide up: \n")
temp = r'C:\temp_folder'
files = os.listdir(folder)



list = ['web', 'code', 'video', 'picture', 'document', 'music', 'text', 'unknown']

for item in list:
    os.mkdir(temp+'\\'+item)
    

for file in files:
    file = file.lower()

    for item in web:
        if file.endswith(item):
            shutil.move(folder+'\\'+file, temp+'\\'+'web')

    for item in code:
        if file.endswith(item):
            shutil.move(folder+'\\'+file, temp+'\\'+'code')

    for item in video:
        if file.endswith(item):
            shutil.move(folder+'\\'+file, temp+'\\'+'video')

    for item in picture:
        if file.endswith(item):
            shutil.move(folder+'\\'+file, temp+'\\'+'picture')

    for item in document:
        if file.endswith(item):
            shutil.move(folder+'\\'+file, temp+'\\'+'document')

    for item in music:
        if file.endswith(item):
            shutil.move(folder+'\\'+file, temp+'\\'+'music')

    for item in text:
        if file.endswith(item):
            shutil.move(folder+'\\'+file, temp+'\\'+'text')

    try:
        shutil.move(folder+'\\'+file, temp+'\\'+'unknown')
    except:
        print("...")


for item in list:
    shutil.move(temp+'\\'+item, folder)


print("done!")


