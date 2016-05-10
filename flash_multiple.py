#!/usr/bin/python

"""Simple Python script to flash a stack, banana, and apex."""

import subprocess, os

def yes(prompt):
        return raw_input(prompt + ' (y/n):').upper() == 'Y'

def main():
        print('Prior to powering up anything please ensure the Iridium Board '
              'has a dummy load or antenna attached.')
        print('Also, dont connect/disconnect flash cable while the circuits '
              'are powered up.  Remove power first.')
        if yes('Do you want to flash the PFC?'):
                print 'Connect the USB to the PFC, then power on the stack.'
                if yes('Is it ready?'):
                        pfc_dir=os.environ['HOME'] + '/major-tom/src/app/pfc'
                        subprocess.call(['make', 'flash_pfc'], cwd=pfc_dir)
        if yes('Do you want to flash the Iridium Board?'):
                print('Remove power.  Attach the AVR, remove other '
                      'programming cables.  Power it back up.')
                if yes('Is it ready?'):
                        irid_dir=os.environ['HOME'] + '/iridium-board'
                        subprocess.call(['make', 'fuses'], cwd=irid_dir)
                        subprocess.call(['make', 'program'], cwd=irid_dir)
                        print 'If it was successful, disconnect the AVR.'
        if yes('Do you want to flash the Battboard?'):
                print('Disconnect the Battboard power and attach the JTAG, '
                      'then connect power. Ensure only the JTAG is connected.')
                if yes('Is it ready?'):
                        batt_dir=os.environ['HOME'] + '/battboard'
                        subprocess.call(['make', 'program'], cwd=batt_dir)
        if yes('Do you want to flash the Banana Board?'):
                print('Ensure the Banana is not electrified, connect the JTAG,'
                      ' remove other programmers, and power it on.')
                if yes('Is it ready?'):
                        bn_dir=os.environ['HOME'] + '/major-tom/src/app/banana'
                        subprocess.call(['make', 'flash_banana'], cwd=bn_dir)
        if yes('Do you want to flash the Apex?'):
                print('Remove power, disconnect other programmers, connect the'
                      ' JTAG, then power on the stack.')
                if yes('Is it ready?'):
                        apex_dir=os.environ['HOME'] + '/major-tom/src/app/apex'
                        subprocess.call(['make', 'flash_apex'], cwd=apex_dir)
                        print('If it was successful, power everything off and '
                              'disconnect the programmers.')

if __name__ == "__main__":
    main()
