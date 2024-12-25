import os

from git import Repo
import datetime as dt
tgl = dt.datetime.now().strftime("%y%m%d_%H%M%S")
os.chdir('/content/images')

full_local_path = "/content/images"

repo = Repo(full_local_path)
repo.git.add("-A")
repo.index.commit(tgl)

origin = repo.remote(name="origin")
origin.push()

os.chdir('/content')
