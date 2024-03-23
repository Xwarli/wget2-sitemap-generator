# wget2-sitemap-generator
Simple script to generate a text file (.txt) of URLs from a given website using the wget2 command (with mirror and spider opitions enabled). 

---- USAGE ----
> sudo python3 wget2-sitemap-generator.py

You will then be prompted to enter a valid URL

The script will run silently, and initially create a single "-log.txt" file. Once the website has been crawled, it will use this file to generate a "-sitemap.txt" file containing a list of URLs. 

These may require further sorting as desired as they occationally have non-target URLs creep in; but in general it only grabs desired URLs. If they do, then use:
> sudo python3 url-list-sorter.py

And then enter the URL list .txt file, and the desired target URL (i.e. https://example.com), and it'll create a "-sorted.txt" file which will only include all the lines that start with your desired URL.


