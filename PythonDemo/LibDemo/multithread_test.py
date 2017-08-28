
import threading
from   time import ctime, sleep


def music( music_name ):
    for i in range(10):
        print("I am music ", music_name, ctime())
        sleep(1)

def song( song_name ):
    for i in range(10):
        print("I am song ", song_name, ctime() )
        sleep(1)

def test() :
    music("xia xia xia ")
    song("kai kai kai ")


threads = []
t1 = threading.Thread( target=music, args=('Love you forever'))
t2 = threading.Thread( target=song,  args=('belong to yesterday') )

threads.append(t1)
threads.append(t2)


if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    print("all over ", ctime() )


