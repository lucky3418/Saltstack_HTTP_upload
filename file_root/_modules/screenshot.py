'''
Module for screenshot and upload to http server
'''
import os;
import shutil

import salt.utils.http

#import logging
#log = logging.getLogger(__name__)

index_min = 1000000
index_max = 9999999
header_file_path = 'header.txt'
filename_header = 'file-name'


def _get_next_image_index():
    '''
    Return the index of next filname to be posted

    Returns:
        index of next filname to be posted
    '''    
    index = 0
    try:
        fin = open(header_file_path, 'r')
        for line in fin:
            karg = line.split(':')
            if 1 < len(karg) and karg[0] == filename_header:
                filename = karg[1]
                items = filename.split(".")
                index = int(items[0])
                break
        fin.close()
    except Exception as e:
        print("Failed to get filename from " + header_file_path + " : " + str(e))

    index = index + 1
    if (index < index_min or index_max < index):
        index = index_min
    return index
    

def get_next_image_name():
    '''
    Return the filname to be posted

    Returns:
        filname to be posted
    '''
    index = _get_next_image_index()
    filename = str(index) + '.jpg'
    return filename


def save_headerfile(filename):
    '''
    Save filename which posted to http server

    Args:
        filename (str) : filename for http post
    '''
    try:
        if os.path.isfile(header_file_path):
            with open(header_file_path, "rt") as fin:
                with open(header_file_path+".tmp", "wt") as fout:
                    for line in fin:
                        karg = line.split(':')
                        if 1 < len(karg) and karg[0] == filename_header:
                            fout.write(filename_header + ':' + filename + '\n')
                        else:
                            fout.write(line)

            os.remove(header_file_path)
            os.rename(header_file_path+".tmp", header_file_path)
        else:
            with open(header_file_path, "wt") as fout:
                fout.write(filename_header + ':' + filename)
    except Exception as e:
        print("Failed to write into " + header_file_path + " : " + str(e))


def screenshot(filename):
    '''
    Capture screen

    Args:
        url (filename) : filename to store screen
    '''
    shutil.copyfile('F:\\1.jpg', filename)


def upload(url, filename):
    salt.utils.http.query(
        url,
        method='POST',
        header_file=header_file_path,
        data_file=filename
    )


def screenshot_upload(url):
    '''
    Capture screen and upload it to the http server

    Args:
        url (str) : url for http post
    '''
    filename = get_next_image_name()
    screenshot(filename)
    save_headerfile(filename)
    upload(url, filename)
    os.remove(filename)

# def dump() :
#     log.warning('log message', exc_info_on_loglevel=True)
