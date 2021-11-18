import os


def gci(filepath):
    # 遍历filepath下所有文件，包括子目录
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            print(os.path.join(filepath, fi_d))
            gci(fi_d)
        else:
            print(os.path.join(filepath, fi_d))  # 递归遍历/root目录下所有文件


if __name__ == '__main__':
    gci('E:\\wwf_files\\learning_and_ai\\淘宝购买的\\淘宝麦穗互联科技python人工智能视频课程（只保存了最新的一套，群里共有45套1400多G很全的python教程！详见“Python学习11群”！）\\python全套\\16-人工智能基础v5.0')
