import re

from models import Celebrity, Crime

def name_link(item):
  name = item.name
  if type(item) == Celebrity:
    link = '/celebrities/{id}'.format(id=item.id)
  elif type(item) == Crime:
    link = '/crimes/{id}'.format(id=item.name)
  return '<a href="{link}">{name}</a>'.format(name=name, link=link)

def date_formatter(d):
  return '{month} {day}, {year}'.format(month=d.strftime('%B'), day=d.day, year=d.year)

def stripTwitter(string):
  if string[0] == '@':
    return string[1:]
  else:
    return string

def firstSentence(string):
  string = string[24:]
  res1 = re.search(r'.+<br />', string)
  # Some amount of anything followed by a break tag. (First paragraph)
  res1 = res1.group(0)[:-6] if res1 else ''
  res2 = re.search('[^.]+\.', string)
  # Some amount of not periods followed by a period. (First sentence)
  res2 = res2.group(0) if res2 else ''

  res = res1 if len(res1) > len(res2) else res2
  # This is necessary because some descriptions only have a single paragraph
  # and thus no break tag, and some names have a '.' in them (Robert Downey
  # Jr.) thus truncating early. This picks the longest option as the most
  # correct one.
  if len(res) > 138:
    res = res[:138]
    res += '...'
  return res

def entireFirstSentence(string):
  res1 = re.search(r'.+<br />', string)
  # Some amount of anything followed by a break tag. (First paragraph)
  res1 = res1.group(0)[:-6] if res1 else ''
  res2 = re.search('[^.]+\.', string)
  # Some amount of not periods followed by a period. (First sentence)
  res2 = res2.group(0) if res2 else ''

  res = res1 if len(res1) > len(res2) else res2
  # This is necessary because some descriptions only have a single paragraph
  # and thus no break tag, and some names have a '.' in them (Robert Downey
  # Jr.) thus truncating early. This picks the longest option as the most
  # correct one.
  if len(res) > 138:
    res = res[:138]
    res += '...'
  return res
