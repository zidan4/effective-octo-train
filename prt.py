import sys
import struct

equals_button = 0x01005D51
memory_file = "WinXPSP2.vmem"
slack_space = None
trampoline_offset = None

# read in our shellcode
sc_fd = open("cmeasure.bin","rb")
sc = sc_fd.read()
sc_fd.close()
sys.path.append("/Users/justin/Downloads/volatility-2.3.1")

import volatility.conf as conf
import volatility.registry as registry

registry.PluginImporter()
config = conf.ConfObject()

import volatility.commands as commands
import volatility.addrspace as addrspace

registry.register_global_options(config, commands.Command)
registry.register_global_options(config, addrspace.BaseAddressSpace)
config.parse_options()
config.PROFILE = "WinXPSP2x86"
config.LOCATION = "file://%s" % memory_file
