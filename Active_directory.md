# Problem 4 - Active Directory.

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.
Write a function that provides an efficient look up of whether the user is in a group.

# solution

Directories can be traversed easily using recursion. In this problem am searching for the user in the current group, 
and if not found, going recursively into each of hte subgroups until found, or no more groups to search.

# time complexity

The time depends on the number of users in the directory, including all subgroups. It is linear time **O(N)**

# space
no additional space, space is constant, regardless of number of users or groups **O(1)** 