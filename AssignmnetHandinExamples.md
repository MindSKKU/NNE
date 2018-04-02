# Assignment Handin Examples

Do not use .rar file. Only .zip file can be accepted.

## Linux OS
### Wrong example
    ~/path/201XXXXXXX$ ls
    YourAnswer.py NNE_Assignment1_Softmax.ipynb ReadMe
    ~/path/201XXXXXXX$ zip 201XXXXXXX.zip YourAnswer.py NNE_assignment1_Softmax.ipynb ReadMe
### Correct example
    ~/path$ l
    201XXXXXXX/
    ~/path$ zip -r 201XXXXXXX.zip 201XXXXXXX
    
    
## Mac OS
### Wrong example
![wrong](https://github.com/MindSKKU/NNE/blob/master/pictures/Screen%20Shot%202018-03-28%20at%203.51.45%20PM.png)

### Correct example
![Correct](https://github.com/MindSKKU/NNE/blob/master/pictures/Screen%20Shot%202018-03-28%20at%203.51.59%20PM.png)


## Window OS
In window OS, if you decompress zip file, program makes another directory with same name of zip file. But in Linux OS, default is decompressing in the current directory. So we recommend you to unzip your file on Linux and check whether another directory is created or not.
