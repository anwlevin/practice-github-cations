# This is a sample Python script.
import sys

from parseData import get_video_info


def make(url):
    print(f'🎥 Url:  {url}')

    data = get_video_info(url)

    print(data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = sys.argv[1]
    make(url)

