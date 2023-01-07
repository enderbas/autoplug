# Broadlink WiFi Plug PC Charge Automation

Repo contains two script file:
+ **autoplug.py** script controls wifi plug according to battery charge rate.
Closes plug when the rate is lower than %21 and opens plug when the rate is higher than %85.
+ **start-autoplug.vbs** is autoplug.py script runner script. You can copy this to windows start applications folder to start this application at start-up.

# Requirements
- Python 3.10 (not tested for different versions)
- _broadlink_ library for python
- - pip3 install broadlink
- _logging_ library for python

## Note:
- In autoplug.py file set your wifi name and password for initialiasation. After first run, you can comment this line.
- If you want to seperate python and starter script locations, you should set 5. line in start-autoplug.vbs file with autoplug.py path.