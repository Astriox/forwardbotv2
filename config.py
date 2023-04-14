import os
import logging
class Config:
    
    API_ID = int(os.environ.get("API_ID", "7822571"))
    API_HASH = os.environ.get("API_HASH", "067329e70bfc5b3022f77080703da788")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2089413356:AAGs97YYJvzoTCM20k6HqyT4qKP9r0nNZyw") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "Forward_BOT") 
    OWNER_ID = os.environ.get("OWNER_ID", "1908563535")
    DATABASE_URI = os.environ.get("DATABASE_URI", "")
    DATABASE_NAME = os.environ.get("DATABASE_NAME","Cluster0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Forward_data')
    SESSION = os.environ.get("SESSION", "BQCx5NCv3COUM4uVMSuRjEqFKcWzPYt949WJ71Er1ZlRb7dOBzTq5LZQ7OW74U5Znge6JjoC1vc5sD35nM_vab5X6b5rqb8LCBGUlc-niOz-xHPQQQPSsAFsVx3qOBhovhp_Lj_qcs0N7rKa-6Wncae5bt0svb2OIF8FAEDg14g3U65Y6J9SFno8qeuB1nTdt_vk0Mfe9dpqHtduEbarBqV2FNS1sva0PYAMkAcqdZ_AKtkjDP03Hc1gUB4ZZ7TFPj61ladJYAafWHgEU3e3kYiKglxoKscHnq1l0V6oaJd3UYSN2rZouTR66pLV5Df148AJKZA3wUMIJ0Zj64Z3pB07ccJeTwA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001954127325"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
