#include <iostream> 
#include <string> 

#include <opencv2/core.hpp> 
#include <opencv2/videoio.hpp>
#include <opencv2/core.hpp> 
#include <opencv2/imgproc.hpp> 
#include <opencv2/imgcodecs.hpp> 


#include "vidrw.hh"


Vidrw::Vidrw(){} ; 
Vidrw::Vidrw(std::string  vmf , Vcap vcap  ) : 
    cv::VideoCapture(vmf , vcap ), 
    video_media_filename { vmf} ,  
    used_vcap_api_reference {vcap} 
{}

Vidrw::Vidrw(int vdi  , Vcap vcap ):
    cv::VideoCapture(vdi , vcap ) , 
    used_vcap_api_reference{vcap} , 
    video_divice_index{vdi} 
{}  


Vidrw::~Vidrw(){}


bool Vidrw::snapshoot(
        std::string const & saved_location_frame , 
        cv::Mat  const    & current_frame ) 
{ 

    return cv::imwrite(saved_location_frame ,  current_frame) ;  

} 
