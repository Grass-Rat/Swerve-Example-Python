# Parade-Bot-Python
A test bot template using robotpy.  This is intended to run the parade bot drivetrain.

# References
This is basic bot to test python programming.  It started with example code from these templates:
 * https://github.com/robotpy/examples/tree/main/GyroDriveCommands
 * https://github.com/robotpy/examples/tree/main/FrisbeeBot

Reference for robotpy can be found here.
 * https://github.com/robotpy
 * Python RobotPy API - https://robotpy.readthedocs.io/projects/robotpy/en/stable/
 * Zero to robot - https://docs.wpilib.org/en/stable/docs/zero-to-robot/introduction.html
 * Learn Python - https://docs.python-guide.org/intro/learning/

Notes:
* `pyproject.toml` is used to add 3rd party libraries.  After updating the file run `robotpy sync` to download new resources

# Installing on MacOS
```bash
conda create -n robotpy310 python=3.10
conda activate robotpy310
python3 -m pip install robotpy
```

Commands2 does not seem to be installed by default.
```bash
pip install robotpy-commands-v2
```

