import asyncio

from viam.robot.client import RobotClient
from viam.rpc.dial import Credentials, DialOptions
from viam.components.sensor import Sensor
from viam.components.camera import Camera
from viam.services.mlmodel import MLModelClient
from viam.services.vision import VisionClient

async def connect():
    opts = RobotClient.Options.with_api_key( 
        api_key='gtgdzduue194dt5dmdm9ibjxrn5dg6x2',
        api_key_id='459618de-7357-4260-9d9e-1ce6a9084fe1'
    )
    return await RobotClient.at_address('mylaptop-main.0p1kevpomd.viam.cloud', opts)

async def main():
    machine = await connect()

    print('Resources:')
    print(machine.resource_names)
    
    # myNTPTimeSensor
    my_ntp_time_sensor = Sensor.from_robot(machine, "myNTPTimeSensor")
    my_ntp_time_sensor_return_value = await my_ntp_time_sensor.get_readings()
    print(f"myNTPTimeSensor get_readings return value: {my_ntp_time_sensor_return_value}")
  
    # myWebcam
    my_webcam = Camera.from_robot(machine, "myWebcam")
    my_webcam_return_value = await my_webcam.get_image()
    print(f"myWebcam get_image return value: {my_webcam_return_value}")
  
    # myImageFileCamera
    my_image_file_camera = Camera.from_robot(machine, "myImageFileCamera")
    my_image_file_camera_return_value = await my_image_file_camera.get_image()
    print(f"myImageFileCamera get_image return value: {my_image_file_camera_return_value}")
  
    # myModel
    my_model = MLModelClient.from_robot(machine, "myModel")
    my_model_return_value = await my_model.undefined()
    print(f"myModel undefined return value: {my_model_return_value}")
  
    # myVision
    my_vision = VisionClient.from_robot(machine, "myVision")
    my_vision_return_value = await my_vision.get_properties()
    print(f"myVision get_properties return value: {my_vision_return_value}")

    # Don't forget to close the machine when you're done!
    await machine.close()

if __name__ == '__main__':
    asyncio.run(main())
