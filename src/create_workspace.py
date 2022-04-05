import os

def generate(project_name):
    os.makedirs("./"+project_name+"/JPEGImages")
    os.makedirs("./"+project_name+"/ImageSets/Main")
    os.makedirs("./"+project_name+"/Annotations")
    label= open("./"+project_name+"/labels.txt", 'w+')
    label.write(project_name)
    label.close()
    
def conclued(all_files,projectname):
    test = open('./'+projectname+'/ImageSets/Main/test.txt', 'w+')
    train = open('./'+projectname+'/ImageSets/Main/train.txt', 'w+')
    trainval = open('./'+projectname+'/ImageSets/Main/trainval.txt', 'w+')
    val = open('./'+projectname+'/ImageSets/Main/val.txt', 'w+')
    for file in all_files:
        test.write(file)
        train.write(file)
        trainval.write(file)
        val.write(file)
    test.close()
    train.close()
    trainval.close()
    val.close()