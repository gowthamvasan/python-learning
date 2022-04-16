from distutils.command.upload import upload
from django.db import models
from django.db import connections

# Create your models here.

class Servers(models.Model):   
    instance_name = models.CharField(max_length=255)
    instance_id = models.AutoField(primary_key=True)
    instance_type = models.CharField(max_length=255)
    private_ip = models.CharField(max_length=255)
    public_ip = models.CharField(max_length=255)
    instance_role = models.CharField(max_length=255)
    environment = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    security_group = models.CharField(max_length=255)
    avail_zone = models.CharField(max_length=255)
    subnet_id = models.CharField(max_length=255)
    vpc_id = models.CharField(max_length=255)
    arch_type = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        db_table = "server_inventory"

class Rds(models.Model):   
    id = models.AutoField(primary_key=True)
    db_name = models.CharField(max_length=255)
    db_instance_name = models.CharField(max_length=255)
    db_type = models.CharField(max_length=255)
    db_storage = models.CharField(max_length=255)
    db_engine = models.CharField(max_length=255)
    db_engine_ver = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    environment = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    workload_type = models.CharField(max_length=255)
    db_endpoint = models.CharField(max_length=255)
    db_vpc_id = models.CharField(max_length=255)
    db_read_replica_db = models.CharField(max_length=255)

    class Meta:
        db_table = "rds_inventory"
