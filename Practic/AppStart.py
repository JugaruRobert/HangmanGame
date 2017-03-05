from Practic.Controller.Controller import *
from Practic.Repository.Repo import *
from Practic.UI.UI import *

repo=repo()
controller=controller(repo)
UI=UI(controller)
UI.start()