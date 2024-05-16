from typing import Any, Optional

from django.db import models


class AutoRouter:
    admin_labels = {"admin", "auth", "contenttypes", "sessions"}

    def get_db(self, model: models.Model) -> str:
        if model._meta.app_label in self.admin_labels:
            return "default"
        return getattr(model._meta.app_config, "db", None)

    def db_for_read(self, model: models.Model, **hints: Any) -> str:
        return self.get_db(model)

    def db_for_write(self, model: models.Model, **hints: Any) -> str:
        return self.get_db(model)

    def allow_relation(self, obj1: models.Model, obj2: models.Model, **hints: Any) -> Optional[bool]:
        return self.db_for_write(obj1) == self.db_for_write(obj2)

    def allow_migrate(
        self, db: str, app_label: str, model_name: Optional[models.Model] = None, **hints: Any
    ) -> Optional[bool]:
        if app_label in self.admin_labels:
            return db == "default"
        return None
