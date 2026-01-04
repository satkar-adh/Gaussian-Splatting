from ftplib import FTP
import os

ftp_server = '192.168.1.68'  # Change to your FTP server's IP
ftp_port = 2222               # Default FTP port is 21, change if yours is different
ftp_user = 'android'           # Your FTP username
ftp_password = 'android'   # Your FTP password
remote_path = 'DCIM/Camera'  # The path to your videos on the phone
local_path = ''


ftp = FTP()
ftp.connect(ftp_server,ftp_port)
ftp.login()

ftp.cwd(remote_path)

# Get list of files in the directory
files = ftp.nlst()

videos = [item for item in files if item.startswith("VID")]

#get most recent video
most_recent_video = videos[-1]

print(most_recent_video)

# Download the most recent video
local_filename = os.path.join("toConvert.mp4")
with open(local_filename, 'wb') as file:
    ftp.retrbinary('RETR ' + most_recent_video, file.write)

ftp.quit()
print(f'Downloaded {most_recent_video} to {local_filename}')