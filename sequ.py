import subprocess

def run():
    file = open('url_db.json', 'r')

    for url in file:
        subprocess.call(["python", "insertFeed.py", url])

if __name__ == "__main__":
    import sys
    run()
