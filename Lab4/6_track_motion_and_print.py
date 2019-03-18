#!/usr/bin/env python3
'''
Demo of using TrackingCamera
to get motion from camera and print motion data in terminal
the data and video are saved (`example_6.csv` and `example_6.json`)
'''

## import camera
from lab.tracking import TrackingCamera


def run_camera():
    ## create camera with configuration, and init with resources
    # will throw exception for errors (such as broken camera or non-existing input/config files, ...)

    ## >>>>>> Be sure to set this to the name of your desired saved mp4 file, if
    ## >>>>>> you would like to analyze recorded video data (instead of live camera data)
    ##
    input_file = 'my_input_file.mp4'

    camera_kwargs = {
        'input_source': 0,  # camera id, set this to 0 if you want to read live camera data
        # or to input_file if you want to read data from a saved mp4 file
        'mode': 'motion',  # optional, the camera mode [recording, tracking (default), motion, calibration]
        'output_video': 'example_6.mp4',  # optional, save the output video file (`mp4` format only)
        'output_data': 'example_6.csv',  # optional, save the tracking data (to `.csv` files)
        'camera_settings': (1920, 1080, 30),  # optional (width, height, fps), (1920, 1080, 30) by default
        'tracking_config_file': 'stickers',  # 'benchmark_stickers',   # optional, markers for tracking or motion
        #           '<name>' for builtin config or '<name>.config' for local file
        'marker_names': [],  # optional, selected markers in tracking config (empty for all)
        'crop': True,
    # optional, if True (default) frame is cropped to near square, otherwise the full resolution is used
        #           always False for video file input
        'builtin_plot_mode': 'default',  # optional, 'none' for no plotting by lib
        #           'default' for plotting center, contour, etc, may add 'trace' for future
        'camera_distance': 51.6  # optional, camera distance (in cm) to object
        # required for `tracking` or `motion` mode to convert pixel to cm
        # This must be set correctly to calculate acceleration or velocity reliably
    }

    with TrackingCamera(**camera_kwargs) as camera:
        while camera.is_running:
            ## read, track, and compute motion for framea
            # return frame number and frame of earliest motion job completed
            # return None values if camera is busy or if read fails (also cause camera to stop)
            motion_frame_no, motion_frame = camera.read_motion()

            ## write frames to output video file (optional)
            camera.write_frame_to_video(motion_frame_no, motion_frame)

            ## display frame
            camera.display_frame(motion_frame_no, motion_frame)

            ## print motion info in terminal
            if motion_frame_no is None:
                continue

            # get timestamp
            motion_frame_ts = camera.get_timestamp_of_frame(motion_frame_no)
            print("Frame #{}, {:.1f}ms".format(motion_frame_no, motion_frame_ts))

            # print motion data (v and a) of markers in the frame
            for marker_name, marker_data in camera.get_motion_data_of_frame(motion_frame_no):
                print("Marker name: {}".format(marker_name))
                print("\tv: {}, a: {}".format(marker_data["v"], marker_data["a"]))


## run in command line
if __name__ == "__main__":
    run_camera()