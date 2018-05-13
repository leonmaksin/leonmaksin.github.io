#!/usr/bin/python
print "Content-type: text/html\n"

import string

import cgi

import cgitb
cgitb.enable()

import random

A = 'ABUNDANT, ADAPTABLE, ADORABLE, ADORED, ADVENTUROUS, AFFABLE, AFFECTIONATE, AGREEABLE, ALLOWING, ALTRUISTIC, AMAZING, AMBITIOUS, AMIABLE, AMICABLE, AMUSING, ANGELIC, APPRECIATED, APPRECIATIVE, AUTHENTIC, AWARE, AWESOME'
B = 'BALANCED, BEAUTIFUL, BELOVED, BEST, BEYOND-FABULOUS, BLESSED, BLISSFUL, BLITHESOME, BOLD, BRAVE, BREATHTAKING, BRIGHT, BRILLIANT, BROAD-MINDED'
C = 'CALM, CAPABLE, CAREFUL, CARING, CENTERED, CHAMPION, CHARISMATIC, CHARMING, CHEERFUL, CHERISHED, COMFORTABLE, COMMUNICATIVE, COMPASSIONATE, CONFIDENT, CONSCIENTIOUS, CONSIDERATE, CONTENT, CONVIVIAL, COURAGEOUS, COURTEOUS, CREATIVE, CUTE'
D = 'DANDY, DARING, DAZZLED, DECISIVE, DEDICATED, DELICIOUS, DELIGHTFUL, DESIRABLE, DETERMINED, DILIGENT, DIPLOMATIC, DISCREET, DIVINE, DYNAMIC'
E = 'EAGER, EASYGOING, EMOTIONAL, EMPATHIC, EMPATHETIC, EMPOWERED, ENCHANTED, ENDLESS, ENERGETIC, ENERGIZED, ENLIGHTENED, ENLIVENED, ENOUGH, ENTHUSIASTIC, ETERNAL, EXCELLENT, EXCITED, EXHILARATED, EXPANDED, EXPANSIVE, EXQUISITE, EXTRAORDINARY, EXUBERANT'
F = 'FABULOUS, FAIR-MINDED, FAITHFUL, FANTASTIC, FAVORABLE, FEARLESS, FLOURISHED, FLOWING, FOCUSED, FORCEFUL, FORGIVING, FORTUITOUS, FRANK, FREE, FREE-SPIRITED, FRIENDLY, FULFILLED, FUN, FUN-LOVING, FUNNY'
G = 'GENEROUS, GENIAL, GENIUS, GENTLE, GENUINE, GIVING, GLAD, GLORIOUS, GLOWING, GODDESS, GOOD, GOOD HEALTH, GOODNESS, GRACEFUL, GRACIOUS, GRATEFUL, GREAT, GREGARIOUS, GROUNDED'
H = 'HAPPY, HAPPY-HEARTED, HARD-WORKING, HARMONIOUS, HEALTHY, HEARTFULL, HEARTWARMING, HEAVEN, HELPFUL, HIGH-SPIRITED, HOLY, HONEST, HOPEFUL, HUMOROUS'
I = 'ILLUMINATED, IMAGINATIVE, IMPARTIAL, INCOMPARABLE, INCREDIBLE, INDEPENDENT, INEFFABLE, INNOVATIVE, INSPIRATIONAL, INSPIRED, INTELLECTUAL, INTELLIGENT, INTUITIVE, INVENTIVE, INVIGORATED, INVOLVED, IRRESISTIBLE'
J = 'JAZZED, JOLLY, JOVIAL, JOYFUL, JOYOUS, JUBILANT, JUICY, JUST, JUVENESCENT'
K = 'KIND, KIND-HEARTED, KISSABLE, KNOWINGLY, KNOWLEDGEABLE'
L = 'LIVELY, LOVABLE, LOVED, LOVELY, LOVING, LOYAL, LUCKY, LUXURIOUS'
M = 'MAGICAL, MAGNIFICENT, MARVELOUS, MEMORABLE, MIND-BLOWING, MINDFUL, MIRACLE, MIRACULOUS, MIRTHFUL, MODEST'
N = 'NEAT, NICE, NIRVANA, NOBLE, NON-RESISTANT, NOURISHED, NURTURED'
O = 'OPEN, OPEN-HEARTED, OPEN-MINDED, OPTIMISTIC, OPULENT, ORIGINAL, OUTSTANDING, OWNING-MY-POWER'
P = 'PASSIONATE, PATIENT, PEACEFUL, PERFECT, PERSISTENT, PHILOSOPHICAL, PIONEERING, PLACID, PLAYFUL, PLUCKY, POLITE, POSITIVE, POWERFUL, PRACTICAL, PRECIOUS, PRO-ACTIVE, PROPITIOUS, PROSPEROUS'
Q = 'QUICK-WITTED, QUESTIONING'
R = 'RADIANT, RATIONAL, READY, RECEPTIVE, REFRESHED, REJUVENATED, RELAXED, RELIABLE, RELIEVED, REMARKABLE, RENEWED, RESERVED, RESILIENT, RESOURCEFUL, RICH, ROMANTIC'
S = 'SACRED, SAFE, SATISFIED, SECURED, SELF-ACCEPTING, SELF-CONFIDENT, SELF-DISCIPLINED, SELF-LOVING, SENSATIONAL, SENSIBLE, SENSITIVE, SERENE, SHINING, SHY, SINCERE, SMART, SOCIABLE, SOULFUL, SPECTACULAR, SPLENDID, STELLAR, STRAIGHTFORWARD, STRONG, STUPENDOUS, SUCCESSFUL, SUPER, SUSTAINED, SYMPATHETIC'
T = 'THANKFUL, THOUGHTFUL, THRILLED, THRIVING, TIDY, TOUGH, TRANQUIL, TRIUMPHANT, TRUSTING'
U = 'ULTIMATE, UNASSUMING, UNBELIEVABLE, UNDERSTANDING, UNIQUE, UNLIMITED, UNREAL, UPLIFTED'
V = 'VALUABLE, VERSATILE, VIBRANT, VICTORIOUS, VIVACIOUS'
W = 'WARM, WARMHEARTED, WEALTHY, WELCOMED, WHOLE, WHOLEHEARTEDLY, WILLING, WISE, WITTY, WONDERFUL, WONDROUS, WORTHY'
X = 'XOXO'
Y = 'YOUNG-AT-HEART, YOUTHFUL, YUMMY'
Z = 'ZAPPY, ZESTFUL, ZING'

