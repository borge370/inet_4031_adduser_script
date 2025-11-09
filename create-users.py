
#!/usr/bin/python3

# INET4031
# Evan Borgen
# Nov 9 2025

# import os needed to adjust files. Couldn't use adduser without it.
import os
# used to search for strings
import re
# required for user input from our .input file
import sys

def main():
    for line in sys.stdin:

        # skip comment lines
        match = re.match("^#",line)

        # reads input from file - each field is seperated by a ":"
        fields = line.strip().split(':')

        # skip over comments and skip over inputs w/o 5 fields
        if match or len(fields) != 5:
            continue

        # reads inputs and places them in fields[] array to display later
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # split for users that belong to multiple groups
        groups = fields[4].split(',')

        # debugging line to assure the code is working intentionally
        print("==> Creating account for %s..." % (username))
        # add username
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # print username then adjust the actual file with os.
        print(cmd)
        os.system(cmd)

        # debug line to assure code working
        print("==> Setting the password for %s..." % (username))
        # execute passwd cmd to adjust user password - sudo privledges needed for file adjustment
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # print passwd and then adjust the actual file with os.
        print(cmd)
        os.system(cmd)

        for group in groups:
            # assign groups
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
