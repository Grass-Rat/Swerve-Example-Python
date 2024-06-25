# Swerve-Example-Python

## Overview

This repository provides a basic implementation of a swerve drive system in Python using WPILib for FRC robots. The code is organized into several key files:

- **swerve.py**: Contains the `Swerve` and `SwerveModule` classes, implementing the swerve drive system.
- **constants.py**: Defines constants used throughout the code, such as motor ports and encoder settings.
- **robot.py**: Contains the `Robot` class, the main entry point for the robot code.
- **robotcontainer.py**: Contains the `RobotContainer` class, which wraps the `Swerve` class and provides a simple interface for the robot code.

## Purpose

The purpose of this repository is to provide a Python example of a swerve drive implementation for FRC teams to use. It serves as a reference and starting point for teams looking to develop their own swerve drive systems using Python and WPILib.

## Todos

- Add CAN IDs for SparkMax motors in `constants.py`.
- Calibrate the gyro in `swerve.py`.
- Initialize the encoder in `swerve.py`.
- Invert motor directions if necessary in `swerve.py`.
- Adjust deadbanding and velocity limiting constants in `swerve.py`.
- Test and debug the code thoroughly.

## License

This repository is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to contribute to this repository, please fork the repository and submit a pull request with your changes.

## Acknowledgments

This repository is based on the WPILib Python examples and the FRC community's swerve drive implementations.

## Contact

If you have any questions or feedback, please contact the repository owner at Grass-Rat.

## Disclaimer

This code is provided as-is, without any warranty or support. Use at your own risk.
It's not recommended to use this code as-is without completing the outstanding tasks and ensuring it works as intended. I am working on that. I just made this as a basic example and impulsively developed it in the span of an hour, I will be testing it tonight (06/25/2024). Please keep this in mind!
