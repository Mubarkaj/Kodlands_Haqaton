
from ultralytics import YOLO
import argparse
import re

yolo=YOLO(r"C:\\Users\\rayya\Documents\\kodland\\M8\\Kodlands_Haqaton\\runs\detect\\train12\\weights\\best.pt")




parser = argparse.ArgumentParser(description='A sample script with flags.')
# Define a string flag with a default value and help message
parser.add_argument('-i', default='default_model', help='Specify input file') 
parser.add_argument('-o', default='default_model', help='Specify output file') 


args = parser.parse_args()

input_file=args.i
output_file=args.o

results = yolo(input_file, conf=0.7, iou=0.3, verbose=False)
results[0].save(output_file)

print(len(results[0].boxes))