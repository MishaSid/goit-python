import pathlib
import sys

def sort_folder_items(path):
    extensions = set()
    image_files = []
    video_files = []
    music_files = []
    docs_files = []
    archive_files = []
    unidentified_files = set()
    
    for element in path.glob('**/*.*'):
        extensions.add(element.suffix)
        if element.suffix in ['.png'] or element.suffix in ['.jpeg'] or element.suffix in ['.jpg'] or element.suffix in ['.svg']:
            image_files.append(element.name)
        elif element.suffix in ['.avi'] or element.suffix in ['.mp4'] or element.suffix in ['.mov'] or element.suffix in ['.mkv']:
            video_files.append(element.name)
        elif element.suffix in ['.mp3'] or element.suffix in ['.ogg'] or element.suffix in ['.wav'] or element.suffix in ['.amr']:
            music_files.append(element.name)
        elif element.suffix in ['.doc'] or element.suffix in ['.docx'] or element.suffix in ['.txt'] or element.suffix in ['.pdf'] or element.suffix in ['.xlsx'] or element.suffix in ['.pptx']:
            docs_files.append(element.name)
        elif element.suffix in ['.zip'] or element.suffix in ['.gz'] or element.suffix in ['.tar']:
            archive_files.append(element.name)
        elif element.suffix == '':
            folders.append(element)
        else:
            unidentified_files.add(element.suffix)
    print(f'All extensions: {extensions ^ set()}')
    print(f'Image files: {image_files}')
    print(f'Video files: {video_files}')
    print(f'Music files: {music_files}')
    print(f'Documents: {docs_files}')
    print(f'Archive files: {archive_files}')
    print(f'Unidentified files (extensions only): {unidentified_files}')


def folders_process():
    entry_folder = input('Please enter your path: ') # ввести адресу папки, яку потрібно сортувати
    path = pathlib.Path(entry_folder)
    if path.exists:
        sort_folder_items(path)
    else:
        print(f"Path {path.absolute} does not exist")


if __name__ == '__main__':
    folders_process()
