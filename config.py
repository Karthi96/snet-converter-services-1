NETWORK = {
    "db": {
        "DB_DRIVER": "mysql+pymysql",
        "DB_HOST": "localhost",
        "DB_USER": "unittest_root",
        "DB_PASSWORD": "unittest_pwd",
        "DB_NAME": "converter_unittest_db",
        "DB_PORT": 3306,
        "DB_LOGGING": True,
    },
}

SLACK_HOOK = {
    "hostname": "",
    "port": 443,
    "path": "",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
}

BLOCKCHAIN_DETAILS = {
    "ethereum": {
        "network": {
            "mainnet": {
                "url": "https://mainnet.infura.io/v3/",
                "secret": {}
            },
            "ropsten": {
                "url": "https://ropsten.infura.io/v3/",
                "secret": {}
            },
            "kovan": {
                "url": "https://kovan.infura.io/v3/",
                "secret": {}
            }
        }
    },
    "cardano": {
        "network": {
            "mainnet": {
                "url": "https://cardano-mainnet.blockfrost.io/api",
                "secret": {
                    "project_id": "project_id"
                }
            },
            "testnet": {
                "url": "https://cardano-testnet.blockfrost.io/api",
                "secret": {
                    "project_id": "project_id"
                }
            }
        }
    }
}

TOPIC_DETAILS= {

}

QUEUE_DETAILS = {
    "CONVERTER_BRIDGE": ""
}


CARDANO_SERVICE_API = {
    "CARDANO_SERVICE_BASE_PATH": "",
    "BURN_TOKEN_URL": "",
    "MINT_TOKEN_URL": ""
}
