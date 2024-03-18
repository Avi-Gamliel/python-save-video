import numpy as np 
import cv2

```
* pip install opencv-python numpy

TkImage = ImageTk.PhotoImage(img)
save_path = 'c:/test_folder/test.jpg'
images_array = [TkImage, TkImage, ]
type = 'avi', 'mov'
fps = 16 // default

```

def save_from_tkintert_images_to_video(type, images_array, save_path, fps=16):
    def tkimage_to_array(tkimage):
        return np.array(tkimage)
    fourcc = ''
    if type == "avi":
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
    elif type == "mov":
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    if fourcc == '':
        return print('there is no type')
    frame_size = (images_array[0].width, images_array[0].height)
    video_writer = cv2.VideoWriter(save_path, fourcc, fps, frame_size)
  
    for tkimage in images_array:
        np_img = tkimage_to_array(tkimage)
        bgr_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
        video_writer.write(bgr_img)
    video_writer.release()
