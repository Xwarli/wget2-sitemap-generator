import subprocess
import re
import os

def generate_sitemap(url):
	logfile = url.replace("/", "_").replace(".","-") + "-log.txt"
	smfile = url.replace("/", "_").replace(".","-") + "sitemap.txt"
	command = "wget2 " + url + " -np -e robots=off -w 1 -m --spider -o " + logfile
	print(command)
	subprocess.run(command, shell=Truew)

	# Parse log file to extract URLs
	urls = set()
	with open(logfile, 'r') as log_file:
		for line in log_file:
			# Using regex to find lines containing URLs
			match = re.search(r'URL:\s+(.+)$', line)
			if match:
				url = match.group(1).strip()
				urls.add(url)

	# Write URLs to sitemap file
	with open(smfile, 'w') as sitemap_file:
		for url in urls:
			sitemap_file.write(url + '\n')

	print("Sitemap generated successfully.")

	# Clean up downloaded files
	os.system('rm -rf ' + os.path.join(os.getcwd(), url.split('//')[1]))

# Example usage:
generate_sitemap(input(">>>>"))
