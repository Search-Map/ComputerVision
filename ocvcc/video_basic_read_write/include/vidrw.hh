#if !defined  _basic_read_write_video 
#define       _basic_read_write_video 

#include <string> 
#include <opencv2/videoio.hpp> 

#define  EXIT_VIDCAPTURE  (113 & 0Xff) 

typedef  enum cv::VideoCaptureAPIs Vcap  ; 

class  Vidrw  : public cv::VideoCapture  { 
    
    std::string video_media_filename ;
    Vcap used_vcap_api_reference ;
    int  video_divice_index ; 
    public :
        Vidrw() ; 
        Vidrw(std::string  vmf   , Vcap  vcap=cv::CAP_ANY) ; 
        Vidrw(int vdi  , Vcap vcap = cv::CAP_ANY) ;  
        virtual  ~Vidrw() ; 
        
        bool snapshoot ( std::string const &  location , cv::Mat const & frame ) ; 

} ;  
#endif  
