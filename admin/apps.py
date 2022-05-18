import environ
import yaml
from django.apps import AppConfig

env = environ.Env(
    APPS=(str, ""),
)

for app_dict in yaml.safe_load(env("APPS")) or []:
    class_name = app_dict["name"].replace(".", "")
    class_name = class_name[0].upper() + class_name[1:]
    globals()[class_name] = type(
        class_name,
        (AppConfig,),
        {
            "name": app_dict["name"],
            "db": app_dict["db"],
        },
    )
