# Zero-To-Mastery-Python
This is a repo for the projects in the Zero-To-Mastery Python Developer course

### JPEG to PNG Converter
The **jpg_to_png.py** file saves a copy of the jpeg file as a png file. It requires the directory of the .jpg files to given as the first argument and the second argument to be the directory for saving the .png files created.

To use the program:

- clone the repo and cd into the Zero-To_Mastery directory from command line
- run the program using python and give the directory containing the .jpg files as the first argument and the directory for storing the .png files as the second argument
- after running the program, the .jpg files will remain in the original directory and new .png copies of the files will be in the second directory given

**Example**

$ python jpg_to_png.py ./jpeg_folder/ ~/Pictures

The file directory exists
File test_image_1.jpg has been opened
The file has been saved as test_image_1.png
File test_image_2.jpg has been opened
The file has been saved as test_image_2.png
File test_image_3.jpg has been opened
The file has been saved as test_image_3.png



### Password Checker
The **password_checker.py** file will check whether a password has ever been leaked. It does this by checking the SHA1 hash of the given password against the SHA1 hash of passwords leaked as stated from the API https://api.pwnedpasswords.com/range/

To use the program:

- clone the repo and cd into the Zero-To-Mastery directory from command line
- run the program using python and you can either pass one or more passwords as an argument or you can pass a txt file which contains passwords in them
- the program will return the password or passwords you entered and the number of times it has been leaked

**Examples**

$ python password_checker.py password123

password123 was found to be leaked 248071 times
done!

$ python password_checker.py my_passwords.txt

cars12345 was found to be leaked 1134 times
password123 was found to be leaked 248071 times
baseball999 was found to be leaked 284 times
secret143 was found to be leaked 946 times
done!
