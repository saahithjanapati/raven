from voice import VoiceModule
from gesture import GestureModule

from tello_controller import TelloController
import sys
import pygame

import base64


def main():
    tello_controller = TelloController()

    modality_type = input("Enter modality type: ")

    if modality_type == "voice":
        voice = VoiceModule()

        while True:
            commands_json = voice.run_voice_step()
            print(commands_json)
            status = tello_controller.control_tello(commands_json)
            if status == "done":
                print("Done")
                sys.exit(0)
    
    elif modality_type == "gesture":
        gesture = GestureModule()
        tello_controller.run_camera_buffer()

        while True:
            img = tello_controller.get_camera_frame()
            img_base64 = tello_controller.encode_img_base64(img)
        


    


    

    
    # gesture.run_gesture_step("test_files/test.jpeg")


    
    # response = voice.run_voice_step()
    # print(response) 

    # tello_controller.control_tello(response)

    # base64_img = tello_controller.get_camera_frame_base64()
    # gesture.process_frame(base64_img)
    
    # tello_controller.tello.stop()
    # tello_controller.tello.land()


if __name__ == "__main__":
    main()