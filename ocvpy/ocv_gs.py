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
__author__   :str  = "Umar <github/jukoo>" 

import cv2 as cv , sys , os  
from inspect  import getmembers  
from  enum import Enum  , unique 
from  collections import namedtuple 
from  smgoodies import Goodies   


@unique 
class AutoSwitchMode (Enum) :  
    VIDEO_MODE   :int  = 0 
    PICTURE_MODE :int  = 1 
    

converge_asmode  = lambda  x: dict (zip( x._member_names_ ,x._value2member_map_))  

# Basic  Exception 
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
    FPS  :int   = 30
    SIZE :tuple =  (600,600)
    CC_FRAME_COMPRESSOR  =   {  "MJPG" :  ".avi" , "XVID" :".mp4" }   
    
    def __init__ (self , video_file_or_device :any )  :
        try   : 
            self.vmediafilename  = int ( video_file_or_device)  
        except ValueError  : 
             self.vmediafilename =  video_file_or_device  

        self.vmediametadata  = None
         
        for  (cv_props_attr  , cv_props_value )   in  Goodies.module_inspection(cv , self.CV_PROPERTIES)  :
            self.__setattr__(cv_props_attr  , cv_props_value) 

        for mode_attribute , value in converge_asmode(AutoSwitchMode).items(): 
            self.__setattr__( mode_attribute ,  value) 



    def _vframe (self , Vcap_instance) : return  Vcap_instance.get(self.CAP_PROP_FPS)
    def _vheight(self , Vcap_instance) : return  Vcap_instance.get(self.CAP_PROP_FRAME_HEIGHT)
    def _vwidth (self , Vcap_instance) : return  Vcap_instance.get(self.CAP_PROP_FRAME_WIDTH) 
    
    @property 
    def _vsize (self)  : return  self.CAP_PROP_FRAME_HEIGHT , self.CAP_PROP_FRAME_WIDTH 
    

    def  __enter__ ( self ) : 
        self.vmediametadata = cv.VideoCapture(self.vmediafilename) 
        if not  self.vmediametadata.isOpened()  : 
            raise VideoMediaProcessError ("Cannot process file ${self.video_file_or_device} or Ressource Busy") 
        
        return  self.vmediametadata  

    def __exit__ (self , *args) : 
        self.vmediametadata.release()  
        cv.destroyAllWindows()  


    def initiate_stream_record ( self,  destination  , frame_size=(1080,1920) ,  framecc=None )  :  
        framecc = list ( self.CC_FRAME_COMPRESSOR.keys()).__getitem__(0)  if  framecc is None  else  framecc.upper() 
        assert list(self.CC_FRAME_COMPRESSOR.keys()).__contains__(framecc)  , f"undefined Attribute  only -> {list(self.CC_FRAME_COMPRESSOR.keys())} are allowed !" 
        destination  = f'{destination}{self.CC_FRAME_COMPRESSOR[framecc]}' 
        return  cv.VideoWriter(destination , cv.VideoWriter_fourcc(*framecc),self.FPS ,  frame_size) 

    def  use_bgsubalgorithm (self, algorithm)  :
        algorithm =  algorithm.upper() if algorithm is not None  else  "MOG2" 
        assert  [ "MOG2" , "KNN"].__contains__(algorithm) ,"undefined backgroundsubtraction algorithm " 
        cv_method_string  =  f"createBackgroundSubtractor{algorithm}" 
        return  getattr(cv , cv_method_string)() 

         
    def __str__ (self) :  
        return f"file name {self.vmediafilename}" 


__FLAGS__ =  {
        "file"         : "-f ,load file media",
        "window-name"  : "-w ,window name",
        "save"         : "-s ,Named your saved file media",
        "Save_"        : "-S ,save the current file in cwd  without  specifing name",
        "size-resolution": "-r ,define size  resolution  e.g  800x800 ",
        "inspect-attr_": "-I ,Inspect Attributes" ,
        "set-fcompress": "-F ,set  format compressor "  ,  
        "bg-algo"      : "-b ,set Background Algorithm ( KNN | MOG2)",
        "version_"     : "-v ,print verion"
}

