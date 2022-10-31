import logging
import os
import shutil
import boto3
import numpy as np
import pandas as pd
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pandas.io.formats import css
from scenedetect import VideoManager, SceneManager, StatsManager, open_video, split_video_ffmpeg
from scenedetect.detectors import ContentDetector
from scenedetect.scene_manager import save_images, write_scene_list_html
from scenedetect.thirdparty.simpletable import HTMLPage


def contentdet(test_video_file):
    try:
        video_path = test_video_file
        stats_path = 'resource/resultscene.csv'

        video_manager = VideoManager([video_path])
        stats_manager = StatsManager()
        scene_manager = SceneManager(stats_manager)

        scene_manager.add_detector(ContentDetector(threshold=30))

        video_manager.set_downscale_factor()

        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)

        # result
        with open(stats_path, 'w') as f:
            stats_manager.save_to_csv(f, video_manager.get_base_timecode())

        scene_list = scene_manager.get_scene_list()
        # outputDIR='resource'
        print(f'{len(scene_list)} scenes detected!')
        # split_video_ffmpeg(video_path,scene_list,show_progress=True)
        # import glob
        #
        #
        # dest_dir = "/Users/akankbhat/PycharmProjects/MediaProject/test"
        # shutil.rmtree(dest_dir)
        # os.mkdir("/Users/akankbhat/PycharmProjects/MediaProject/test")
        # for file in glob.glob(r'/Users/akankbhat/PycharmProjects/MediaProject/*.mp4'):
        #     print(file)
        #
        #
        #     shutil.move(file, dest_dir)
        # save_images(
        #     scene_list,
        #
        #     video_manager,
        #     num_images=1,
        #     image_name_template='$SCENE_NUMBER',
        #     output_dir='videonew')




        write_scene_list_html('resultsc.html', scene_list)

        for scene in scene_list:
            start, end = scene

            # your code
            print(f'{start.get_seconds()} - {end.get_seconds()}')

    except Exception as e:
        # if scene_manager.get_num_detectors() == 0:
        #     logging.error(
        #         'No scene detectors specified (detect-content, detect-threshold, etc...),\n'
        #         ' or failed to process all command line arguments.')
            print('exception',e)
        # page = HTMLPage()
        # page.tables(scene_list)

        # page.save('resultsc.html')

    # finally:
    #     video_manager.release()


