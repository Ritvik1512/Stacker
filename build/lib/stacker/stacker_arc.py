#!/usr/bin/env python
#import statements
import stackexchange
from stackexchange import Sort
import os
import subprocess
from __future__ import print_function
import click
import sys
from __future__ import unicode_literals
import html2text
from __future__ import print_function
import json
import urllib2
import sys
import re


if sys.version_info[:2] < (3, 0):
    input = raw_input

NUM_RESULTS = 5
#API_KEY = "3GBT2vbKxgh*ati7EBzxGA(("
API_KEY = "*s)qiqv5gMYkpvjJN)w*9g(("
VERSION_NUM = "1.0.0"

usr_api_key = API_KEY

h2t = html2text.HTML2Text()

sok = stackexchange.Site(stackexchange.StackOverflow, app_key=usr_api_key, impose_throttling=True)
sok.be_inclusive()

class Config():
    """ Main configuration object """
    def __init__(self):
        self.stderr = False
        self.search = False
        self.verbose = False
        self.tag = False
        self.wiki = False
        


passing_configuration = click.make_pass_decorator(Config, ensure=True)


def select(questions, num):
    print_full_question(questions[num - 1])
    working = True
    while working:
        usr_in = click.prompt("Yo bruh, I'm Ritvik and I developed this awesome shit called Stacker, which is command line StackOverflow. So now, go ahead and type ln to launch browser, srh to return to search, or q to quit")
        if usr_in == 'ln':
            click.launch(questions[num - 1].json['link'])
        elif usr_in == 'q':
            sys.exit()
        elif usr_in == 'srh':
            click.echo("\n" * 12)
            ogn = 0
            if not num % NUM_RESULTS:
                ogn = num - NUM_RESULTS
            else:
                ogn = num - num % NUM_RESULTS
            for j in range(ogn, ogn + NUM_RESULTS):
                print_question(questions[j], j + 1)
            working = False
        else:
            click.echo(click.style(
                "Hey! The input entered was not recognized! Are you drunk bruh? :P",
                fg="red",
                err=True))


def focus_question(questions):
    working = True
    while working:
        usr_in = click.prompt("Please enter a ques no. to select, mo for more and q to quit")
        if usr_in == 'mo':
            working = False
        elif usr_in == 'q':
            sys.exit()
        elif usr_in.isnumeric() and int(usr_in) <= len(questions):
            select(questions, int(usr_in))
        else:
            click.echo(click.style(
                "Hey! The input entered was not recognized! Are you drunk bruh? :P",
                fg="red",
                err=True))


def _search(config):
    click.echo('Tags: {0}'.format(configs.tag))
    click.echo('Finding: {0}...'.format(configs.term))
    

    questions = sok.search_advanced(
        q=config.term,
        sort=Sort.Votes,
        tagged=config.tag.split())
        

    count = 0
    question_logs = []
    add_it_logs = question_logs.append
    for question in questions:
        if 'accepted_answer_id' in question.json:
            count += 1
            add_to_logs(question)
            print_question(question, count)

            if count % NUM_RESULTS == 0:
                focus_question(question_logs)

    if not questions:
        click.echo(
            click.style(
                "Aw Snap! Mother of Node.js, your search \'{0}\' along with the tags \'{1}\' returned no results. :( Should we try again bruh?".format(config.term, config.tag),
                fg="red",
                err=True))
        sys.exit(1)


def print_question(question, count):
    ansid = question.json['accepted_answer_id']

    ans = h2t.handle(sok.answer(ansid, body=True).body)
    if len(answer) > 200:
        answer = ''.join([answer[:200], '...'])

    click.echo(''.join([
        click.style(''.join([str(count), '\nQuestion: ', question.title]), fg='white'),
        ''.join(['\nAnswer:', answer, "\n"]),
    ]))


def get_term(config):
    if config.search:
        return config.search
    elif config.stderr:
        with open(os.devnull, 'wb') as DEVNULL:
            process = subprocess.Popen(
                config.stderr,
                stdout=DEVNULL,
                stderr=subprocess.PIPE, shell=True)

        output = process.communicate()[1].splitlines()
        if not len(output):
            click.echo(click.style(
                "Yo, executable does NOT throw an error.",
                fg="red"))
            sys.exit(1)

        return str(output[-1])
    return ""


def print_full_question(question):
    ansid = question.json['accepted_answer_id']

    questiontext = h2t.handle(sok.question(question.id, body=True).body)
    ans = h2t.handle(sok.answer(ansid, body=True).body)

    click.echo(''.join([
        click.style(''.join([
            "\n\n-----------------------------------------------------------------Here is the question----------------------------------------------------------------------------------\n\n",
            question.title, '\n', questiontext,
        ]), fg='green'),
        ''.join([
            "\n-------------------------------------------------------------------And here is the answer------------------------------------",
            answer,
        ]),
    ]))


def search_verbose(term):
    questions = so.search_advanced(q=term, sort=Sort.Votes)
    question = questions[0]
    print_full_question(question)


@click.command()

