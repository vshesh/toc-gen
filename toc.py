#!/python
from sys import argv
from toolz import *
import json

header='''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
  <style>
    body {
      text-align:center;
      font-family: Campton, sans-serif;
    }

    .flex-row {
      width:100%;
      display:flex;
      flex-direction: row;
      margin-bottom: 10px;
    }

    .flex-row > div {
      overflow: scroll;
      border: 2px solid #ffee00;
      margin: 0 5px;
      padding: 5px;
    }


    .flex-col {
      height:100%;
      display:flex;
      flex-direction: column;
    }

    .flex-1{
      flex:1;
      display:flex;
      align-items:center;
      justify-content: center;
    }

    svg > line {
      stroke: black;
    }
  </style>
</head>
<body>'''

footer='''</body>
</html>'''

def process(f):
  data=json.load(open(f))
  order = list(sliding_window(2,data['order']))

  # make the first boxes
  print '<div class="flex-row '+order[0][0]+'">'
  for k,v in data[order[0][0]]:
    print '<div class="flex-1"><p class="vertical-align">'+v+'</p></div>'
  print '</div>'

  for e in order:
    topn = len(data[e[0]])
    botn = len(data[e[1]])
    toporder = list(pluck(0, data[e[0]]))
    botorder = list(pluck(0, data[e[1]]))
    # make the lines between the first/second elements
    print '<svg viewBox="0 0',(topn*botn),int(topn*botn/20),'">'
    for t,b in data['links'][e[0]]:
      print '<line x1="',botn*(toporder.index(t)+0.5),'" x2="',topn*(botorder.index(b)+0.5),'" y1="0" y2="',int(topn*botn/20),'" stroke-width="',(topn*botn/1100),'"></line>'
    print '</svg>'
    # make the elements of the second element
    print '<div class="flex-row '+e[1]+'">'
    for k,v in data[e[1]]:
      print '<div class="flex-1"><p class="vertical-align">'+v+'</p></div>'
    print '</div>'

if __name__ == '__main__':
  if len(argv) < 3: 
    print 'usage: toc.py tocfile.json title'
  else:
    print header
    print '<h1 class="title">'+argv[2]+'</h1>'
    process(argv[1])
    print footer

































