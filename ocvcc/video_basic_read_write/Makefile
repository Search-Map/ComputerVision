#!/usr/bin/make  
# LICENCE  not -yet 
# Author  Umar <jUmarB@protonmail.com> 



cxx = g++ 
cxxflags = -Wall -Wextra  -pedantic 
src = $(wildcard *.cc )
include_directories = -I include -I /usr/include/opencv4 
opencv_libraries_dirs=  /usr/lib
opencv_shared_libraries  = -lopencv_highgui \
						   -lopencv_core \
						   -lopencv_imgcodecs \
						   -lopencv_imgproc \
						   -lopencv_cvv \
						   -lopencv_videoio

obj=$(src:.cc=.o) 
exec=fcut  
all : $(exec) 


$(exec)  : $(obj)
	@echo -e  "[LD] - $^"
	$(cxx)   $^  -o $@  -L ${opencv_libraries_dirs}  ${opencv_shared_libraries}  ${cxxflags} ${include_directories} 
	
%.o : %.cc
	@echo -e "[CC] - $<"
	$(cxx) -o $@ -c $<  -L ${opencv_libraries_dirs}  ${opencv_shared_libraries}  ${cxxflags} ${include_directories}

.PHONY : clean mproper

clean : 
	@echo -e "Cleaning Object  file [C-OBJ]"
	rm  $(obj)  
	
mproper: clean 
	@echo -e "R EXE" 
	rm $(exec)  

