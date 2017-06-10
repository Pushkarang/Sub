#!/bin/python3
import subscene
import sys
import requests,zipfile,io
if len(sys.argv)>1:
	print("Searching for subtitles...\n")
	film = subscene.search(str(" ".join(sys.argv[1:])))
	print(" ".join(sys.argv[1:]))
	if len(film.subtitles)>0:
		print("Film Found\n",film)
		d = []
		count = 0
		for i in film.subtitles:
			if i.language=="English":
				d.append(i)
				count = count+1
				print(count,":",i.title)
		print("Select subtitle : ")
		c = int(input())
		su = d[c-1]
		url = su.zipped_url
		r = requests.get(url)
		z = zipfile.ZipFile(io.BytesIO(r.content))
		z.extractall()
		print("Done..")
else:
	print("Enter SUB [movie_name]")				

