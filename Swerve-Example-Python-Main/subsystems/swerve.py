# TODO: Calibrate the gyro
# TODO: Initialize the encoder
# TODO: Invert motor directions (if necessary)
# TODO: Adjust deadbanding and velocity limiting constants

import wpilib
import math
import constants 

class Swerve:
    def __init__(self):
        self.modules = [SwerveModule(i) for i in range(MODULE_COUNT)]

    def robotInit(self):
        for module in self.modules:
            module.robotInit()

    def autonomousInit(self):
        for module in self.modules:
            module.autonomousInit()

    def autonomousPeriodic(self):
        for module in self.modules:
            module.autonomousPeriodic()

    def teleopInit(self):
        for module in self.modules:
            module.teleopInit()

    def teleopPeriodic(self, x, y, rotation):
        for module in self.modules:
            module.teleopPeriodic(x, y, rotation)

    def testInit(self):
        for module in self.modules:
            module.testInit()

    def testPeriodic(self):
        for module in self.modules:
            module.testPeriodic()

class SwerveModule:
    def __init__(self, module_number):
        self.module_number = module_number
        self.drive_motor = wpilib.SparkMax(DRIVE_MOTOR_PORTS[module_number], wpilib.MotorType.kBrushless)
        self.steer_motor = wpilib.SparkMax(STEER_MOTOR_PORTS[module_number], wpilib.MotorType.kBrushless)
        self.encoder = wpilib.Encoder(ENCODER_TICKS_PER_REV, ENCODER_GEAR_RATIO)
        self.gyro = wpilib.ADXRS450_Gyro(GYRO_PORT)

        # Deadbanding constants
        self.deadband_x = 0.1
        self.deadband_y = 0.1
        self.deadband_rotation = 0.1

        # Velocity limiting constants
        self.max_velocity = 1.0

        # Angle limiting constants
        self.max_angle = math.pi / 2

        # Motor acceleration limiting constants
        self.max_acceleration = 0.5

    def robotInit(self):
        self.encoder.reset()
        self.gyro.reset()

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self, x, y, rotation):
        # Apply deadband
        if abs(x) < self.deadband_x:
            x = 0
        if abs(y) < self.deadband_y:
            y = 0
        if abs(rotation) < self.deadband_rotation:
            rotation = 0

        # Calculate velocities and angles
        velocity = math.hypot(x, y)
        angle = math.atan2(y, x) if x != 0 else 0

        # Limit velocity
        velocity = min(velocity, self.max_velocity)

        # Calculate motor speeds
        drive_speed, steer_speed = self.calculate_motor_speeds(velocity, angle)

        # Set motor speeds
        self.drive_motor.set(drive_speed)
        self.steer_motor.set(steer_speed)

    def testInit(self):
        pass

    def testPeriodic(self):
        pass

    def calculate_motor_speeds(self, velocity, angle):
        # Calculate drive and steer motor speeds using the velocity and angle
        drive_speed = velocity * math.cos(angle)
        steer_speed = velocity * math.sin(angle)

        # Limit motor acceleration
        drive_speed = max(-self.max_acceleration, min(self.max_acceleration, drive_speed))
        steer_speed = max(-self.max_acceleration, min(self.max_acceleration, steer_speed))

        return drive_speed, steer_speed
