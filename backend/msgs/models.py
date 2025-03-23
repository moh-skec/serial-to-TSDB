from clickhouse_backend import models
from django.utils import timezone


class Msg(models.ClickhouseModel):
    id = models.UInt32Field(primary_key=True)
    slug = models.StringField()
    description = models.StringField()
    sensor_id = models.UInt32Field()
    sensor_name = models.StringField()
    time = models.DateTimeField(default=timezone.now)
    value = models.Float64Field()

    engine = models.MergeTree(order_by=["id"])

    def __str__(self):
        return f'{self.id} - {self.slug}'
