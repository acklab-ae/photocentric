import argparse
import torch
import torchvision.models
import torchvision.transforms as transforms
from PIL import Image
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
import os
import pandas as pd
from tqdm import tqdm 
import time

def prepare_image(image):

    if image.mode != 'RGB':
        image = image.convert("RGB")
    Transform = transforms.Compose([
            transforms.Resize([224,224]),
            transforms.ToTensor(),
            ])
    image = Transform(image)
    image = image.unsqueeze(0)

    return image.to(device)

def predict(image, model, file, log):
    file = file
    image = prepare_image(image)

    with torch.no_grad():
        preds = model(image)
    score = preds.item()

    with open(log,'a') as f:
        f.write(f'\n{file},{round(score,2)}')
    f.close()

def process(x, y, log):
    path = x
    file = y
    image_path = path + file
    #print(f'{file}')
    image = Image.open(image_path)
    model = torchvision.models.resnet50()
    # model.avgpool = nn.AdaptiveAvgPool2d(1) # for any size of the input
    model.fc = torch.nn.Linear(in_features=2048, out_features=1)
    model.load_state_dict(torch.load('model/model-resnet50.pth', map_location=device))
    model.eval().to(device)
    predict(image, model, image_path, log)

image_location = '/data/images/'
log = 'images.log'

with open(log,'w') as f:
    f.write('image,score')
f.close()

list_of_files = os.listdir(image_location)

count = 0
for i in tqdm(list_of_files):
    process(image_location,list_of_files[count],log)
    count +=1

df = pd.read_csv('images.log')
df.sort_values(by=['score'], ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)

print(df)
