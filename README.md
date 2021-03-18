# button-press
Python scripts designed to run in the background, waiting for button presses to execute
shell commands or scripts when the button is pressed.

Example usage:

1.  button-press.py

    This script waits for a button press on the /dev/input/event0.
    When the button is pressed - "Pressed" is printed in the terminal window,
    and the program exits.

    ./button-press.py /dev/input/event0 "echo 'Pressed'"

2.  button-press-forever.py

    This script waits for a button press on the /dev/input/event0.
    Each time the button is pressed - "Pressed" is printed in the terminal window.

    ./button-press-forever.py /dev/input/event0 "echo 'Pressed'"

Note that for some system root privileges are neccesary to run these scripts.
This scripts can be setup to run on bootup. Look up runlevels and rcd scripts for your system.

Example:

Make a example_script.sh with following content:
(Make sure that both example_script.sh and button-press.py are executable.)

#!/bin/sh

/usr/bin/python3 /path/to/script/button-press.py /dev/input/event0 "echo 'Pressed'" &


Copy example_script.sh to /etc/init.d. Then go to your default runlevel (can be found in /etc/inittab)
folder in (example /etc/rc5.d/) and make a symbolic link to the script in /etc/init.d.

That is all.