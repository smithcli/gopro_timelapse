import time
from datetime import datetime
from goprocam import GoProCamera, constants
import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

# Log to console
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] - %(message)s',
        '%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
root.addHandler(handler)

# Log to file
logfile = logging.FileHandler('gopro.log', encoding='utf-8')
logfile.setLevel(logging.INFO)
logfile.setFormatter(formatter)
root.addHandler(logfile)

gpcam = GoProCamera.GoPro()
gpcam.overview()

today = datetime.now()
pretty_date = today.date().isoformat()
current_time = today
start_time = today.replace(hour=6, minute=0, second=0, microsecond=0)
end_time = today.replace(hour=18, minute=0, second=0, microsecond=0)

logging.debug(f'\
Current time is {current_time}\n \
Recording Start time is at {start_time} hours\n \
Recording End time is at {end_time} hours\n')

def set_timelapse():
    gpcam.mode(constants.Mode.VideoMode, constants.Mode.SubMode.Video.TimeLapseVideo)
    gpcam.gpControlSet(constants.Setup.Display, constants.Setup.Display.OFF)
    gpcam.gpControlSet(constants.Setup.AUTO_OFF, constants.Setup.AutoOff.Never)
    gpcam.gpControlSet(constants.Setup.LedBlinkNew, constants.Setup.LedBlinkNew.Led_ON)
    logging.debug('Timelapse Set')

def start_timelapse():
    set_timelapse()
    gpcam.shutter(constants.start)
    logging.info('Started Timelapse recording')
        
def stop_timelapse():
    gpcam.shutter(constants.stop)
    logging.info('Stopped Timelapse recording')

def get_video():
    time.sleep(60)
    gpcam.downloadLastMedia(path=gpcam.getMedia(), custom_filename=pretty_date +"-housebuild.mp4")
    logging.info('Downloaded video')
    time.sleep(60)
    gpcam.delete("last")
    logging.info('Deleted video from gopro')

def main():
    recording = gpcam.IsRecording()
    if (not(recording) and 
            current_time >= start_time and
            current_time < end_time):
        start_timelapse()
    elif (recording and current_time < end_time):
        logging.debug('Recording...')
    elif (recording and current_time >= end_time):
        stop_timelapse()
        get_video()

if __name__ == "__main__":
    main()
