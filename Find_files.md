# Problem 2 - File Recursion

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing, which can be downloaded here:

./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
Python's os module will be useful—in particular, you may want to use the following resources:

os.path.isdir(path)

os.path.isfile(path)

os.listdir(directory)

os.path.join(...)

Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

# solution
1. check the contents of the given path
2. for every element found, check if it's a file.
3. If the element is a file, verify if it has the provided extension, in which case to add it to the result array.
4. If the element is a directory, call the function itself, using recursion, to repeat steps 1-3.
5. return the result array

# time complexity
The time it takes to execute will depend on the number of files, numbers of sub-directories and number of files in each sub-directory.
The program will have to check each element once, so the time is **0(n)** where n is the total number of files in the path (including subdirectories)

# space
No additional space is required for traversing the tree. 
The generated output depends on the number of matches found, being the worst case that all files have the given suffix. Hence, space is **O(N)**