# Simple Pomodoro Timer

In this script I have developed a very simple Pomodoro timer to enhance your working time.

## What is Pomodoro?
To explain what this technique is, I am referencing <>:
"This popular time management method asks you to alternate pomodoros – focused work sessions – with frequent short breaks to promote sustained concentration and stave off mental fatigue."

The time of each work session or break periods can be chosen by the user to what fits best for him/her. There are multiple webpages that implement timers with this technique, but these have some problems related to Internet connection; whenever you lose your Internet connection, you lose the track of your working time.

## My program
In this script I have put emphasis on these two issues. Thanks to its simplicity, you can print to your console at which times you have to be working or taking a break with no need of a stable Internet connection all the time! Also, you can select all the parameters related to your Pomodoro working time:

- **Start of working time**: the first two arguments in the script are defined by the hour you are starting working.
- **End of working time**: the next two arguments depend on when are you finishing your working time.

For example, if you plan to work from eight o'clock to half-past twelve, you should run the script like this:
```python pomodoro.py 8 00 12 30```

There are some extra options:
- **Time of each working session**: if you want to be focused 30 minutes between breaks, you should introduce a **-w** or **--work** argument like this:
```python pomodoro.py 8 00 12 30 -w 30```
- **Time of each short break**: how many minutes would you like to invest in each short break? By default this time is set to 5 minutes, but maybe you need 8 minutes? If so, you can introduce a **-s** or **--short** argument like this:
```python pomodoro.py 8 00 12 30 -s 8```
- **Time of each short break**: what about long breaks? By default this period lasts 10 minutes, but what if you want to spend 15 minutes to relax in each long break? Then, you can introduce a **-l** or **--long** argument like this:
```python pomodoro.py 8 00 12 30 -l 15```
- **Number of work sessions between long breaks**: by default, I have set 3 working sessions between long breaks, but you are free to set this number to whichever you want thanks to the **-n** or **--numwork**. For example, if you only want 2:
```python pomodoro.py 8 00 12 30 -n 2```
- **Language**: you can run this code in English (en) or Spanish (es) with the option **-i** or **--language**. If you are Spanish:
```python pomodoro.py 8 00 12 30 -i es```

## Usage

I have prepared a demo for you on [Google Colab](https://colab.research.google.com/github/edu9as-old/pomodoro-timer/blob/main/pomodoroDemonstration.ipynb).

## Installation
### Linux
Ensure you have Python installed by running:

```python --version```

If you can see the version of your Python interpreter (hopefully 3.*.*), you can go on. If not, you must install Python before running this code.

Now enter this line of code in your console to download the program:

```wget https://raw.githubusercontent.com/edu9as/tools/main/pomodoro/pomodoro.py```

Next, to run the program, enter ```python pomodoro.py``` followed by the four mandatory arguments (hour of start and end of work) and the optional arguments you want.

### Windows
Ensure you have Python installed by running:

```python --version```

If you can see the version of your Python interpreter (hopefully 3.*.*), you can go on. If not, you must install Python before running this code.

Next, install Pomodoro program by running. Inset the path to the folder where you want the program to be stored instead of **<PATH>**:

```[io.file]::WriteAllText("<PATH>\pomodoro.py",(Invoke-WebRequest -URI "https://raw.githubusercontent.com/edu9as/tools/main/pomodoro/pomodoro.py").content)```

Next, to run the program, enter ```python pomodoro.py``` followed by the four mandatory arguments (hour of start and end of work) and the optional arguments you want.
