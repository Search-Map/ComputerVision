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
#include <string> 
#include <cstring> 
#include <cstdlib>  
#include <sstream>
#include <iterator>

#if defined _POSIX_C_SOURCE >= 2 || _XOPEN_SOURCE
#include  <unistd.h>  
#endif 

#include "include/goodies.hh" 

void argument_parser (  int  & argc  , char *const *argv  ,  FlagsEntryHdl_t  & arg_flags_hdl ){
    int option  ; 

    char  *program_basename  = argv[argc-1] ; 
     
    if  (argc  == 1 )  
    { 
        HELP(program_basename)   
    }
    while (  (option  = getopt(argc , argv ,  FLAGS) ) != -1  ) 
    {
        switch  (option) 
        {
            case 'v':  
                VERSION
                exit(EXIT_SUCCESS);  
            case 'f':
               arg_flags_hdl.file =  optarg ;  
               break ;
            case 's':
              arg_flags_hdl.save  = true ; 
              break ; 
            case 'r': 
              arg_flags_hdl.file_rename = optarg  ; 
              break; 
            case 'h':  
               HELP(program_basename)
               exit(EXIT_SUCCESS);  
            default :
               std::cerr<<" Unrecognize argument : " << argv[optind-1]  << std::endl ;  
               exit(EXIT_FAILURE) ;

        }
    }

}
