# gopro_timelapse
Gopro timelapse script to maintain sd card space

Thank you to
[Konrad Iturbe](https://github.com/konradit/gopro-py-api)
for making this possible and easy.

## The Problem
The family wanted to see the construction of my mom's house. 
However, they only knew how to share by taking pictures from their phone 
and sending an SMS to the group. 
That is ok, but it relies on someone at the site taking photos. 
So I decided to use my GoPro to take a timelapse of the build. 
A few problems with that are the battery is weak, 
and the sd card is not that large. 
The next barrier is that my family is not technologically friendly, 
and getting them to connect to the camera, download, then upload the videos 
to a cloud service for everyone to see was not going to work. 
Finally, I visit maybe once a week, which might not be enough to do it myself. 
So I must automate the download and removal from the camera.


## The Solution 
- Setup gopro in film position with powercable attached.
- Install this script into my raspberrypi 3B set nearby.
- Connect raspberrypi to internet via ethernet and gopro via WiFi.
- Let cron or systemd run script.
- _TODO: upload videos to cloud service for storage and family viewing._

## To Execute Script
```
pip install goprocam
python3 gopro.py
```
