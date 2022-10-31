import os
import shutil

import cv2
from scenedetect import (
    open_video,
    StatsManager,
    SceneManager,
    AdaptiveDetector,
    save_images,
    split_video_ffmpeg,
    VideoManager,
)
from scenedetect.scene_manager import write_scene_list_html

def adaptive(test_video_file):
    video_path = test_video_file
    stats_path = "../resource/resultadv.csv"
    video_stream = open_video(video_path, backend="pyav")
    video_manager = VideoManager([video_path])
    stats_manager = StatsManager()
    # Construct our SceneManager and pass it our StatsManager.
    scene_manager = SceneManager(stats_manager)

    # Add ContentDetector algorithm (each detector's constructor
    # takes various options, e.g. threshold).
    detector = AdaptiveDetector(
        adaptive_threshold=3.0,
        luma_only=True,
        min_scene_len=15,
        min_delta_hsv=15.0,
        window_width=4,
        video_manager=None,
    )
    scene_manager.add_detector(detector)
    # Perform scene detection.
    scene_manager.detect_scenes(video=video_stream)
    scene_list = scene_manager.get_scene_list()
    video_manager.set_downscale_factor()
    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)


    with open(stats_path, "w") as f:
        stats_manager.save_to_csv(f, video_manager.get_base_timecode())

        outputDIR = "resource"
        print(f"{len(scene_list)} scenes detected!")
        split_video_ffmpeg(video_path, scene_list,output_file_template='$SCENE_NUMBER.mp4',show_progress=True)
        import glob

        dest_dir = "/test"
        shutil.rmtree(dest_dir)
        os.mkdir("/test")
        for file in glob.glob(r'/Users/akankbhat/PycharmProjects/MediaProject/*.mp4'):
            print(file)

            shutil.move(file, dest_dir)

        write_scene_list_html('result.html', scene_list)

        for scene in scene_list:
            start, end = scene

            # your code
            print(f'{start.get_seconds()} - {end.get_seconds()}')

