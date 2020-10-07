import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    def find_helper(suffix, path):
        subdir_files = []
        
        #validating that the provided path is in fact a directory path
        if not os.path.isdir(path):
            # handle edge case
            if os.path.isfile(path) and path.endswith(suffix):
                return path

            return []

        for p in os.listdir(path):
            if os.path.isfile(os.path.join(path,p)) and p.endswith(suffix):
                subdir_files.append('{}/{}'.format(path, p))
                continue
            
            #using "path.join()" rather than slash for cross-platform compatibility
            subdir_files += find_helper(suffix, os.path.join(path, p)) 

        return subdir_files
    
    files = find_helper(suffix, path)

    return files

# test case 1
print("Test case 1:")
path = "./testdir"
suffix = ".c"
files = find_files(suffix, path)
print(files)

# test case 2 - pass the path to the file directly
print("Test case 2:")
path = "testdir/subdir3/subsubdir1/b.h"
suffix = ".h"
print(find_files(suffix, path))

# test case 3 - empty path
print("Test case 3:")
path = ""
suffix = ".h"
print(find_files(suffix, path))

# test case 4 - empty suffix - will return all files
print("Test case 4:")
path = "./testdir"
suffix = ""
print(find_files(suffix, path))

# test case 5 - empty both - returns empty array
print("Test case 5:")
path = ""
suffix = ""
print(find_files(suffix, path))

# test case 6 - no match - returns empty array
print("Test case 6:")
path = "./testdir"
suffix = ".pdf"
print(find_files(suffix, path))

# test case 7 - non existent path
print("Test case 7:")
path = "./this/path/does/not/exist"
suffix = ""
print(find_files(suffix, path))