@click.option("-exec", "--executable", default="", help="It runs an exec and posts errors obtained to SO. Cool shit!")
@click.option("-tg", "--tags", default="", help="Searches the StackOverflow for specified tags bruh")
@click.option("-srh", "--search", default="", help="Searches StackOverflow for the query bruh")
@click.option("-v", "--verbose", is_flag=True, help="Displays the complete text of the relevant ques and ans bruh")
@click.option("-V", "--version", is_flag=True, help="Displays the version info bruh")
@click.option("-W", "--wiki", default="", help="Searched the wikipedia for what you want" )
@pass_config
def main(config, search, stderr, tag, verbose, version, wiki):
    """ Parses command-line arguments for Stacker """
    config.search = search
    config.stderr = executable
    config.tag = tags
    config.verbose = verbose
    config.wiki = wiki

    config.term = get_term(config)

    if verbose:
        search_verbose(config.term)
    elif search or stderr:
        _search(config)
    elif version:
        click.echo("You are using {VERSION_NUM}".format(**globals()))
    elif wiki:
        KEY = 0

    base_url = "http://en.wikipedia.org/w/api.php?"

    action = "action=query"


    Format = "&format=json"


    titles="&titles="




    def get_title():
        title = raw_input('What do you want to know about?\n')
        title = title.replace(' ','_')
        global titles
        titles = titles + title



    def url_and_displaytitle():
        print('\ntitle and url for this wikipedia site',end="\n")
        global base_url
        global action
        global titles
        global Format
        prop = "&prop=info"
        inprop = "&inprop=url|displaytitle"
        url = base_url + action + titles + prop + inprop + Format
        result = json.load(urllib2.urlopen(url))  
        key = result['query']['pages'].keys()
        global KEY
        KEY = (key[0][:])
        print(result['query']['pages'][str(KEY)]['title'])
        print(result['query']['pages'][str(KEY)]['fullurl'])
        print('\t-------------------\t')
        


    def interesting_links():
        print('\nyou may also be interested in the following links',end="\n") 
        global base_url
        global Format
        global action
        global titles
        prop = "&prop=extlinks"
        try:
            url = base_url + action + titles + prop + Format
            result =json.load(urllib2.urlopen(url))
            key = result['query']['pages'].keys()
            key = key[0][0:]
            j = 0
            offset = result['query-continue']['extlinks']['eloffset']
            while j < offset:
                print(result['query']['pages'][str(key)]['extlinks'][j])
                j=j+1
        except:
            print('sorry,couldn\'t find any links') 




#def interwiki_links():
 #   print('inter wiki links found for this search',end="\n")
  #  base_url
   # action
   #  titles
  #  prop = "&prop=iwlinks"
  #  url = base_url + action + titles + prop
  #  print(url)
  #  result = urllib2.urlopen(url)
  #  for i in result:
  #      print(i)




    def wiki_search():
        global base_url
        global action
        global titles
        global Format
        prop = "&prop=extracts"
        plaintext = "&explaintext"
        section_format = "&exsectionformat=plain"
        try:
            url = base_url + action + titles + prop + plaintext + section_format + Format
            result = json.load(urllib2.urlopen(url))
            key = result['query']['pages'].keys()
            key = key[0][0:]
            print(result['query']['pages'][str(key)]['extract'],end="\n")
        except:
            print('oops!,no wikipedia page for that title.Wikipedia search titles are case Sensitive...')
    




def images():
        print('\nall images related to this search',end="\n")
        image_url = "http://en.wikipedia.org/wiki/"
        global base_url
        global Format
        global action
        global titles
        prop = "&prop=images"
        url = base_url + action + titles + prop + Format
        result = json.load(urllib2.urlopen(url))
        key = result['query']['pages'].keys()
        key = key[0][0:]
        try:
            i = 1
            while(i):
                Image = str(result['query']['pages'][str(key)]['images'][i]['title'])
                image = image_url + Image.replace(' ','_')
                print(image)
                i=i+1
        except:
            print('\t------------------\t',end="\n")
            pass     

    def featured_feed():
        global base_url
        Format = "&format=json"
        action = "&action=featuredfeed"
        try:
            feed = "&feed=" + str(sys.argv[1])
            url = base_url + action + feed + Format
            print(url)
            result = urllib2.urlopen(url).read()
            res1 = re.compile('<title>(.*)</title>')
            res2 = re.compile('<link>(.*)en</link>')
            Result1 = re.findall(res1,result)
            Result2 = re.findall(res2,result)
            for i in enumerate(zip(Result1,Result2)):
                print(i)
        except:
            print('error!')


        if len(sys.argv) < 2:
            get_title()
            wiki_search()
            url_and_displaytitle()
            images()
    #interwiki_links()
        interesting_links()
        else:
            featured_feed()

    else:
        click.echo(
            click.style(
                "What do you want bruh? No argument is given, so please do both of us a favour just go ahead and use --help for help",
                fg="red",
                err=True))
        sys.exit(1)

if __name__ == '__main__':
    main()
