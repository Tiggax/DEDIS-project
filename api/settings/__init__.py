import os


print(os.environ.get("ENV_TYPE"))


from .default import *
if os.environ.get("ENV_TYPE") in ['Production', "prod", "Prod"]:
    from .prod import *
else:
    from .dev import *