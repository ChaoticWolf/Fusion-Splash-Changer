import os
import sys
import shutil
import struct
from PIL import Image

version = 'v1.0'

xex_magic = b'\x58\x45\x58\x32'
splash_magic = b'\x73\x70\x6C\x61\x73\x68'


def change_splash(xex_file, image_file):
    with Image.open (image_file) as image:
        #Verify that the image is a PNG
        if image.format != 'PNG':
            print("The specified image does not appear to be a PNG")
            sys.exit(1)
                
        #Verify that the PNG is 640x480
        width, height = image.size
            
        if width != 640 and height != 480:
            print("The specified PNG is not 640x480")
            sys.exit(1)
                
        image_mode = image.mode
            
        if 'RGB' not in image_mode:
            print("The specified PNG must be 24-bit or 32-bit color depth")
            sys.exit(1)
        
    image_size = os.path.getsize(image_file)
    
    if image_size > 68608:
        print("The specified PNG is too large (must be 67KB (68,608 bytes) or less in size)")
        sys.exit(1)

    with open (xex_file, 'r+b') as f, open (image_file, 'r+b') as i:
        #Check if the file is an xex
        if not xex_magic in f.read(4):
            print("The specified file does not appear to be an xex")
            sys.exit(1)
            
        #Verify that it's the emulator
        print("Verifying xex...")
        f.seek(0x380)
        if not splash_magic in f.read(6):
            print("Could not find splash image in xex")
            sys.exit(1)
            
        #Create a backup of the xex
        print("Backing up xex...")
        shutil.copy2(xex_file, (xex_file)+".bak")
        
        print("Setting the splash image...")
        
        #Set the splash image size        
        f.seek(0x38C)
        f.write(struct.pack('>i', image_size))
        
        #Delete the current image
        f.seek(0x68400)
        image_offset = f.tell()
        f.write(b'\x00' * 68608)
        
        #Set the new image
        f.seek(image_offset)
        f.write(i.read())
        
        print("The splash image has been added!")
       

def main():
    print("=========================================")
    print("== Xbox 360 Fusion Splash Changer %s ==" % version)
    print("=========================================\r\n")
    
    #Check if the tool is running as an exe
    if getattr(sys, 'frozen', False):
        extension = 'exe'
    else:
        extension = 'py'
        
    #Get file input
    if len(sys.argv) > 2:
        xex_file = sys.argv[1]
        image_file = sys.argv[2]
    else:
        print("Usage: fusionsplashchanger.%s xbox.xex image.png" % extension)
        sys.exit()
        
    #Check if the files exist
    if not os.path.exists(xex_file):
        print(f"{xex_file} not found")
        sys.exit(1)
    
    if not os.path.exists(image_file):
        print(f"{image_file} not found")
        sys.exit(1)
        
    change_splash(xex_file, image_file)
    

if __name__ == '__main__':
    main()