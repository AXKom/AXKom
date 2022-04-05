#!/usr/bin/env python
from lxml import etree
from src.annotation import Annotation

def generate(_project_name,_filename,_with,_height,_annotation_datas):
    annotation = etree.Element("annotation")
    filename = etree.SubElement(annotation, "filename")
    filename.text=_filename
    folder = etree.SubElement(annotation, "folder")
    folder.text="data"
    source = etree.SubElement(annotation, "source")
    database = etree.SubElement(source, "database")
    database.text="data"
    annotation1 = etree.SubElement(source, "annotation")
    annotation1.text = "custom"
    image = etree.SubElement(source, "image")
    image.text = "custom"
    size = etree.SubElement(annotation, "size")
    with_ = etree.SubElement(size, "with")
    with_.text = str(_with)
    height = etree.SubElement(size, "height")
    height.text = str(_height)
    depth = etree.SubElement(size, "depth")
    depth.text = "3"
    segmented = etree.SubElement(annotation, "segmented")
    segmented.text="0"
    for annotation_data in _annotation_datas:
        _object = etree.SubElement(annotation, "object")
        _name = etree.SubElement(_object, "name")
        _name.text = annotation_data.name
        pose = etree.SubElement(_object, "pose")
        pose.text = "unspecified"
        truncated = etree.SubElement(_object, "truncated")
        truncated.text = "0"
        difficult = etree.SubElement(_object, "difficult")
        difficult.text = "0"
        bndbox = etree.SubElement(_object, "bndbox")
        xmin = etree.SubElement(bndbox, "xmin")
        xmin.text = str(annotation_data.xmin)
        ymin = etree.SubElement(bndbox, "ymin")
        ymin.text = str(annotation_data.ymin)
        xmax = etree.SubElement(bndbox, "xmax")
        xmax.text = str(annotation_data.xmax)
        ymax = etree.SubElement(bndbox, "ymax")
        ymax.text = str(annotation_data.ymax)
    tree = annotation.getroottree()
    tree.write("./"+_project_name+"/Annotations/"+_filename+".xml",  pretty_print=True)

#generate("batavia1",1632,1232,annotation_datas)
