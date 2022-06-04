import os

def generate(project_name):
    os.makedirs("./"+project_name+"/JPEGImages")
    os.makedirs("./"+project_name+"/ImageSets/Main")
    os.makedirs("./"+project_name+"/Annotations")
    label= open("./"+project_name+"/labels.txt", 'w+')
    label.write(project_name)
    label.close()
    test = open("./"+project_name+"/ImageSets/Main/test.txt", "w+")
    train = open("./"+project_name+"/ImageSets/Main/train.txt", "w+")
    trainval = open("./"+project_name+"/ImageSets/Main/trainval.txt", "w+")
    val = open("./"+project_name+"/ImageSets/Main/val.txt", "w+")
    test.close()
    train.close()
    trainval.close()
    val.close()
    
def conclued(all_files,projectname):
    test = open("./"+projectname+"/ImageSets/Main/test.txt", "a")
    train = open("./"+projectname+"/ImageSets/Main/train.txt", "a")
    trainval = open("./"+projectname+"/ImageSets/Main/trainval.txt", "a")
    val = open("./"+projectname+"/ImageSets/Main/val.txt", "a")
    for file in all_files:
        test.write(file+"\n")
        train.write(file+"\n")
        trainval.write(file+"\n")
        val.write(file+"\n")
    test.close()
    train.close()
    trainval.close()
    val.close()
