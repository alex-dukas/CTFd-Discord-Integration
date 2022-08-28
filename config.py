import os

CURRENT_PATH = os.getenv("CTF_BOT_ROOT") or os.getcwd()

class ProductionConfig():
    TOKEN = os.getenv("CTF_BOT_TOKEN") or ""
    PREFIX = "?"
    CTFD_BASE_URL = "http://ctf.bsidesstpete.com"
    JSON_FILE_PATH = CURRENT_PATH + "/user-tokens.json"
    TEMP_DATA_PATH = CURRENT_PATH + "/temp.json"
    UPDATE_TIME = 90
    UPDATE_CHAN_ID = 1001182631792218303
    ADMIN_TOKEN = os.getenv("CTF_BOT_ADMIN_TOKEN") or ""

class TestingConfig(ProductionConfig):
    TOKEN = ""
    UPDATE_TIME = 60
    UPDATE_CHAN_ID = 0
    ADMIN_TOKEN = ""

Config = ProductionConfig()