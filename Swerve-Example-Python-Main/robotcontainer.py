import wpilib
from swerve import Swerve

class RobotContainer:
    def __init__(self):
        self.swerve = Swerve()

    def robotInit(self):
        self.swerve.robotInit()

    def autonomousInit(self):
        self.swerve.autonomousInit()

    def autonomousPeriodic(self):
        self.swerve.autonomousPeriodic()

    def teleopInit(self):
        self.swerve.teleopInit()

    def teleopPeriodic(self, x, y, rotation):
        self.swerve.teleopPeriodic(x, y, rotation)

    def testInit(self):
        self.swerve.testInit()

    def testPeriodic(self):
        self.swerve.testPeriodic()