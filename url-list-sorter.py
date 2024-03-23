# --------------------------------------------------------------------------------------
# 	Witten by Marley Sexton | Github: Xwarli
# 	CC0 License (Public Domain)
# --------------------------------------------------------------------------------------

def url_sorter():
	
	# --- EXAMPLE USAGE ------------------------------------------------------------------
	#
	# This  works on URL lists (not XML) where each lines starts with http(s)://....
	#
	#	Example user imput:
	# 	sm-file -----> list_of_urls.txt
	# 	startw ------> http://example.com
	#
	#	The script will then read each line of the sm-file, and if it starts with 
	# 		http://example.com it will then be added to the "sorted" url list
	#
	# Ultimatly is weeds out any non-standard URLS from the wget2 sitemap script
	# ------------------------------------------------------------------------------------
	
	sm-file = input("Start File: ")
	startw = input("URL to find: ")
	
	file = open(sm-file, "r")
	file2 = open(sm-file + "-sorted", "w+")
	
	for line in file:
		if line.startswith(startw) is True:
			file2.write(line)
			
url_sorter()