@Goodies.argctrl(__FLAGS__) 
def main (*argv ,**kwargs)  ->  int :
    argv  = argv.__getitem__(0) 

    if  argv.version :
        sys.__stdout__.write(f"{__version__}\n")  
        sys.exit(0) 

    if  argv.inspect_attr  : 
        print (*Goodies.module_inspection(cv , VideoMediaProcess.CV_PROPERTIES) , sep='\n')  
        sys.exit(0) 
        
    #! Require file as input  ... !!! Raise Brutal Assertion !!!  
    assert argv.file  is not  None  ,  f"require  File  media to proceed\n"
    
    #set  default  window name  if not specified  ... 
    default_window_name  =  ( "SM OCV::Display" ,  argv.window_name)[argv.window_name is not None] 

    #! Dynamic switch mode  (video or image )
    mediastreaming =  (AutoSwitchMode.VIDEO_MODE.value , VideoMediaProcess(argv.file or 0 ))  
    mediastatic    =  (AutoSwitchMode.PICTURE_MODE.value ,  argv.file)
    media_file   =   (mediastreaming , mediastatic) [ cv.imread(argv.file) is not None] 

    fmod = namedtuple("fmod" , [ "mode" ,  "fd"])
    fmod = fmod(*list(media_file))  
    
    #depending  what you give as input it Dynamicly choose the right mode for you 

    if  fmod.mode.__eq__(AutoSwitchMode.VIDEO_MODE.value)  : 
        writablestream  = None 
        if  argv.save  is not None :  
            writablestream = fmod.fd.initiate_stream_record(argv.save ,framecc =argv.set_fcompress)  
        
        #  configure first  
        subt = fmod.fd.use_bgsubalgorithm(argv.bg_algo)  if argv.bg_algo  is not None  else None 
        size = fmod.fd.SIZE  
        if argv.size_resolution : 
            size_dimension =  argv.size_resolution.split("x") 
            if size_dimension.__len__().__ge__(2):  
                size  =  tuple ([ int(dim)  for dim in   size_dimension ]) 

        with fmod.fd as vmprocess  : 
            _ :bool =  vmprocess.isOpened()
            while  _  : 
                _ , video_frame =  vmprocess.read() 
                fps  =  fmod.fd._vframe(vmprocess) 
                resized_vframe = cv.resize(video_frame  ,size[:2] )
                if subt : 
                    mask_filter   = subt.apply(resized_vframe) 
                    cv.findContours(mask_filter, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE) 
        

                cv.imshow(default_window_name , mask_filter if subt  else video_frame ) 
                cv.displayOverlay(default_window_name, f"{default_window_name}\nfps:{fps}" ) 
                keystroke  = cv.waitKey(20) 

                if  keystroke.__eq__(ord('q')) : break  
                if  writablestream and  keystroke.__eq__(ord('s')) : 
                    writablestream.write(video_frame)  
           
            if writablestream  : 
                writablestream.release() 
    else : 
        imgfile =  cv.imread(cv.samples.findFile(fmod.fd)) 
        cv.namedWindow(default_window_name)     
        cv.imshow(default_window_name ,  imgfile) 
        write_once = 0  # only used if argv.Save is defined 
    
        # 'q' for quit  
        while True : 
            keystroke_event_listener =   cv.waitKey(0) &0xff 
            if keystroke_event_listener.__eq__(ord('q')) :
                 cv.destroyAllWindows()  
                 break 
            # 's' for save  
            if argv.save is not None and  keystroke_event_listener == ord('s') :
                sys.__sdtout__.write(f"saved !\n") 
                cv.imwrite(argv.save ,imgfile) 

            if argv.Save and write_once.__eq__(0):
                sys.__stdout__.write(f"auto saved !\n") 
                file_on_cwd = argv.file.split("/").__getitem__(-1) 
                cv.imwrite(file_on_cwd ,imgfile)
                # just avoid overwrite 
                write_once = 1 
                

    return  0   


if __name__.__eq__("__main__")  : 
     main.__call__()  
