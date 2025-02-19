from django.db.models.signals import post_save
from django.dispatch import receiver
import time, threading
from django.db import IntegrityError
from .models import MyModel  

# Define a signal handler to test synchronous execution
@receiver(post_save, sender=MyModel)
def sync_signal_handler(sender, instance, created, **kwargs):
    print("Signal handler started")
    time.sleep(2)  # Simulating delay
    print("Signal handler finished")

# Define a signal handler to check threading
@receiver(post_save, sender=MyModel)
def thread_check_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal handler executed in thread: {threading.get_ident()}")

# Define a signal handler to check transaction behavior
@receiver(post_save, sender=MyModel)
def transaction_check_signal_handler(sender, instance, created, **kwargs):
    print("Signal handler started for transaction check")
    print("Signal handler finished successfully")  
