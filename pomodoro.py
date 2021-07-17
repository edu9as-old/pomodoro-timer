import argparse

parser = argparse.ArgumentParser()

parser.add_argument("hour_start", help="Hour when you start working",
                    type=int)
parser.add_argument("min_start", help="Minutes when you start working",
                    type=int)
parser.add_argument("hour_end", help="Hour when you end working",
                    type=int)
parser.add_argument("min_end", help="Minutes when you end working",
                    type=int)
parser.add_argument("-w", "--work", help="Minutes of each work period",
                    type=int, default = 25)
parser.add_argument("-s", "--short", help="Minutes of each short break period",
                    type=int, default = 5)
parser.add_argument("-l", "--long", help="Minutes of each long break period",
                    type=int, default = 10)
parser.add_argument("-n", "--nworks", help="Work sessions between long breaks",
                    type=int, default = 3)
parser.add_argument("-i", "--language", help="Language",
                    type=str, default = "en")

args = parser.parse_args()

hour_start = args.hour_start
min_start = args.min_start
hour_end = args.hour_end
min_end = args.min_end
work = args.work
short = args.short
nworks = args.nworks
long_break = args.long
language = args.language

# Two languages by the moment: English and Spanish. All the texts are stored in
# a dictionary

text_en = {"prompt": "At {:0>2}:{:0>2} do some {} for {} minutes!",
           "work": "WORK",
           "short": "SHORT BREAK",
           "long": "LONG BREAK",
           "t_error": "Time of start must be sooner than time of finishing.",
           "a_error": "Invalid argument:",
           "exit": "Exiting program..."}

text_es = {"prompt": "¡A las {:0>2}:{:0>2} es hora de {} durante {} minutos!",
           "work": "TRABAJO",
           "short": "DESCANSO CORTO",
           "long": "DESCANSO LARGO",
           "t_error": ("La hora de inicio debe ser anterior a la hora de "
                     "finalización del trabajo."),
           "a_error": "Argumento inválido:",
           "exit": "Terminando programa..."}


################################################################################

"""
def check_argument(arg, valid_arg, valid_values = False):
    try:
        assert(type(arg) == type(valid_arg))
    except AssertionError:
        print(prompt["a_error"], arg)
        print(prompt["exit"])
        exit()

    if valid_values:
        try:
            print(arg)
            print(valid_values)
            assert(arg in valid_values)
            
        except AssertionError:
            print(prompt["l_error"], prompt["exit"], sep = "\n")
            exit()
"""

def pomodoro(hour_start, min_start, hour_end, min_end, 
             work = 25, short = 5, long_break = 10, nworks = 3):
    time = hour_start*60 + min_start
    end = hour_end*60 + min_end
    try:
        assert(time < end)
    except AssertionError:
        print(prompt["error"], prompt["exit"], sep = "\n")
    
    work = (work, prompt["work"])
    short = (short, prompt["short"])
    long_break = (long_break, prompt["long"])
    while time < end:
        for period in ((work, short)*nworks)[:-1] +(long_break,):
            hour = time//60
            minute = time%60
            print(prompt["prompt"].format(hour, minute, period[1], period[0]))
            time += period[0]
            if time > end:
                break


if __name__ == "__main__":
    prompt = {"en": text_en, "es": text_es}[language]
    """
    for group in zip(list(vars(args).keys())[:-1],
                    [1,1,1,1,1,1,1]):
        arg = vars(args)[group[0]]
        check_argument(arg, group[1])
    """
    
    pomodoro(hour_start, min_start, hour_end, min_end, nworks = nworks, 
             work = work, short = short, long_break = long_break)
