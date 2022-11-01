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


from  typing  import  Dict , List , Tuple ,  TypeVar  

pym_  = TypeVar("pymodule")
smg_  = TypeVar("smgmodule")  

os  : pym_ = __import__("os") 
sys : pym_ = __import__("sys")
argp: pym_ = __import__("argparse") 


def  SmGoodies ( goodies  )  : ... 


@classmethod  
def argument_handler(goodies , _defcall_)  : 
    def bundler  (  *args,  **kwargs):
        stdarg  = argp.ArgumentParser(description ="Simple Open CV programme  to Get started ") 
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



def  build_arguments_from_dictionary ( goodies ,  **kwargs  ) : ...  


_smgoodies_map_ :  Dict[str , any]   = {
        "__init__" : SmGoodies , 
        "argctrl" :argument_handler
        } 


Goodies: smg_  =  type("goodies" ,() , _smgoodies_map_ ) 

