import sys

file = open("url_db.json", "a")
file.write(sys.argv[1])
file.write('\n')
file.close()
