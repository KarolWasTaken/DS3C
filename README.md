[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)


## Due to the newest Dark Souls III update, this program no longer works. It can only be used by manually inputting the death data in. If I can, I will implement a fix.
## fix implemented in the form of a ![new project](https://github.com/KarolWasTaken/sldc)


## Screenshots

![App Screenshot](https://cdn.discordapp.com/attachments/467018961259855872/916074446333288448/unknown.png)
# DS3C
Hello! This is my first proper program. I kind of made this because I was bored. You know how it is, right? Sitting down in your chair, opening and closing games you dont even feel like playing; only doing so to speed up the passage of time until either the end of the day has been reached, or someone texts you for whatever reason.
Any reason will do - its not like you're busy. 
Well, I got bored of idly sitting around and waiting for life to pass me by (striking I know) so I began a project. 
I wrote some simple code on my arduino to make button that counts how many times I press it then I thought, "Maybe I can read the output with python."
So I installed [pyserial](https://pyserial.readthedocs.io/en/latest/index.html#) and got to work. The idea was I press the button every death but eventually I wondered if I can make this program increment automatically. 
I remembered about a library called [ReadWriteMemory](https://pypi.org/project/ReadWriteMemory/) that basically reads and writes the memory of any process - a bit like Cheat Engine.
Thanks to [RandomDavis](https://www.youtube.com/watch?v=Pv0wx4uHRfM) I found out how to do that. From there to now, we got the program I've released today. 
# How To Use DS3C
This is a pretty simple program to use. When the counter has loaded in, press 'y' 
on your keyboard to bring up the options menu. In there you'll be able to edit the number of deaths, font, font and 
background colour, and savedata location; aswell as reset the settings back to default and, most importantly, connect your 
game to Dark Douls 3!
# WARNING
I don't THINK this program can ban a player BUT I could be wrong. It doesn't attach itself 
to the game - or attach any kind of debugger to it either. It simply reads the current health value of the player in a similar way that 
Cheat Engine does. Always exercise caution when it comes to things like this. To stay extra safe you could:
- Turn your steam to offline mode
- Turn your Dark Souls into offline mode
- Make a second steam account and family share Dark Souls 3 to it
## Deployment

To run this project just run 'DarkSoulsDeathCount.exe' on the [release page](https://github.com/TohruTheMaid/DS3C/releases)


## Acknowledgements

 - [Random Davis](https://www.youtube.com/channel/UCEtOy2t4jLY7oNGHfdlMHvA)


## Dependencies
To run the code files, install the following dependencies

- [tkinter](https://tkdocs.com/tutorial/install.html)(preinstalled with python)
- [pywin32](https://pypi.org/project/pywin32/)
- [psutil](https://pypi.org/project/psutil/)
- [pypresence](https://pypi.org/project/pypresence/3.2.0/)


## Authors

- [@TohruTheMaid](https://github.com/TohruTheMaid)