header1 = '''<!DOCTYPE html>
<html>
    <head>
        <title>Happy Mother's Day!</title>'''
header2 = '''    </head>
    <body>
        <form action="mothersDay2018.py">
            Please Enter your Name: <input type="text" name="username"></input>
            <input type="submit" value="Enter" name="submit">
        </form>'''

foot = '''    </body>
</html>'''

def getOne(words):
    x = random.randint(0,(len(words) - 1))
    return words[x]

def makeLetterToWord():
    original = '''    if letter == 'a' or letter == 'A':
        wList = A.split(', ')
        return getOne(wList)'''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        working = original
        working = working.replace('a',letter)
        working = working.replace('A',letter.upper())
        print working

def letterToWord(letter):
    if letter == 'a' or letter == 'A':
        wList = A.split(', ')
        return getOne(wList)
    if letter == 'b' or letter == 'B':
        wList = B.split(', ')
        return getOne(wList)
    if letter == 'c' or letter == 'C':
        wList = C.split(', ')
        return getOne(wList)
    if letter == 'd' or letter == 'D':
        wList = D.split(', ')
        return getOne(wList)
    if letter == 'e' or letter == 'E':
        wList = E.split(', ')
        return getOne(wList)
    if letter == 'f' or letter == 'F':
        wList = F.split(', ')
        return getOne(wList)
    if letter == 'g' or letter == 'G':
        wList = G.split(', ')
        return getOne(wList)
    if letter == 'h' or letter == 'H':
        wList = H.split(', ')
        return getOne(wList)
    if letter == 'i' or letter == 'I':
        wList = I.split(', ')
        return getOne(wList)
    if letter == 'j' or letter == 'J':
        wList = J.split(', ')
        return getOne(wList)
    if letter == 'k' or letter == 'K':
        wList = K.split(', ')
        return getOne(wList)
    if letter == 'l' or letter == 'L':
        wList = L.split(', ')
        return getOne(wList)
    if letter == 'm' or letter == 'M':
        wList = M.split(', ')
        return getOne(wList)
    if letter == 'n' or letter == 'N':
        wList = N.split(', ')
        return getOne(wList)
    if letter == 'o' or letter == 'O':
        wList = O.split(', ')
        return getOne(wList)
    if letter == 'p' or letter == 'P':
        wList = P.split(', ')
        return getOne(wList)
    if letter == 'q' or letter == 'Q':
        wList = Q.split(', ')
        return getOne(wList)
    if letter == 'r' or letter == 'R':
        wList = R.split(', ')
        return getOne(wList)
    if letter == 's' or letter == 'S':
        wList = S.split(', ')
        return getOne(wList)
    if letter == 't' or letter == 'T':
        wList = T.split(', ')
        return getOne(wList)
    if letter == 'u' or letter == 'U':
        wList = U.split(', ')
        return getOne(wList)
    if letter == 'v' or letter == 'V':
        wList = V.split(', ')
        return getOne(wList)
    if letter == 'w' or letter == 'W':
        wList = W.split(', ')
        return getOne(wList)
    if letter == 'x' or letter == 'X':
        wList = X.split(', ')
        return getOne(wList)
    if letter == 'y' or letter == 'Y':
        wList = Y.split(', ')
        return getOne(wList)
    if letter == 'z' or letter == 'Z':
        wList = Z.split(', ')
        return getOne(wList)
    if letter == ' ':
        return '-'
    if letter in string.punctuation:
        return letter
    if letter in '1234567890':
        return letter

def nameToList(name):
    nameList = []
    for letter in name:
        nameList.append(letterToWord(letter))
    return nameList

def nameToHTML(name):
    words = nameToList(name)
    print '        <h1><img src="Images/rose1.png">     Happy Mother\'s Day!    <img src="Images/rose1.png"></h1>'
    print "        <div id='rwords'><i>"
    for word in words:
        print '            <p>' + '<b>' + word[0] + '</b>' + word[1:] + '<p>'
    print "        </i></div>"

def getData():
    formData = cgi.FieldStorage()
    username = formData.getvalue('username')
    return username

def submitted():
    formData = cgi.FieldStorage()
    submit = formData.getvalue('submit')
    return submit

print header1
if submitted() == 'Enter':
    print '        <link rel="stylesheet" href="styleMom.css">'
else:
    print '        <link rel="stylesheet" href="style.css">'
print header2
username = getData()
username = '{0}'.format(username)
if username != 'None':
    nameToHTML(username)
    print '        <h2>By Leon Maksin</h2>'
print foot
