import os

import cv2


def gci(filepath, file_name_list):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            print(os.path.join(filepath, fi_d))
            file_name_list.append(os.path.join(filepath, fi_d))
            gci(fi_d, file_name_list)
        else:
            print(os.path.join(filepath, fi_d))
            file_name_list.append(os.path.join(filepath, fi_d))  # 递归遍历/root目录下所有文件


if __name__ == '__main__':
    file_name_list = []
    gci('E:\\wwf_files\\learning_and_ai\\淘宝购买的\\淘宝麦穗互联科技python人工智能视频课程（只保存了最新的一套，群里共有45套1400多G很全的python教程！详见“Python学习11群”！）\\python全套\\temp', file_name_list=file_name_list)
    print(file_name_list)
    video_name_list = []
    for file_name in file_name_list:
        if file_name.endswith(('.mp4', '.flv')):
            video_name_list.append(file_name)
    print(video_name_list)

    total_video_length = 0
    for video_name in video_name_list:
        cv2video = cv2.VideoCapture(video_name)
        framecount = cv2video.get(cv2.CAP_PROP_FRAME_COUNT)
        frames_per_sec = cv2video.get(cv2.CAP_PROP_FPS)
        print("Video duration (sec):", framecount / frames_per_sec)
        total_video_length += framecount / frames_per_sec

    print(total_video_length)
    hours = total_video_length // 3600
    minutes = total_video_length % 3600 // 60
    seconds = total_video_length % 3600 % 60 // 1
    print(hours, minutes, seconds)
    print('{}:{}:{}'.format(int(hours), int(minutes), int(seconds)))

