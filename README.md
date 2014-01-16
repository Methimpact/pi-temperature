pi-temperature
==============

A collection of Linux-based python and html programs for reading and reporting the temperature from a raspberry pi with two DS18B20 temperature sensors (indoor/outdoor)

Inspired by Adafruit tutorials.

The set-up is: a raspberry pi with two digital thermometers (one is put outside of a window, the other interior) and access to a remote web-server (which can be your own server, or there are a number of cloud services that give you a virtual Linux). You could use the pi itself as the web-server, but it may be preferable to dedicate the pi to sensing and let a remote server to the data-processing and web-hosting.

pytemp.py is the program that will gather the temperature readings and report them to your web-server. You will need to set up ssh keys so that the remote session doesn't require a password.  Put that in your home directory, or modify the init script (temp) to point to wherever you may have put it.

temp is the init script that you would place in /etc/init.d so that the temperature sensor starts automatically at boot. Once you move it there, run:

sudo chmod +x /etc/init.d/temp

sudo update-rc.d temp defaults

to have it run automatically on boot up.

protemp.py goes on your remote web-server. Give it x permissions (so it can be run as a script):

chmod +x protemp.py

Currently this program *does not* generate a file from scratch, you will need to give it a starter file, and so I've included temperature.dat for that purpose--after about six hours the data in that file will have all been overwritten by your data.

Finally, index.html is the html file that does the heavy lifting in terms of presenting the data. It uses the jquery and flot libraries to create a smooth and dynamic presentation of the data. This should be placed in your web-servers web root. It updates automatically (and smoothly, not with a page refresh but by redrawing the graph and updating the data).