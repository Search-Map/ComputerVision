#!/usr/bin/make  
 #* Opencv  Getting  started  @Search-Map
 #* author  :  Umar<github/jukoo>   ( jUmarB@protonmail.com)  
 #*
 #* CC0 1.0 Universal
 #* CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
 #* LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
 #* ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
 #* INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
 #* REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
 #* PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
 #* THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER.

# ! Generic  Makefile ! 
cxx  = g++  
incdir = /usr/include/opencv4  
libdir = /usr/lib/ 
shared_libs=-lopencv_core \
    -lopencv_imgproc \
    -lopencv_imgcodecs \
    -lopencv_highgui \
    -lopencv_ml \
    -lopencv_video \
    -lopencv_cvv \
    -lopencv_features2d 

cxxflags=-Wall -Wextra -pedantic  -std=c++17 -I include  
src=$(wildcard  *.cc) 
obj=$(src:.cc=.o)  

binexe=smocv_gs

all : $(binexe) 
	
$(binexe) : $(obj)  
	@echo -e "\t [ LINK ] $^"
	$(cxx) -I $(incdir)  -L $(libdir)  $(shared_libs) -o  $@ $^  $(cxxflags) 

%.o :  %.c*
	@echo -e "\t [ CXX ] $<"
	$(cxx) -I $(incdir)  -L $(libdir)  $(shared_libs) -o  $@ -c  $< $(cxxflags) 


.PHONY : clean mproper  


clean : 
	rm $(obj)  


mproper : clean 
	rm  $(binexe)
	
