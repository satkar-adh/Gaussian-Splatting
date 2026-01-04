REM get video from phone
python ftp_file_transfer.py

REM convert video to images
python video_to_image.py toConvert.mp4

REM remove mp4 file
del toConvert.mp4

REM run colmap to get required format
python gaussian_splatting/convert.py -s data

REM conda activate sugar
REM train gaussian splatting
python gaussian_splatting/train.py -s data --iterations 7000 -m output

REM train sugar model
python train.py -s data -c output -r "density"
