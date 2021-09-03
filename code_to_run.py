
import os
import sys


def main():
    print(sys.argv[1])
    host_fp = sys.argv[1]
    print('Checking [' + host_fp + '] ')
    try:
        os.stat(host_fp)
    except:
        print("FILE PATH IS UNREACHABLE")
        return
    print('Node Path is', host_fp)
    f = os.listdir(host_fp)
    for file_n in f:
        print(os.path.join(host_fp, file_n))

    print('Number of files or folders found: ' + str(len(f)))


if __name__ == "__main__":
    main()
