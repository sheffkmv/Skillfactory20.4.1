from api2 import pf
from settings import valid_email, valid_password, non_valid_email, non_valid_password
import pytest


def test_get_api_key_for_valid_user(email = valid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_for_valid_user(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_create_pet_simple_for_valid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    params = {
        "name":"barsik",
        "animal_type":"cat",
        "age":"5"
    }
    status, result = pf.create_pet_simple(auth_key, params)
    assert status == 200
    assert len(result) > 0


def test_delete_pet_for_valid_user():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    auth_key = auth_key['key']
    status = pf.delete_pet(auth_key, pet_id='26afef6a-24f4-438f-a7fc-4d05c4007fa3')
    assert status == 200
