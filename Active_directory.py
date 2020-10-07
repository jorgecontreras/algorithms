class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    users = group.get_users()
    if user in users:
        return True

    for group in group.get_groups():
        if is_user_in_group(user, group):
            return True

    return False

# build hierarchy
parent = Group("parent")
child = Group("child")
sibling = Group("sibling")
sub_child = Group("subchild")
sub_child_sibling = Group("subchild_sibling")

sub_child_user = "sub_child_user"
sub_child_user_x = "sub_child_user_x"
sub_child.add_user(sub_child_user)
sub_child_sibling.add_user(sub_child_user_x)

child.add_group(sub_child)
sibling.add_group(sub_child_sibling)
parent.add_group(child)
parent.add_group(sibling)

# tests
assert is_user_in_group(sub_child_user, parent) == True
assert is_user_in_group(sub_child_user, child) == True
assert is_user_in_group(sub_child_user_x, sub_child) == False
assert is_user_in_group(sub_child_user_x, sub_child_sibling) == True
assert is_user_in_group(sub_child_user_x, sibling) == True
assert is_user_in_group(sub_child_user, sibling) == False
