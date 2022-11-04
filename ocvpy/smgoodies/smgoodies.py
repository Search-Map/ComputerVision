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


#! Sugar  syntaxic  annotation  
pym_  = TypeVar("pymodule")
smg_  = TypeVar("smgmodule")  

os  : pym_ = __import__("os") 
sys : pym_ = __import__("sys")
argp: pym_ = __import__("argparse") 


def  SmGoodies ( goodies  )  : ... 


@classmethod 
def argparse ( goodies , flags_dictionary , sep =",") : 
    
    def argument_handler(_defcall_)  : 
        stdarg  = argp.ArgumentParser(description ="Simple Open CV programme  to Get started ") 
        for key , value  in flags_dictionary.items() :  
            _value =  value.split(sep)
            __key =  f"--{key}"

            # NOTE  add  '_' at  the end of  the flag to enable action 
            if  __key.__getitem__(-1).__eq__("_")  : 
                __key = __key[0:-1]  
                stdarg.add_argument(_value.__getitem__(0), __key, action="store_true", help=_value.__getitem__(1) or " " ) 

            else : 
                stdarg.add_argument(_value.__getitem__(0) , __key , help=_value.__getitem__(1) or " " ) 

        def bundler  (  *args,  **kwargs):
            argv_handler = stdarg.parse_args()
            args = [args] 
            args.__iadd__([argv_handler])  
            args.__delitem__(0)  
            _defcall_(*args  ,  **kwargs)

        return  bundler  
    return argument_handler 





_smgoodies_map_ :  Dict[str , any]   = {
        "__init__" : SmGoodies , 
        "argctrl" :argparse
        } 


Goodies: smg_  =  type("goodies" ,() , _smgoodies_map_ ) 
