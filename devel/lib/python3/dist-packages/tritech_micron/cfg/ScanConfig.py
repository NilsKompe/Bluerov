## *********************************************************
##
## File autogenerated for the tritech_micron package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'inverted', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Upside down', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'continuous', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Scan continuously or only a sector', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'scanright', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Rotate clockwise', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'adc8on', 'type': 'bool', 'default': True, 'level': 0, 'description': 'ADC 8 mode', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'gain', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Gain', 'min': 0.0, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ad_low', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Minimum amplitude in dB', 'min': 0.0, 'max': 80.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ad_high', 'type': 'double', 'default': 80.0, 'level': 0, 'description': 'Maximum amplitude in dB', 'min': 0.0, 'max': 80.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'left_limit', 'type': 'double', 'default': 2.356194490192345, 'level': 0, 'description': 'Left limit in rad', 'min': 0.0, 'max': 6.283185307179586, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'right_limit', 'type': 'double', 'default': 3.9269908169872414, 'level': 0, 'description': 'Right limit in rad', 'min': 0.0, 'max': 6.283185307179586, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'speed', 'type': 'double', 'default': 1500.0, 'level': 0, 'description': 'Speed of sound', 'min': 1400.0, 'max': 1600.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'range', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Range in meters', 'min': 2.0, 'max': 100.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'mo_time', 'type': 'int', 'default': 250, 'level': 0, 'description': 'Motor speed in microseconds', 'min': 0, 'max': 2550, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'nbins', 'type': 'int', 'default': 400, 'level': 0, 'description': 'Number of bins per slice', 'min': 0, 'max': 1500, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'step', 'type': 'double', 'default': 0.031415926535897934, 'level': 0, 'description': 'Motor step size in rad', 'min': 0.0009817477042468104, 'max': 0.2503456645829366, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'LOWEST', 'type': 'double', 'value': 0.2503456645829366, 'srcline': 42, 'srcfile': '/home/bluerov23/v3Bluerov/src/tritech_micron/cfg/Scan.cfg', 'description': 'Lowest resolution', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'LOWER', 'type': 'double', 'value': 0.12566370614359174, 'srcline': 43, 'srcfile': '/home/bluerov23/v3Bluerov/src/tritech_micron/cfg/Scan.cfg', 'description': 'Lower resolution', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'LOWERISH', 'type': 'double', 'value': 0.06283185307179587, 'srcline': 44, 'srcfile': '/home/bluerov23/v3Bluerov/src/tritech_micron/cfg/Scan.cfg', 'description': 'Lowerish resolution', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'LOW', 'type': 'double', 'value': 0.031415926535897934, 'srcline': 45, 'srcfile': '/home/bluerov23/v3Bluerov/src/tritech_micron/cfg/Scan.cfg', 'description': 'Low resolution', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'MEDIUM', 'type': 'double', 'value': 0.015707963267948967, 'srcline': 46, 'srcfile': '/home/bluerov23/v3Bluerov/src/tritech_micron/cfg/Scan.cfg', 'description': 'Medium resolution', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'HIGH', 'type': 'double', 'value': 0.007853981633974483, 'srcline': 47, 'srcfile': '/home/bluerov23/v3Bluerov/src/tritech_micron/cfg/Scan.cfg', 'description': 'High resolution', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'ULTIMATE', 'type': 'double', 'value': 0.003926990816987242, 'srcline': 48, 'srcfile': '/home/bluerov23/v3Bluerov/src/tritech_micron/cfg/Scan.cfg', 'description': 'Ultimate resolution', 'ctype': 'double', 'cconsttype': 'const double'}], 'enum_description': 'Default resolution enumeration'}", 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Scan_LOWEST = 0.2503456645829366
Scan_LOWER = 0.12566370614359174
Scan_LOWERISH = 0.06283185307179587
Scan_LOW = 0.031415926535897934
Scan_MEDIUM = 0.015707963267948967
Scan_HIGH = 0.007853981633974483
Scan_ULTIMATE = 0.003926990816987242