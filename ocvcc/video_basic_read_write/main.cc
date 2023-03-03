#include <iostream> 
#include <string> 
#include <cstdlib> 
#include <stdexcept> 

#include <opencv2/videoio.hpp>
#include <opencv2/core.hpp> 
#include <opencv2/imgproc.hpp> 
#include <opencv2/imgcodecs.hpp> 
#include <opencv2/highgui.hpp> 

#include "vidrw.hh"


auto
main  (int  argc   , char **argv ) -> int { 
    
     
    Vidrw  v  {"/dev/video0"} ;  
    cv::Mat vFrame ;  
    char  k  ;
    int i   { 0} ; 
    while ( v.isOpened())  
    {
        v >> vFrame ;
        
        if  ( vFrame.data == NULL ) 
            throw std::runtime_error("Oops Empty Frame Catched !") ;  
        
        cv::imshow("Live Frame " , vFrame)  ; 
        if  ( (k =  cv::waitKey(20)) == EXIT_VIDCAPTURE )
            break  ; 
        
        v.snapshoot("test"+std::to_string(i)+".jpg" , vFrame) ; 
        i++ ; 
    }
    v.release() ; 
    cv::destroyAllWindows()  ;

    return  EXIT_SUCCESS ; 
} 
