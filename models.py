"""
This is models file for CRR servers inventory
"""
# pylint: disable=invalid-name
from django.db import models
from django.utils.timezone import now


class Server(models.Model):
    """
    model class for server-inventory 
    """
    testbed = models.CharField(max_length=255,)
    fi_details = models.TextField()  # Fabric Interconnect details
    serial = models.CharField(max_length=255,)  # Server serial number
    management_ip = models.CharField(max_length=255,)  # Server IP address
    owner = models.CharField(max_length=255,)  # Owner of the server
    health_status = models.CharField(max_length=255, default="Up")  # # Status of the server Up/Down
    down_since = models.DateTimeField(null=True, blank=True)  # Track when it went down
    reason = models.CharField(max_length=255,)
    last_checked = models.CharField(max_length=255,)
    server_type = models.TextField(max_length=255,)  # server_type information
    location_details = models.TextField(max_length=255,)
    adapters_details = models.TextField(max_length=255,)  # server_type information
    server_model = models.TextField(max_length=255,)  # server_type information
    claimed_to = models.CharField(max_length=255, blank=True, null=True)
    server_pid = models.CharField(max_length=255, blank=True, null=True)
    chassis = models.CharField(max_length=255, blank=True, null=True)
    fex = models.CharField(max_length=255, blank=True, null=True)
    storage_controllers = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    cimc_ip = models.CharField(max_length=255, blank=True, null=True)  # cimc IP address
    host_ip = models.CharField(max_length=255, blank=True, null=True)  # host IP address
    esxi_ip = models.CharField(max_length=255, blank=True, null=True)  # ESXI IP address
    hardware_code_name = models.CharField(max_length=100, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return f"Server {self.serial} in server_name {self.testbed}"  # Corrected field reference

    def is_down_longer_than(self, minutes):
        """
        Check if the server has been down for longer than the given minutes.
        """
        if self.down_since:
            return (now() - self.down_since).total_seconds() / 60 > minutes
        return False
