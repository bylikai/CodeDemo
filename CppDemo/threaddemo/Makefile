
all: threaddemo

CC=g++
CPPFLAGS=-Wall -std=c++11 -ggdb
LDFLAGS=-pthread

threaddemo: threaddemo.o
	$(CC)  $(LDFLAGS)  -o  $@  $^
	echo $@
	echo $^

threaddemo.o : threaddemo.cpp
	$(CC)  $(CPPFLAGS)  -o  $@  -c  $^

.PHONY:
	clean

clean:
	rm  threaddemo.o  threaddemo
