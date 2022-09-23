"""
Upgrade the constructor in the DriveBot class in order to accept three optional parameters. The constructor can accept motor_speed (which defaults to 0 if not provided), direction (which defaults to 180 if not provided, and sensor_range (which defaults to 10 if not provided). These parameters should replace the associated instance variables. Test out the upgraded constructor by initializing a new robot called robot_2 with a speed of 35, a direction of 75, and a sensor range of 25.
"""

class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
    
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

# Create robot_2 here!
robot_2 = DriveBot()
robot_2.motor_speed = 35
robot_2.direction = 75
robot_2.sensor_range = 25

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)
