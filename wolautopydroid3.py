import subprocess
from wakeonlan import send_magic_packet
import schedule
import time

IP_DEVICE = "192.168.2.6"

devices = {
    'my_pc': {'mac': '50:EB:F6:78:4F:C0', 'ip_address': '192.168.2.255'}
}


def wake_device(device_name):
    if device_name in devices:
        mac, ip = devices[device_name].values()
        send_magic_packet(mac, ip_address=ip)
        print('Magic Packet Sent')
    else:
        print('Device Not Found')

def run_script():
    proc = subprocess.Popen(["ping", IP_DEVICE], stdout=subprocess.PIPE)

    while True:

        line = proc.stdout.readline()
        if not line:
            break
        else:
            None

        try:
            connected_ip = line.decode('utf-8').split()[3].replace(':', '')
            if connected_ip == IP_DEVICE:
                print('Device connected!')
                wake_device('my_pc')
                # Do whatever you want when the device connects here...
                break
            else:
                print('Pinging device...')
        except:
            pass

schedule.every().day.at("22:02").do(run_script)


while 1:
	schedule.run_pending()
	time.sleep(1)
