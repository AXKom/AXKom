from src.detectedFrame import DetectedFrame
import src.pcv_detection as pcv_detection
import src.dataset_xml_generator as dataset_xml_generator
import src.create_workspace as create_workspace
from plantcv import plantcv as pcv
import cv2

def main(projectname,filename):


    create_workspace.generate(projectname)
    img, path, fi = pcv.readimage("./"+filename+".png")
    rawFrame = img.copy()
    heigh, width, c = img.shape
    detected = pcv_detection.detect(img,filename)
    dataset_xml_generator.generate(projectname,filename,width,heigh,detected.annotations)
    pcv.print_image(detected.detected_image, "./crop_area.png")
    pcv.print_image(detected.dilated_image, "./dilated.png")
    cv2.imwrite("./"+projectname+"/JPEGImages/"+filename+".jpg", rawFrame)
    create_workspace.conclued(filename,projectname)

if __name__ == '__main__':
    main("BATAVIA","batavia")