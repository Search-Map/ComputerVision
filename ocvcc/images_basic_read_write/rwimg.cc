#include <iostream> 
#include <cstdlib>
#include <stdexcept>

#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp> 
#include <opencv2/core.hpp> 
#include <opencv2/highgui.hpp> 

#include "rwimg.hh"


Imgrw::Imgrw() : ImageCollection(){} 

Imgrw::Imgrw(std::string imgfilename , cv::ImreadModes mode ) : 
    ImageCollection(imgfilename , mode ) , 
    imgMediaFilename {imgfilename} ,
    imgMode{mode}
{
    if (!imgIOCompatible()) 
        throw std::runtime_error("This media file is not Compatible") ; 

} 

Imgrw::~Imgrw(){} 

bool Imgrw::imgIsReadable () const   { 
    return cv::haveImageReader(imgMediaFilename) ;  
} 

bool Imgrw::imgIsWritable() const {
    return cv::haveImageWriter(imgMediaFilename) ;  
}

bool Imgrw::imgIOCompatible() const  { 
    return  imgIsReadable() && imgIsWritable()  ;  
} 

cv::Mat  Imgrw::read(std::string const & imgfilename){ 

    if  ( imgfilename.length()  > 0 ) 
        imgMediaFilename  = imgfilename ;
    
    if  (!imgIsReadable()) 
        throw std::runtime_error("Cannot  Read Image ")  ; 
    
    imgMatrixMetadata =  cv::imread(imgMediaFilename , imgMode) ;  
    return imgMatrixMetadata ; 
} 

void Imgrw::show(const std::string  & windowMainFrame_name , 
        int wait_delay   , char k ) const {  
    
    if (imgMatrixMetadata.data  == NULL) 
        throw std::runtime_error("Matrix NULL") ;  

    /*Create a window with specific size*/ 
    cv::namedWindow(windowMainFrame_name ,cv::WINDOW_GUI_EXPANDED) ; 
    /* Create track bar */
    cv::createTrackbar("Trackbar" , windowMainFrame_name ,nullptr,4 ); 
    cv::imshow(windowMainFrame_name ,  imgMatrixMetadata); 
    
    char   key = -1 ; 
    while (  key  !=  k ) 
    {
        key = cv::waitKey(wait_delay)  ; 
    }
    cv::destroyAllWindows() ; 
    
} 

void Imgrw::write(std::string const &   outfile_location , std::string ext){ 
    
   
    bool write_status = cv::imwrite(outfile_location , imgMatrixMetadata) ; 
    if  (!write_status)
    {
        throw std::runtime_error("Cannot write Image")  ;  
    }
} 




