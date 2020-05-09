# Keyboard Emulator - Adafruit Trinket M0

The challenge was simple enough... beat the system by automating mouse clicks and
keystrokes in a game, so it'd think the player was still interacting enough (e.g., milking
cows).

This is a simple project to emulate a USB mouse and keyboard.  A mouse button is held down
for 2 minutes, followed by a couple keystrokes to jog the character and stay "active".


## The Hardware

[Adafruit Trinket M0](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino)

Why the Trinket?  Two reasons...
- Emulating USB devices requires support in both hardware and software.
  E.g., The Pi Zero has a port capable of USB device emulation, but the regular Raspberry
  Pi does not.  The Trinket's microcontroller (Atmel SAMD21) also has this support, making it
  a great candidate.
- I had a Trinket M0 on-hand when the need arose.  The example I found seemed
  easier than doing the project with a Pi Zero (which I also had handy), and I liked the
  extra small size of the Trinket M0.


## The Software

The Trinket runs Adafruit's variant of MicroPython, called CircuitPython.  At the same
time, it is both incredibly easy to use and also very difficult.  As of this project,
CircuitPython is at version 5.3.0.

The easy part... when you plug in the Trinket, it mounts a disk on your laptop.  Drop your
code in the root directory with the name 'main.py' and it'll automatically start running.

The hard parts...
- Trinket is extremely space-limited.  Like, 48KB of storage in total.  You have to be
  extra judicious about which libraries you copy in, and then *how* you copy the files can
  be critical.  Info below.
- Debugging isn't trivial.  Well, it could have been easier, but I was tackling this on a
  shoestring setup with no prior experience, so there was a lot of stumbling along the
  way.  I was certain that I was always "just one step away from success", so I didn't
  spend effort to setup a proper IDE to test with.  My advice: spend the time.
  (The project I started with was built with an older set of libraries with different
  syntax/dependencies.)


## The Prep Work

- First, get the Trinket up to speed with the latest code.
  Get it [here](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython)

    - I found it handy to follow the Erase instructions on the
      [troubleshooting page](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/troubleshooting)
      before imaging the Trinket for a fresh start:

- Next, download the proper library version.
  Get it [here](https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries)

- Copy over just the files you need.  This is not as easy as it sounds... because the
  Trinket is so space-constrained, if you use a Mac you cannot copy the files using
  drag-and-drop - MacOS will create hidden 'metadata' files that will consume precious
  storage space, and the libraries won't fit.

    ```
    #MacOS-specific instructions - you'll need to adapt for other OSes
    #Run this from the /lib folder in the downloaded library
    
    #Create the library folders (they may already exist)
    mkdir /Volumes/CIRCUITPY/lib
    mkdir /Volumes/CIRCUITPY/lib/adafruit_hid

    #Copy the files onto the Trinket without creating the metadata sidecar files
    cp -Xadafruit_dotstar.mpy /Volumes/CIRCUITPY/lib/
    cp -X adafruit_hid/__init__.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/keyboard.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/keyboard_layout_us.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/keycode.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    cp -X adafruit_hid/mouse.mpy /Volumes/CIRCUITPY/lib/adafruit_hid/
    ```


## Obervations

- You'll see that keyboard and mouse events have distinctly separate click & release events.
  The keyboard and mouse here can be connected in parallel to the physical versions with no
  issue, except... when the mouse button is clicked, it can cause weird behavior if you try
  to do other things with the physical keyboard and mouse.  It's best to unplug the device
  when you need to use the physical keyboard; this implicitly deactivates the button-down
  event.

- When in use, it'd be handy if the CIRCUITPY disk didn't auto-mount (because Windows 10
  auto-opens a navigation window).  I suspect there's a way to control this via the
  bootloader's boot.py file, but I don't find any documentation on it in CircuitPython.
  I suspect that'll require a venture into the MicroPython docs.


## References

- Thanks goes to <https://github.com/andyclymer/minikbd> for the example that inspired this project.

- Keycode docs are [here](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode).


## For questions or defects

Please open an issue [here](https://github.com/RichardFoo/Trinket-USB-Keyboard/issues).

## Use at your own risk.  
