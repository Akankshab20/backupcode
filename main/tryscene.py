import logging
import os
import shutil

import cv2
from pandas.io.formats import css
from scenedetect import (
    open_video,
    StatsManager,
    SceneManager,
    AdaptiveDetector,
    save_images,
    ThresholdDetector,
    split_video_ffmpeg,
    VideoManager, ContentDetector,
)
from scenedetect.scene_manager import write_scene_list_html
from scenedetect.thirdparty.simpletable import HTMLPage, SimpleTable


def ttryy(test_video_file):
    try:
        video_path = test_video_file
        stats_path = "../resource/resultthres.csv"
        video_stream = open_video(video_path, backend="pyav")
        stats_manager = StatsManager()
        video_manager = VideoManager([video_path])
        # Construct our SceneManager and pass it our StatsManager.
        scene_manager = SceneManager(stats_manager)

        scene_manager.add_detector(ContentDetector(threshold=30))

        video_manager.set_downscale_factor()

        video_manager.start()
        scene_manager.detect_scenes(frame_source=video_manager)
        scene_list = scene_manager.get_scene_list()

        with open(stats_path, "w") as f:
            stats_manager.save_to_csv(f, video_manager.get_base_timecode())

            # outputDIR = "resource"
            print(f"{len(scene_list)} scenes detected!")
            # split_video_ffmpeg(video_path, scene_list, show_progress=True)
            # import glob
            #
            # dest_dir = "/Users/akankbhat/PycharmProjects/MediaProject/test"
            # shutil.rmtree(dest_dir)
            # os.mkdir("/Users/akankbhat/PycharmProjects/MediaProject/test")
            # for file in glob.glob(r'/Users/akankbhat/PycharmProjects/MediaProject/*.mp4'):
            #     print(file)
            #
            #     shutil.move(file, dest_dir)
            write_scene_list_html("result.html", scene_list)

            for scene in scene_list:
                start, end = scene

                # your code
                # print(f"{start.get_seconds()} - {end.get_seconds()}")

    except Exception as e:
        # if scene_manager.get_num_detectors() == 0:
            logging.error(
                'No scene detectors specified (detect-content, detect-threshold, etc...),\n'
                ' or failed to process all command line arguments.')

            print('exception', e)
            # write_scene_list_html("resultsc.html", scene_list=None)
    # finally:
    #      video_manager.release()


ttryy("resource/chunk8.mp4")