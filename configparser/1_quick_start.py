"""
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
#%% Create and save a file
import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {
    "ServerAliveInterval": "45",
    "Compression": "yes",
    "CompressionLevel": "9",
}

config["bitbucket.org"] = {"User": "hg"}

config["topsecret.server.com"] = {}
topsecret = config["topsecret.server.com"]
topsecret["Port"] = "50022"
topsecret["ForwardX11"] = "No"

config["DEFAULT"]["ForwardX11"] = "Yes"

with open("example.ini", "w") as configfile:
    config.write(configfile)

#%% read it back the file
import configparser

config = configparser.ConfigParser()
print(config.sections())
config.read("example.ini")
print(config.sections())

for key, value in config.items():
    print(key)
print(type(value))
for key, value in config["DEFAULT"].items():
    print(key, value)
print(config["bitbucket.org"]["ForwardX11"])
# %%
