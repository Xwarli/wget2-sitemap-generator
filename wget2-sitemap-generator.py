# --------------------------------------------------------------------------------------
# 	Witten by Marley Sexton | Github: Xwarli
# 	CC0 License (Public Domain)
# --------------------------------------------------------------------------------------
import subprocess
import re
import os

def generate_sitemap(url):
	# creates the log file and sitemap (sm) file names
	#	example: http://example.com --> http:__example-com[-log/sitemap].txt
	logfile = url.replace("/", "_").replace(".","-") + "-log.txt"
	smfile = url.replace("/", "_").replace(".","-") + "-sitemap.txt"

	# creates the command. wget2, no parent, robots off, wait 1sc, mirror, spider
	# outputs all to the logfile above
	command = "wget2 " + url + " -np -e robots=off -w 1 -m --spider -o " + logfile
	
	# prints the command for user feedback/error spotting, then runs the subprocess
	print(command)
	subprocess.run(command, shell=True)

	# Parse log file to extract URLs
	urls = set()
	with open(logfile, 'r') as log_file:
		for line in log_file:
			# Using regex to find lines containing URLs
			match = re.search(r'URL:\s+(.+)$', line)
			if match:
				url = match.group(1).strip()
				urls.add(url)

	# Write URLs to the prenamed sitemap file
	with open(smfile, 'w') as sitemap_file:
		for url in urls:
			sitemap_file.write(url + '\n')

	# user feeback
	print("Sitemap generated successfully.")

	# Clean up downloaded files
	os.system('rm -rf ' + os.path.join(os.getcwd(), url.split('//')[1]))

# Gets user input for the starting URL
generate_sitemap(input("Starting URL: "))
