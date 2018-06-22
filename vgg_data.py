
import shutil
import os

train_file = '/notebooks/caffe-oxford102/train.txt'
val_file = '/notebooks/caffe-oxford102/valid.txt'
vgg_train_dir = '/notebooks/vgg/train/'
vgg_val_dir = '/notebooks/vgg/val/'


def vgg_dataset(src_file, target_dir):
    lines = open(file=src_file, encoding='utf-8').readlines()
    for line in lines:
        jpg_file, label = line.split()
        filename = os.path.basename(jpg_file)
        dst_dir = os.path.join(target_dir, label)
        if not os.path.isdir(dst_dir):
            os.makedirs(dst_dir)
        dst_path = os.path.join(dst_dir, filename)
        if not os.path.isfile(dst_path):
            shutil.copy(jpg_file, dst_path)


vgg_dataset(train_file, vgg_train_dir)
vgg_dataset(val_file, vgg_val_dir)