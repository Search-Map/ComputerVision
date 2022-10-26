
`g++ -I /usr/include/opencv4 -L /usr/lib/ -g -o ocvcc_gs *.cc \
    -lopencv_core \
    -lopencv_imgproc \
    -lopencv_imgcodecs \
    -lopencv_highgui \
    -lopencv_ml \
    -lopencv_video \
    -lopencv_cvv \
    -lopencv_features2d`

#-lopencv_calib3d -lopencv_objdetect -lopencv_stitching` 
#-lopencv_contrib -lopencv_legacy -lopencv_stitching` 

test  $?  -ne 0  &&  { 
    echo -e "Failure" 
} 
