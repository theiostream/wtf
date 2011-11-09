# wtf -- translates common Internet acronyms

## About
This is a Python clone of the **wtf** sh script from NetBSD, the special acronym translator!

It's based on the original <a href="http://cvsweb.de.netbsd.org/cgi-bin/cvsweb.cgi/src/games/wtf/">**wtf** sh script</a>, and also uses the same main acronym database, which is very rich and complete :)

## Installation
To install this clone of **wtf**, just run:
`curl raw.github.com/link | sh`

To build from source:
`$ git clone git://git.github.com/theiostream/wtf.git`
`$ ./wtf/install/install.sh`

The `install.sh` script will put **wtf** inside */usr/bin*, and will rename any other file named *<b>wtf</b>* to *wtf-old*.

## Usage
Dead simple:
`$ wtf [-f dbfile / -d dbdir] [is] <acronym>`

For more detail on usage, refer to the manual:
`$ man 6 wtf-py`

## Creating a dbfile
It is extremely basic: It is basically:
<pre>
`ACRONYM	meaning
`ANOTHERACR	meaning`
</pre>

As you can see, using both `\t` and ` ` is valid to split acronym and meaning. But note that if you choose to use ` ` as a separator, you can't use `\t` in a part of the package description.

Also note that all acronyms should be written in *CAPS*.

## Why the clone?
There are many advantages on using this port of **wtf**. These are the main ones:

### Developer-related:
* Code is way more dynamic as it's written in Python
* Handles arguments in a better way (using the optparse module)

### For the user happiness:
* Loads from a more human-readable directory (*/Library/**wtf**/lists/*) by default
* Looks recursively for ADBs in directory specified with -d flag
* Gets only useful data from *whatis*

## Why the original script?
The original version of **wtf** searches into *pkg_info*'s database, and into *pkgsrc*'s help facility. That isn't available on most non-BSD operating systems, so this clone lacks looking into it.

That should weight plenty to you if you are a BSD user. If so I'd stick with the original script.

## Credits
* The NetBSD folks, who made:
    * The original **wtf** script
    * The (amazingly big and used by this tool) standard ADB
    * The man page for **wtf**

## More Info
Feel free to visit this <a href="http://wiki-static.aydogan.net/wtf">wiki article</a> under the NetBSD distro of **wtf**.