from clickhouse_backend.models import ClickhouseModel

def get_subclasses(cls):
    subclasses = set(cls.__subclasses__())
    for subclass in subclasses.copy():
        subclasses.update(get_subclasses(subclass))
    return subclasses


class ClickHouseRouter:
    _route_model_names = None

    def _load_route_model_names(self):
        if self._route_model_names is None:
            self._route_model_names = set()
            for model in get_subclasses(ClickhouseModel):
                if model._meta.abstract:
                    continue
                self._route_model_names.add(model._meta.label_lower)

    def _get_db_for_routing(self, model, hints):
        self._load_route_model_names()
        if model._meta.label_lower in self._route_model_names or hints.get("clickhouse"):
            return "clickhouse"
        return None

    def db_for_read(self, model, **hints):
        return self._get_db_for_routing(model, hints)

    def db_for_write(self, model, **hints):
        return self._get_db_for_routing(model, hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        self._load_route_model_names()
        if f"{app_label}.{model_name}" in self._route_model_names or hints.get("clickhouse"):
            return db == "clickhouse"
        elif db == "clickhouse":
            return False
        return None
