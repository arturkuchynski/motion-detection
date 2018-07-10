# motion-detection
Static camera motion detection using OpenCV 3 with Python 3 

##### Motion can be captured from the webcam or from any other video-capturing device

To run motion capture from video use
`python3 src/motion_detector.py -v "path/to/.mp4"`
or
`python3 src/motion_detector.py --video "path/to/.mp4"`

To change default motion area run the script with flag `-a [value of type int]`
or `--min-area [value of type int]`

All detected movement is serialized in .csv table using Pandas

### .CSV example of moving object occurrences with related time intervals

| Occurrence | Start                      | End                        | 
|-----------|----------------------------|----------------------------| 
| 0         | 2018-06-28 11:19:03.034333 | 2018-06-28 11:19:03.239962 | 
| 1         | 2018-06-28 11:19:04.013949 | 2018-06-28 11:19:04.170417 | 
| 2         | 2018-06-28 11:19:04.873939 | 2018-06-28 11:19:05.113811 | 
| 3         | 2018-06-28 11:19:05.616372 | 2018-06-28 11:19:05.790772 | 
| 4         | 2018-06-28 11:19:06.324708 | 2018-06-28 11:19:06.559286 | 

##### Plotting data in your web browser with bokeh
To do so, run `python3 src/plot.py` and you'll get a simple and reusable plot  
