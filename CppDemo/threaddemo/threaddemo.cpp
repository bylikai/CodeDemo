/*************************************************************************
    > File Name: threaddemo.cpp
    > Author: kai.li
    > Mail: bylikai@163.com 
    > Created Time: 二  7/25 09:03:57 2017
 ************************************************************************/

#include <iostream>
#include <thread>

#include <stdio.h>
#include <stdlib.h>

// test precompaired
#if !defined(__cplusplus)
#error c++ compiler reqired
#else 
#define PFUNCTION3(kaili, duxiaoxia, liyi) \
	void pfunction##kaili##duxiaoxia##liyi() { \
		std::cout<<#kaili<<", "<<#duxiaoxia<<", "<<#liyi<<std::endl; \
	}
//#error c++ compiler success   //#error macro interrupt the compiler
#endif

#if defined(ppx)
PFUNCTION3(_K,_D,_Y)
#endif


using namespace std;

void thread_task() {
//	pfunction_K_D_Y();
	std::cout<<"hello world! for thread."<<std::endl;
}

int main( int argc, char* argv[] ) {
	std::thread t(thread_task);
	t.join();

	return 0;
}
