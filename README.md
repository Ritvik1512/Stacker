# Stacker!

<b> I'm not at all certain about the working of this thing, as this was developed at 3 in morning and might be full of crappy code, proceed at your own risk. </b>
<p align="center">

Yo! You a developer? You need stacker. Period. <br/>

<b>Stacker</b> lives and works in your heart, I mean, your command line. <br/> </p>

***

## Features (aka Dope Shit)

+ Written in Python.
+ Allows a seamless experience directly from Command line. Even allows, integrated error reporting and searching on SO
+ All you Apple and Linus Trovaldis fans, this works on Mac and Linux.

## Installation

** Build from this repo**

Clone the repository, then use setup.py to install the package.

    $ git clone https://github.com/Ritvik1512/stacker.git
    $ cd stacker
    $ python setup.py install

Hey, depending on your environment, you may need to `sudo python setup.py install`.

## Usage

We are gonna set an alias, `stacker`, for stacker_arc.py's functionality, for ease of access.


### CLI arguments
+ `-exec`: `--executable`: Searches by the errors thrown by running an executable.
+ `-srh`: `--search`: search by the given query
+ `-h`, `--help`: Help!
+ `--version`: Version bruh
+ `-t`: `--tags`: searches by tags ofcourse!
+ `--verbose`: Complete text of question and answer

### Commands:
+ `mo`: more: shows the next 5 questions
+ `--ln`: opens focused question in browser
+ #: select: shows full question//top answer text in focus
+ `--q`: exit: go back to the list focus

### Examples
Let's search Stack Overflow for "How do I write HelloWorld in jQuery?" along with the tags, "jQuery";

    $ stacker -srh "How do I install HelloWorld in jQuery?" -tg "jQuery"

## Thanks <3

+ [Py-StackExchange](https://github.com/lucjon/Py-StackExchange): a Python wrapper for the StackExchange API

## Contributing to this beauty

If you want to write code:

1. Fork the repository
2. Create your feature branch (`git checkout -b slick-feature`)
3. Commit (`git commit -am 'add some feature'`)
4. Push it (`git push origin slick-feature`)
5. Create a new Pull Request!
