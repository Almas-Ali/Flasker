import argparse
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)

parser = argparse.ArgumentParser()

parser.add_argument('--CreateProject', help='Create a new flask project.')
parser.add_argument('--CreateApp', help='Create a new flask app.')

args = parser.parse_args()

if args.CreateProject:
    print('[+] Creating Flasker Project...')
    with open(os.path.join(BASE_DIR, 'templates/CreateProject.txt'), 'r') as f:
        c = ''.join(f.readlines())
    with open(f'{args.CreateProject}.py', 'w') as r:
        r.write(c)
    print('[+] Project created successfully!')

elif args.CreateApp:
    print('[+] Creating Flasker App...')
else:
    parser.print_help()
