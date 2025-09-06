# mi_script.py
import platform
import datetime

def main():
    print(f"Operative System: {platform.system()} {platform.release()}")
    print(f"Date and time from Python: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()