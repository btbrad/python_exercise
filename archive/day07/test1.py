import os
import time

def main():
    content = '欢迎欢迎欢迎...'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

main()