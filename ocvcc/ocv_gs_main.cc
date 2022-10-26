/* 
 * Opencv  Getting  started  @Search-Map
 * author  :  Umar<github/jukoo>   ( jUmarB@protonmail.com)  
 *
 * CC0 1.0 Universal
 * CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
 * LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
 * ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
 * INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
 * REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
 * PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
 * THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED HEREUNDER.
 *
 */

#include <iostream> 
#include <cstdlib> 
#include <iterator> 
#include <string> 
#include <iterator>

//!  opencv  libraries  
#include "opencv2/core.hpp"
#include "opencv2/highgui.hpp"  
#include "opencv2/imgcodecs.hpp"  
#include "opencv2/opencv.hpp"

//internal library for some good utilities
#include "include/goodies.hh"  

auto
main ( int argc , char **argv ) -> int  {  


    FlagsEntryHdl_t  argshdl  ; 

    argument_parser(argc , argv  , argshdl ) ; 
     
    std::string  media_file  {cv::samples::findFile(argshdl.file)};
    cv::Mat media_data  { cv::imread(media_file , cv::IMREAD_COLOR ) } ;
    
    if ( media_data.total() ==  0)   
    {
        //! Print  the  message  on  Open cv that raised an Exception ...  
        CV_Error(cv::Error::StsError , cv::format("Cannot Read  file '%s'" , media_file.c_str())); 
    }
     
    std::string  window_name  { WIN_DEFAULT_NAME} ;   
    cv::imshow(window_name  ,  media_data)   ;
    unsigned char   keyStroke  { 0 } ; 
    
    while  (keyStroke  != QUIT ) 
    {
        keyStroke  = cv::waitKey(0) ; 
         
        if (keyStroke == SAVE and (argshdl.save or  not argshdl.file_rename.empty())) 
        {
            std::string  new_name =  argshdl.file_rename.empty() ?  media_file :  argshdl.file_rename ; 
            cv::imwrite( new_name,  media_data);  
        }
    }
     

    return EXIT_SUCCESS ; 
} 
