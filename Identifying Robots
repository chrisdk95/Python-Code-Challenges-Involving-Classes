"""
The final modifications to this class can be seen at the top of the class and in the constructor. We use a class variable to keep track of the total number of robots. This information is shared across all robot objects we create from the class. Every time a robot object is created, the constructor is called and the count is incremented. Each robot has an instance variable for id which is local to that robot object. This is assigned at the time of construction and stores what the count was at that time.
"""

class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
 
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count
 
    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction
 
    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

