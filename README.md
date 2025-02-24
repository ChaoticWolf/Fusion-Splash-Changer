# Fusion Splash Changer
This is a simple tool for changing the splash screen image that appears when loading a game in the Xbox 360's Original Xbox emulator.

## Requirements
You will need to have [Python](https://www.python.org/) installed with the Pillow library. You can install the library using pip with this command:

    pip install pillow

If you're on Windows, you can use the exe in the releases. Python does not need to be installed to use it.

The image you would like to add as the splash screen must be:

* A PNG (JPG, TIFF, etc will not work)
* 640x480 width and height
* 24-bit or 32-bit color depth
* 67KB (68,608 bytes) or less in file size

## Adding image
The image is located in the xbox.xex file of the emulator, located at HddX/Compatibility on the hard drive.

You will need to unpack xbox.xex with XexTool. You can use this command to unpack it:

    xextool -c u xbox.xex

Place the splash changer tool and the image and xbox.xex file together in the same directory. From the command line running in the same directory, type in the following to patch it:

    fusionsplashchanger.py xbox.xex image.png

If you're using the exe, type in fusionsplashchanger.exe instead.

Once the image has been added, you can then pack the xbox.xex with XexTool using this command:

    xextool -c c xbox.xex

You can now copy the file back to your console, overwriting the original. A backup of the original unpacked xbox.xex will be created by the tool when adding the image.

## Credits
Credit to DaCukiMonsta for the original guide on editing the splash image. I used the info to create this tool.
