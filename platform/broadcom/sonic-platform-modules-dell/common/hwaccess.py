# Helper functions to access hardware

import struct
import mmap
import subprocess

# Read PCI device

def pci_mem_read(mm, offset):
    mm.seek(offset)
    read_data_stream = mm.read(4)
    return struct.unpack('I',read_data_stream)[0]

def pci_get_value(resource, offset):
    val = None
    with open(resource, 'r+b') as fd:
        mm = None
        try:
            mm = mmap.mmap(fd.fileno(), 0)
            val = pci_mem_read(mm, offset)
        except:
            pass
        if mm is not None:
            mm.close()
    return val

# Read I2C device

def i2c_get(bus, i2caddr, ofs):
    try:
        result = int(subprocess.check_output(['/usr/sbin/i2cget', '-y', str(bus), str(i2caddr), str(ofs)]), 16)
    except:
        result = None
    return result
