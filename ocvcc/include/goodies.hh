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

#if !defined goodies_searchmap_ocvcc 
#define      goodies_searchmap_ocvcc  

#define   FLAGS  "vsf:hr:"  //!  
#define  VERSION   std::cout << "Search-Map  OpenCV v0.1" <<std::endl ;  
#define  WIN_DEFAULT_NAME  "Search Map Viewer <press 'q' to Exit" 
#define  USAGE_DETAIL std::cout <<  

#define  HELP(__programme_basename) std::cout  <<  "USAGE: " <<\
    __programme_basename << " [option] [-vshrf] [-f <filename>] [-r <new filename>]" <<std::endl;

#define SAVE 's'  //!0x73
#define QUIT 'q'  //!0x71 

//! Add more option  you want to deal with argument flags!!!   
typedef  struct  {
    std::string  file ;             //! Store the filename entry  
    std::string  file_rename ;      //! rename filename   entry 
                                    //  if the flag -r  is used the file is  automatically saved
                                    //  even the -s (save) option has not been  specified  ... 
                
    bool save  ;                    //! save  the filename entry in the current path 
                                    //! when  -r (rename) flag is not specified 
                                    //  it takes the default file and saves:c it in current path         

} FlagsEntryHdl_t ; 
 
void  argument_parser  ( int  & __argc  , char * const *__argv  ,  FlagsEntryHdl_t  &__args_hdl  ) ; 

#endif //! goodies_searchmap_ocvcc   
