execute_process(COMMAND "/home/bluerov23/v3Bluerov/build/som_wall_detection/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/bluerov23/v3Bluerov/build/som_wall_detection/catkin_generated/python_distutils_install.sh) returned error code ")
endif()