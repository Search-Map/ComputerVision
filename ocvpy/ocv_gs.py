""" 
Opencv  Getting  started  @Search-Map

CC0 1.0 Universal

    CREATIVE COMMONS CORPORATION IS NOT A LAW FIRM AND DOES NOT PROVIDE
    LEGAL SERVICES. DISTRIBUTION OF THIS DOCUMENT DOES NOT CREATE AN
    ATTORNEY-CLIENT RELATIONSHIP. CREATIVE COMMONS PROVIDES THIS
    INFORMATION ON AN "AS-IS" BASIS. CREATIVE COMMONS MAKES NO WARRANTIES
    REGARDING THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS
    PROVIDED HEREUNDER, AND DISCLAIMS LIABILITY FOR DAMAGES RESULTING FROM
    THE USE OF THIS DOCUMENT OR THE INFORMATION OR WORKS PROVIDED
    HEREUNDER.
"""
__version__  :str  = "@Search-Map opencv getting started v1.0" 
__author__   :str  = "Umar <github/jukoo" 

import cv2 as cv , sys , os , re   
from inspect  import getmembers  
from  enum import Enum  , unique 
from  collections import namedtuple 
from  smgoodies import Goodies   


@unique 
class AutoSwitchMode (Enum) :  
    VIDEO_MODE   :int  = 0 
    PICTURE_MODE :int  = 1    


class  VideoMediaProcessError(Exception) : 
    def __init__(self, mesg ,*args , **kwargs) : 
        Exception.__init__(self, mesg ,args ,**kwargs)

class  VideoMediaProcess : 
    """
    Open CV   : Video Processing 
    with  some extra  introspection  inside cv properties 
    *this class  can be use as context manager... as protected scope  like "with open" 
    """ 
    
    CV_PROPERTIES :str =  "^CAP_PROP_*.+" 

    def __init__ (self , video_file_or_device :any )  :
        try   : 
            self.vmediafilename  = int ( video_file_or_device)  
        except ValueError  : 
             self.vmediafilename =  video_file_or_device  

        self.vmediametadata  = None 
        for  (cv_props  , rate)  in  self.inspect_cv2_cap_proterties :
            self.__setattr__(cv_props, rate )  

    @property 
    def _vframe (self) : return  self.vmediametadata.get(self.CAP_PROP_FPS)
    @property
    def _vheight(self) : return  self.vmediametadata.get(self.CAP_PROP_FRAME_HEIGHT)
    @property
    def _vwidth(self)  : return  self.vmediametadata.get(self.CAP_PROP_FRAME_WIDTH) 
    @property 
    def _vsize (self)  : return  self.CAP_PROP_FRAME_HEIGHT , self.CAP_PROP_FRAME_WIDTH 
    
    @property  
    def inspect_cv2_cap_proterties (self): 
        vcap_properties =  [ cap for  cap in getmembers(cv) if re.match(rf"^{self.CV_PROPERTIES}" , cap.__getitem__(0)) is not None  ]
        return vcap_properties 

    @inspect_cv2_cap_proterties.setter  
    def inspect_cv2_cap_proterties(self ,new_patern )  :
        self.CV_PROPERTIES = new_patern
        return self.inspect_cv2_cap_proterties  

    def  __enter__ ( self ) : 
        self.vmediametadata = cv.VideoCapture(self.vmediafilename) 
        if not  self.vmediametadata.isOpened()  : 
            raise VideoMediaProcessError ("Cannot process file ${self.video_file_or_device} or Ressource Busy") 
        
        return  self.vmediametadata  

    def __exit__ (self , *args) : 
        self.vmediametadata.release()  
        cv.destroyAllWindows()  


    def initiate_stream_record ( self  ,  destination )  :   
        return  cv.VideoWriter(destination , cv.VideoWriter_fourcc(*'MJPG'),30,(1080,1920)) 
         
    def __str__ (self) :  
        return f"file name {self.vmediafilename}" 


__FLAGS__ =  {
        "file"        : "-f ,load file media",
        "window-name" : "-w ,window name",
        "save"        : "-s ,Named your saved file media",
        "version_"    : "-v ,print verion"
}

@Goodies.argctrl(__FLAGS__) 
def main (*argv ,**kwargs)  ->  int :
    argv  = argv.__getitem__(0) 

    if  argv.version :
        sys.__stdout__.write(f"{__version__}\n")  
        sys.exit(0) 
    
    #! Require file as input  ... !!! Raise Brutal Assertion !!!  
    assert argv.file  is not  None  ,  f"require  File  media to proceed\n"
    
    #set  default  window name3  if not specified  ... 
    default_window_name  =  ( "SM OCV::Display" ,  argv.window_name)[argv.window_name is not None]  
    
    #! TODO :  SWITCH  VIDEO  OR IMAGE Depending  file extension  ...  
    media_file   =  ( ( AutoSwitchMode.VIDEO_MODE.value ,  VideoMediaProcess(argv.file or 0 )), ( AutoSwitchMode.PICTURE_MODE.value ,  argv.file))[ cv.imread(argv.file) is not None] 

    fmod = namedtuple("fmod" , [ "mode" ,  "fd"])
    fmod = fmod(*list(media_file))  
    
    if  fmod.mode.__eq__(AutoSwitchMode.VIDEO_MODE.value)  : 

        writablestream = cv.VideoWriter("test.avi" , cv.VideoWriter_fourcc(*'MJPG'),30,(1080,1920))
        with fmod.fd as vmprocess  : 
            _ :bool =  vmprocess.isOpened()
            fps =  vmprocess.get(fmod.fd.CAP_PROP_FPS) 
            #writablestream  = vmp.initiate_stream_record("test.avi")  
            subt = cv.createBackgroundSubtractorKNN() 
            while  _  : 
                _ , video_frame =  vmprocess.read() 
                cf = cv.resize(video_frame  ,(800,800) )
                mask  = subt.apply(cf) 
                c , O = cv.findContours(mask, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) 
                cv.imshow("Video Frame" , mask ) 
                cv.displayOverlay('Video Frame', "dsadasdsa") 
                writablestream.write(video_frame)  
                keystroke  = cv.waitKey(20)
                if  keystroke.__eq__(ord('q')) : break  

            writablestream.release() 
    else : 
        imgfile =  cv.imread(cv.samples.findFile(fmod.fd)) 
        cv.namedWindow(default_window_name)     
        cv.imshow(default_window_name ,  imgfile)  
        keystroke =  0 
    
        # 'q' for quit  
        while  keystroke != ord('q'):
            keystroke = cv.waitKey(0) 

            # 's' for save
            if argv.save is not None and  keystroke == ord('s') :
                cv.imwrite(argv.save ,imgfile) 

    return  0   


if __name__.__eq__("__main__")  : 
    main.__call__()  
