from src.detectedFrame import DetectedFrame
import src.pcv_detection as pcv_detection
import src.dataset_xml_generator as dataset_xml_generator
import src.create_workspace as create_workspace
from plantcv import plantcv as pcv
import cv2
import numpy as np

def main(projectname,filename):
    create_workspace.generate(projectname)
    counter=0
    cap = cv2.VideoCapture(filename+'.mp4')
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out_detected = cv2.VideoWriter(filename+'out_detected.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    out_dilated = cv2.VideoWriter(filename+'out_dilated.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    all_files = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        rawFrame = frame.copy()
        actual_filename = filename+"_"+counter
        if ret == True:
            detected = pcv_detection.detect(actual_filename)
            if len(detected.annotations) >0:
                dataset_xml_generator.generate(actual_filename,frame_width,frame_height,detected.annotations)
                out_detected.write(detected.detected_image)
                out_dilated.write(detected.dilated_image)
                cv2.imwrite("./JPEGImages/"+actual_filename+".jpg", rawFrame)
                all_files.append(actual_filename)
                counter+=1
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        else: 
            break
    create_workspace.conclued(all_files,projectname)
    cap.release()

if __name__ == '__main__':
    filename = "dsjjzfioj"
    main("BATAVIA",filename)
