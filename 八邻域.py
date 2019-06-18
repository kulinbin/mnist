from PIL import Image
import numpy as np

import pandas as pd

from 图像骨架化3_0 import be_thin

def find_eight(img_name):
    img = img_name

    myimage = img.convert('L')
    img2array=np.array(myimage)

    img2array=be_thin(img2array)

    degree=[0]*10
    all_point=[]

    for i in range(1,len(img2array)-1):
        for j in range(1,len(img2array[0])-1):
            if img2array[i][j]==0:
                degree[0] = abs(img2array[i][j] - img2array[i][j + 1])
                degree[1] = abs(img2array[i][j] - img2array[i-1][j + 1])
                degree[2] = abs(img2array[i][j] - img2array[i-1][j])
                degree[3] = abs(img2array[i][j] - img2array[i-1][j - 1])
                degree[4] = abs(img2array[i][j] - img2array[i][j - 1])
                degree[5] = abs(img2array[i][j] - img2array[i+1][j - 1])
                degree[6] = abs(img2array[i][j] - img2array[i+1][j])
                degree[7] = abs(img2array[i][j] - img2array[i+1][j + 1])
                degree[8]=i
                degree[9]=j
                all_point.append(degree[:])

    all_point=np.array(all_point)

    for i in range(len(all_point)):
        for j in range(len(all_point[0])-2):
            if all_point[i][j]==255:
                all_point[i][j]=0
            else:
                all_point[i][j] = 1

    new_pd=pd.DataFrame(all_point,columns=['0','45','90','135','180','225','270','315','行','列'])
    # print(new_pd)
    all_close=['0','45','90','135','180','225','270','315']

    point_sum=[]

    for i in all_close:

        a = round(new_pd[i].sum()/len(all_point),3)
        point_sum.append(a)

    return point_sum

all_number_eight=[[0.154, 0.192, 0.462, 0.192, 0.154, 0.192, 0.462, 0.192], [0.0, 0.071, 0.786, 0.071, 0.0, 0.071, 0.786, 0.071], [0.318, 0.364, 0.136, 0.136, 0.318, 0.364, 0.136, 0.136], [0.25, 0.375, 0.042, 0.292, 0.25, 0.375, 0.042, 0.292], [0.25, 0.25, 0.417, 0.125, 0.25, 0.25, 0.417, 0.125], [0.458, 0.25, 0.125, 0.125, 0.458, 0.25, 0.125, 0.125], [0.259, 0.296, 0.259, 0.185, 0.259, 0.296, 0.259, 0.185], [0.278, 0.278, 0.333, 0.056, 0.278, 0.278, 0.333, 0.056], [0.25, 0.286, 0.25, 0.25, 0.25, 0.286, 0.25, 0.25], [0.36, 0.24, 0.24, 0.2, 0.36, 0.24, 0.24, 0.2]]

def find_all_loss(img_name):
    test_img_name = img_name
    point_sum = find_eight(test_img_name)
    all_loss = []
    loss_sum = 100
    find_num = 0
    for i in range(len(all_number_eight)):
        temp_loss=0
        for j in range(8):
            temp_loss+=np.power(abs(all_number_eight[i][j]-point_sum[j]),0.5)
        all_loss.append(temp_loss)
        if temp_loss<loss_sum:
            loss_sum=temp_loss
            find_num=i
    for i in range(len(all_loss)):
        all_loss[i]=round(all_loss[i],3)
    return (all_loss,find_num,point_sum)#1,未知数字与所有数字的损失2，最小的3，该数字的八领域


