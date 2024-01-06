from django.test import TestCase
import uuid


def generate_uuid():
    x=1
    pkey=uuid.uuid4().hex
    pkey+=str(x)
    x+=1
    return pkey


print(generate_uuid())