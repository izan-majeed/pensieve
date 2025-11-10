import hashlib
import os
import json


def calculate_file_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

def calculate_directory_checksum(directory_path):
    sha256 = hashlib.sha256()
    for root, dirs, files in os.walk(directory_path):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256.update(chunk)
    return sha256.hexdigest()


def main():
    checksums = {
        "CHECKSUM_METADATA": calculate_directory_checksum('./metadata'),
        "CHECKSUM_TAFASIR": calculate_directory_checksum('./tafasir/'),
        "CHECKSUM_TRANSLATIONS": calculate_directory_checksum('./translations/'),
        "CHECKSUM_VERSES": calculate_directory_checksum('./verses/'),
        "CHECKSUM_RECITATIONS": calculate_directory_checksum('./recitations/'),
    }

    with open('checksums.json', 'w') as f:
        json.dump(checksums, f, indent=4)

    print("Checksums calculated and saved to checksums.json")

if __name__ == "__main__":
    main()





