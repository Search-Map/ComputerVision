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

import cv2 as cv , sys, argparse 


def argument_handler (_defcall_)  : 
    def bundler  (  *args,  **kwargs):
        stdarg  = argparse.ArgumentParser(description ="Simple Open CV programme  to Get started ") 
        stdarg.add_argument("-f" , "--file" ,  help="load file media")
        stdarg.add_argument("-w" ,"--window-name" , help="Personalize your Window name")  
        stdarg.add_argument("-s"  ,"--save" , help="Named your Saved file media") 
        stdarg.add_argument("-v" , "--version" , action="store_true" ,  help="print Version")  
        #TODO :  you can add more command  ...  
        argv_handler = stdarg.parse_args()
        args = [args] 
        args.__iadd__([argv_handler])  
        args.__delitem__(0)  
        _defcall_(*args  ,  **kwargs)

    return  bundler ;  


@argument_handler     
def main (*argv ,**kwargs) :
    argv  = argv.__getitem__(0) 

    if  argv.version :
        sys.__stdout__.write(f"{__version__}\n")  
        sys.exit(0) 

    
    #! Require file as input  ... !!! Raise Brutal Assertion !!!  
    assert argv.file  is not  None  ,  f"require  File  media to proceed\n"
    
    #set  default  window name  if not specified  ... 
    default_window_name  =  ( "SM OCV::Display" ,  argv.window_name)[argv.window_name is not None]  
    
        
    media_file_image  = cv.imread(cv.samples.findFile(argv.file)) 
    if  media_file_image is None : 
        sys.exit(1) 

    cv.namedWindow(default_window_name)     
    cv.imshow(default_window_name , media_file_image) 
    keystroke =  0 
    
    # 'q' for quit  
    while  keystroke != ord('q'):
        keystroke = cv.waitKey(0) 

        # 's' for save
        if argv.save is not None and  keystroke == ord('s') :
            cv.imwrite(argv.save ,media_file_image ) 


if __name__.__eq__("__main__")  : 
    main.__call__()  
