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

#if !defined  _ocv_basic_read_write_image 
#define       _ocv_basic_read_write_image 

#include <opencv2/imgcodecs.hpp>
#include <string> 

typedef cv::ImageCollection  ImageCollection ; 
#define  DFAULT_READ_MODE  cv::IMREAD_UNCHANGED  

class  Imgrw : public ImageCollection  { 

    std::string imgMediaFilename ;
    cv::Mat  imgMatrixMetadata   ;   
    cv::ImreadModes  imgMode ;

    bool imgIsReadable () const ; 
    bool imgIsWritable () const ; 
    bool imgIOCompatible()const ;   
    public: 
        Imgrw() ; 
        Imgrw (std::string imgfilename ="" , cv::ImreadModes mode = DFAULT_READ_MODE);
        ~Imgrw() ; 
        
        cv::Mat read (std::string const & imgfilename=""); 
        void  show (std::string const & wmainFrame , 
                int wait_delay=0 , 
                char k='q' )  const ;
        void  write(std::string const & outputFilename  , std::string ext="");

} ; 



#endif  
