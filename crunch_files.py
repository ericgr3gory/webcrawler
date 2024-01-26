import os

def main():
    files = os.listdir('chia-docs/')
    with open('crunch.txt', 'w') as crunch:
        for file in files:
            crunch.write(file)
            with open(f'chia-docs/{file}', 'r') as f:
                crunch.write(f'{f.read()}/n')


if __name__ == "__main__":
    main()