This crawler fetches data from http://shopping.com and returns a result for a given keyword.

One can fetch two type of information for a given keyword:
1) No. of results for given keyword
2) All the results for a given keyword and a given page no.

Steps to run:
1) First install Beautiful Soup:
$ pip install beautifulsoup4

2) For first kind of query, run:
$ python pscript.py <keyword>

3) For second kind of query, run:
$ python pscript.py <keyword> <page number>

Some details about files in this repository:
- pscript.py contains basic script to run from command line
- crawler.py contains all the crawler logic
- config.json contains some configuration for a given page. e.g. it tells that to fetch total no. of results look for an element with class "numTotalResults"
- configWriter.py is for modifying the config.json

