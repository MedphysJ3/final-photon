The attached scripts runs the pylinac winston-lutz module on the daily qa images taken.  The script looks in a folder with the requirement of being created today and containing files of a certain size and name. It moves the image files from the varian I: drive TDS daily QA folder of a certain size ( 805KB for SMS, 2770KB for Penrose), name "RI" to a newly created shared folder. After the files are moved, they are analyzed using the pylinac WL library.  A pdf is then created and placed in the same folder the images files are in. The scripts are run for both machines at Penrose and both machines at SMC.
