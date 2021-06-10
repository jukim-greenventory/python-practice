"""
Config parsers do not guess datatypes of values in configuration files, 
always storing them internally as strings. This means that if you need other datatypes, 
you should convert on your own:

Since this task is so common, config parsers provide a range of handy getter methods to handle integers,
floats and booleans. The last one is the most interesting because simply passing the value to bool() 
would do no good since bool('False') is still True. This is why config parsers also provide getboolean(). 
This method is case-insensitive and recognizes Boolean values from 
'yes'/'no', 'on'/'off', 'true'/'false' and '1'/'0'
.Apart from getboolean(), config parsers also provide equivalent getint() and getfloat() methods. 
You can register your own converters and customize the provided ones.
"""
import configparser

config = configparser.ConfigParser()
config.read("example.ini")
topsecret = config["topsecret.server.com"]


print(int(topsecret["Port"]))
print(float(topsecret["CompressionLevel"]))
print(topsecret.getboolean("ForwardX11"))
print(config["bitbucket.org"].getboolean("ForwardX11"))
print(config.getboolean("bitbucket.org", "compression"))
