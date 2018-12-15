#-------------------------------------------------------------------------------
# Name:        iputil
# Purpose:     To change IP address of my laptop
#
# Author:      Mayur Shingote
#
# Created:     16-12-2018
# Copyright:   (c) Mayur Shingote 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import wmi

def home():
    # Obtain network adaptors configurations
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # First network adaptor
    nic = nic_configs[0]

    # Enable DHCP
    nic.EnableDHCP()

def office(ip='10.11.15.146', subnetmask='255.255.255.0', gateway='10.11.15.1'):
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)

    # First network adaptor
    nic = nic_configs[0]
    nic.EnableStatic(IPAddress=[ip],SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'home':
            home()
        elif sys.argv[1] == 'office':
            office()
        else:
            raise RuntimeError('Invalid command line argument!')

if __name__ == '__main__':
    main()
