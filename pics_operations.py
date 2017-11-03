from datetime import datetime
import tarfile
import shutil
import  os
from os import listdir
from os.path import isfile, join


import PIL.Image

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

thesdpath = "/run/media/sidbg/6134-3531/DCIM/100D5300"
sdfiles = [] #[f for f in listdir(thesdpath) if isfile(join(thesdpath, f))]

def copy_files_renamed(base_dir, source_dir):
    try:
        touploadfiles = [f for f in listdir(source_dir) if isfile(join(source_dir, f))]
        for x in touploadfiles:
            datetime_object = getdatetaken(source_dir + "/" + x)
            target_dir_name = base_dir + "/" + str(datetime_object.year) + "_" + str(datetime_object.month)
            if not os.path.exists(target_dir_name):
                os.makedirs(target_dir_name)
            target_file = target_dir_name + "/" + str(datetime_object.year) + "_" + str(datetime_object.month) + "_" + str(datetime_object.day) + "_" +x
            print target_file
            shutil.copy(source_dir + "/" + x, target_file)
    except IOError as e:
        print e

    print(os.path.isdir(base_dir + "/home/el"))

def getdatetaken(imagename):
    img = PIL.Image.open(imagename)
    exif_data = img._getexif()
    datetime_object = datetime.strptime(exif_data[36867], '%Y:%m:%d %H:%M:%S')
    return datetime_object

def make_tar(imagename, filename, tar_path):
    try:
        datetime1 = getdatetaken(imagename)
        arcname1 = str(datetime1.year) + "_" + str(datetime1.month) + "_" + str(datetime1.day) + "_" + filename
        tarname = tar_path + str(datetime1.year) + "_" + str(datetime1.month)
        print "file added ----- " + arcname1
        # fileformal picbk_2017_06
        with tarfile.open( tarname, "a") as tar:
            if arcname1 in tar.getnames():
                print arcname1 + " present!!!"
            else:
                tar.add(imagename, arcname=arcname1)
    except IOError as e:
        print e
    #print exif_data


def tarize(path, tarpath) :
    touploadpath = path
    touploadfiles = [f for f in listdir(touploadpath) if isfile(join(touploadpath, f))]
    for x in touploadfiles:
        make_tar(touploadpath + "/" + x, x, tarpath)
# copy_files_renamed("/run/media/sidbg/Shrirang White Hard Drive/pictures/monthwise_pics", "/run/media/sidbg/CANON_DC/DCIM/117___04")
# copy_files_renamed("/run/media/sidbg/Shrirang White Hard Drive/pictures/monthwise_pics", "/run/media/sidbg/CANON_DC/DCIM/118___05")
# copy_files_renamed("/run/media/sidbg/Shrirang White Hard Drive/pictures/monthwise_pics", "/run/media/sidbg/CANON_DC/DCIM/119___03")
# copy_files_renamed("/run/media/sidbg/Shrirang White Hard Drive/pictures/monthwise_pics", "/run/media/sidbg/CANON_DC/DCIM/120D5300")
tarize("/run/media/sidbg/9016-4EF8/DCIM/112___10", "/run/media/sidbg/Shrirang White Hard Drive/pictures/tar_backups/")
tarize("/run/media/sidbg/9016-4EF8/DCIM/100GOPRO", "/run/media/sidbg/Shrirang White Hard Drive/pictures/tar_backups/")
tarize("/run/media/sidbg/9016-4EF8/DCIM/113D5300", "/run/media/sidbg/Shrirang White Hard Drive/pictures/tar_backups/")
#tarize("/run/media/sidbg/CANON_DC/DCIM/120D5300", "/run/media/sidbg/Shrirang White Hard Drive/pictures/tar_backups/")








def sort_images():
    for q in sdfiles:
        str1 = thesdpath + "/" + q
        os.system("xdg-open " + str1 )
        c  = raw_input('Press c to copy continue:')
        if c == 'c':
            shutil.move("/run/media/sidbg/6134-3531/DCIM/100D5300/" + q, "/run/media/sidbg/6134-3531/DCIM/100D5300/upload/" + q)
        else :
            shutil.move("/run/media/sidbg/6134-3531/DCIM/100D5300/" + q, "/run/media/sidbg/6134-3531/DCIM/100D5300/not_to_upload/" + q)

        # for a in touploadfiles:
        #     if a == q:
        #         print a
        #         shutil.move("/run/media/sidbg/6134-3531/DCIM/100D5300/"+a, "/run/media/sidbg/6134-3531/DCIM/100D5300/bucket1/"+a)