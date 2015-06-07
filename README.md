Theory of Change generator
=============================

Overview
--------------

A tool that allows a specification of all the layers in the theory of change model and the interactions bewteen them. 

Generates an html document that shows each layer in order with the links in between.

usage:
```bash
$ python toc.py isa-toc.json 'ISA TOC' > gentoc.html
```

Will output the html file so that you can open it. 

Specification
-----------------

The `isa-toc.json` file is a good example. First, there's an order field that
specifies the layers, in order. For each string in the order field, there's a 
key that maps to a list of [id, string] for each box that you want to make for that
layer. Finally, at the bottom, there's a 'links', and each key is again the name
in the orders array. However, the key is of the top layer, and the links are 
associated with the bottom layer. The link format is an array of [topid, bottomid].

Changing the order of the [id,string] combos will change the order in the final 
document and keep all the links intact.



