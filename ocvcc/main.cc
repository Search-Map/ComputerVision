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
#include <string>  

#include <opencv2/core.hpp> 
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/imgcodecs.hpp> 

#include "rwimg.hh"
#include "goodies.hh"  

auto
main (int argc  , char**argv)-> int {  
    
    FlagsEntryHdl_t  flag_parser  ;  
    argument_parser(argc , argv , flag_parser)  ; 
    
    Imgrw  imgrw  {flag_parser.file} ; 

    if  (  imgrw.read().data == NULL )  
        CV_Error(cv::Error::StsError , cv::format("Cannot Read file %s" , flag_parser.file.c_str())); 
    
    imgrw.show(WIN_DEFAULT_NAME)  ; 
    
    if (flag_parser.save)
    {  
        if (flag_parser.file_rename.length() > 0  ) 
        {
            imgrw.write(flag_parser.file_rename) ;
        }
        imgrw.write(flag_parser.file) ; 
    }

    return EXIT_SUCCESS ; 
} 
