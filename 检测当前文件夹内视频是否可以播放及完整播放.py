import os
from moviepy.editor import VideoFileClip

def check_mp4_files_in_current_directory():
    # 获取当前文件夹的路径
    current_directory = os.getcwd()
    
    # 获取当前文件夹下所有扩展名为 .mp4 的文件
    files = [f for f in os.listdir(current_directory) if f.endswith('.mp4')]
    
    if not files:
        print("当前文件夹中没有找到任何 MP4 文件。")
        return
    
    for file in files:
        file_path = os.path.join(current_directory, file)
        try:
            # 尝试加载视频
            video = VideoFileClip(file_path)
            
            # 获取视频时长
            duration = video.duration
            if duration > 0:
                print(f"{file} 可以播放，时长为 {duration:.2f} 秒")
                
                # 检查是否可以从倒数10秒的时刻加载播放
                start_time = max(0, duration - 10)
                
                # 尝试截取倒数10秒的视频部分
                try:
                    last_part = video.subclip(start_time, duration)
                    # 对截取的部分做简单的处理，确保可以加载
                    last_part.preview()  # 可以用 preview() 查看播放情况，或用 last_part.ipython_display() 在 Jupyter 中显示
                    print(f"{file} 的倒数 10 秒可以正常播放。")
                except Exception as e:
                    print(f"{file} 的倒数 10 秒无法播放，错误: {e}")
            
            else:
                print(f"{file} 文件损坏，无法完整播放")
        
        except Exception as e:
            # 如果加载失败，说明视频无法播放
            print(f"{file} 无法播放，错误: {e}")

# 检测当前文件夹下的 MP4 文件
check_mp4_files_in_current_directory()
