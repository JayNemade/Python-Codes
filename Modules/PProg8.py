import Module

Module.greet('Jay')
print(Module.mun)

import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

from Module import countries

print(countries)