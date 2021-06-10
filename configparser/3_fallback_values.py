"""
As with a dictionary, you can use a section’s get() method to provide fallback values:
Please note that default values have precedence over fallback values. 

[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
"""
import configparser

config = configparser.ConfigParser()
config.read("example.ini")
topsecret = config["topsecret.server.com"]

print(topsecret.get("Port"))
print(topsecret.get("Cipher", "3des-cbc"))
print(topsecret.get("CompressionLevel", "3"))
# parser-level get() method provides a custom, more complex interface, maintained for backwards compatibility.
# When using this method, a fallback value can be provided via the fallback keyword-only argument:
print(config.get("bitbucket.org", "monster", fallback="No such things as monsters"))
