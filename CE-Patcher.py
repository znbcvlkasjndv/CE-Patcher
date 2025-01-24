import os
import re

strtorepl = b"Cheat Engine"
repldastr = b"CE by Mafioz"

def changeFile(fname, strrepl, replstr):
    with open(fname, "rb") as f:
        data = f.read()
    data = data.replace(strrepl, replstr)
    with open(fname, "wb") as f:
        f.write(data)

def find_file(filename, start_dir="C:\\"):
    for root, dirs, files in os.walk(start_dir):
        if filename in files:
            return os.path.join(root, filename)
    return None

def main():
    target_file = "cheatengine-x86_64.exe"
    print("Ищем файл по всему компьютеру...")
    found_path = find_file(target_file)

    if found_path:
        print(f"Файл найден: {found_path}")
        target_dir = os.path.dirname(found_path)
        os.chdir(target_dir)
        print(f"Текущая директория: {target_dir}")
        
        files = [
            "cheatengine-x86_64.exe", 
            "cheatengine-i386.exe", 
            "cheatengine-x86_64-SSE4-AVX2.exe"
        ]
        
        for file in files:
            if os.path.exists(file):
                changeFile(file, strtorepl, repldastr)
                print(f"Файл {file} успешно запатчен.")
            else:
                print(f"Файл {file} не найден в директории {target_dir}.")
    else:
        print("Файл не найден на этом компьютере.")

if __name__ == "__main__":
    main()
input("Нажмите Enter, чтобы закрыть консоль...")