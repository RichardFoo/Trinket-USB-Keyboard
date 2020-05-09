# USB Keyboard & Mouse Emulator - Adafruit Trinket M0

The challenge was simple enough... beat the system by automating mouse clicks and
keystrokes in an online game, so it'd think the player was still interacting
(e.g., milking cows).

This is a simple project to emulate a USB mouse and keyboard - a human interface device,
or 'HID' in USB lingo.  A mouse button is held down for 2 minutes, followed by a couple
keystrokes to jog the character and stay "active". Repeat, ad infinitum.


## The Hardware

[Adafruit Trinket M0](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino)

Why the Trinket?  Reasons... mostly, convenience.
- Emulating USB devices requires support in both hardware and software - it sounds simple,
  but it's not.  E.g., The Pi Zero has a port capable of USB device emulation, but the
  regular Raspberry Pi does not.  The Trinket's microcontroller (Atmel SAMD21) also has
  this support, making it a great candidate.
- I had a Trinket M0 on-hand when the need arose.  Leftovers from a hands-on lab at a
  conference where I had hooked it to a GSM modem for testing.  I'd literally just found
  this lonely board while organizing my parts box and thought "This is tiny and nifty.
  What could I use it for now?"
- The Trinket example I found seemed cleaner / simpler / easier than the instructions I
  found for Pi Zero (which I also had handy), and I liked the extra small size of the
  Trinket M0 - it's tiny.  And even a Pi Zero is overkill for this project.


## The Software

The Trinket runs Adafruit's variant of MicroPython, called CircuitPython.  It is at the
same time both incredibly easy to use and also very difficult.  As of this project,
CircuitPython is at version 5.3.0.

The easy part... when you plug in the Trinket, it mounts a USB drive on your computer.
Drop your code in the root directory with the name 'main.py' and it'll automatically start
running.  It doesn't even need a reboot.

The hard parts...
- Trinket is extremely space-limited.  Like, 48KB of storage in total.  You have to be
  extra judicious about which libraries you copy in, and then *how* you copy the files can
  be critical.  More info below.
- Debugging isn't trivial.  Well, it could have been easier, but I was tackling this on a
  shoestring setup with no prior experience, so there was a lot of stumbling along the
  way.  I was certain that I was always "just one step away from success", so I didn't
  spend effort to setup a proper IDE to test with.  My advice: spend the time.
  (The example I referenced was built with an older set of libraries, and the
  syntax/dependencies were different.)


## The Prep Work

- First, get the Trinket up to speed with the latest code.
  Instructions are [here](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython).
  This project was built with v5.3.0.

    - For a fresh start, I found it handy to follow the Erase instructions on the
      [troubleshooting page](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/troubleshooting)
      before imaging the Trinket.  (OK, yes, I actually re-imaged it a bunch of times
      trying to figure out why I couldn't fit the libraries on it.  Erasing was part of my
      last clean round of imaging.)

- Next, download the proper library version.
  Get it [here](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries).

- Copy only the library files you need onto the Trinket.  This is not as easy as it
  sounds, because the Trinket is so space-constrained.  If you use a Mac, you cannot copy
  the files using drag-and-drop - MacOS will create hidden 'metadata' files that will
  consume precious storage space, and the libraries won't fit.  Use these terminal
  commands instead:

    ```
    #MacOS-specific instructions - you'll need to adapt for other OSes
    #Run this from the /lib folder in the downloaded library
    
    #Create the library folders (they may already exist)
    mkdir /Volumes/CIRCUITPY/lib
    mkdir /Volumes/CIRCUITPY/lib/adafruit_hid

    #Copy the files onto the Trinket without creating the metadata sidecar files
    cp -X adafruit_dotstar.mpy /Volumes/CIRCUITPY/lib/
    cp -X adafruit_hid/__init__.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/keyboard.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/keyboard_layout_us.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/keycode.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/mouse.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    ```


## Observations

- You'll see that keyboard and mouse events have distinctly separate click & release events.
  The keyboard and mouse here can be connected at the same time as physical devices with
  no issue, except... while the mouse button is being pressed, it can cause weird behavior
  if you try to do other things with the physical keyboard and mouse.  It's best to unplug
  the device when you need to use the physical keyboard; this terminates the button-down
  event.

- When in use, it'd be handy if the CIRCUITPY disk didn't auto-mount (because Windows 10
  auto-opens a File Explorer window).  I suspect there's a way to control this via the
  bootloader's boot.py file, but I don't find any documentation on it in CircuitPython.
  [This](https://github.com/adafruit/circuitpython/issues/1015) makes me believe the
  feature doesn't exist, but the
  [pyb.usb_mode](http://docs.micropython.org/en/latest/library/pyb.html?highlight=bootloader#pyb.usb_mode)
  docs at MicroPython suggest it might, depending on when CircuitPython was forked.
  I didn't investigate further.


## References

- Thanks goes to [Andy Clymer](https://github.com/andyclymer/minikbd) for the example that
  inspired this project.

- Keycode docs are [here](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode).


## For questions or defects

Please open an issue [here](https://github.com/RichardFoo/Trinket-USB-Keyboard/issues).

## Use at your own risk.  
