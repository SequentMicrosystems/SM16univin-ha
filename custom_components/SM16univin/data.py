FULL_NAME = "Sixteen Analog/Digital Inputs"
LINK = "https://sequentmicrosystems.com/products/sixteen-analog-digital-inputs-8-layer-stackable-hat-for-raspberry-pi"

import lib16univin
API = lib16univin.SM16univin
DOMAIN = "SM16univin"
NAME_PREFIX = "sm16ui"
SM_MAP = {
    "binary_sensor": {
        "dig": {
                "chan_no": 16,
                "com": {
                    "get": "get_dig_in",
                },
        },
    },
    "button": {
        "dig_rst": {
                "chan_no": 16,
                "com": {
                    "get": "reset_dig_in_counter",
                },
        }
    },
    "switch": {
        "dig_cnt_en": {
                "chan_no": 16,
                "com": {
                    "get": "get_dig_in_cnt_en",
                    "set": "set_dig_in_cnt_en",
                },
        },
    },
    "sensor":  {
        "dig_cnt": {
                "chan_no": 16,
                "com": {
                    "get": "get_dig_in_counter",
                    "set": "set_dig_in_counter",
                },
        },
        "u": {
                "chan_no": 16,
                "uom": "V",
                "com": {
                    "get": "get_u_in",
                },
        },
        "r1k": {
                "chan_no": 16,
                "uom": "Ohm",
                "com": {
                    "get": "get_r1k_in",
                },
        },
        "r10k": {
                "chan_no": 16,
                "uom": "Ohm",
                "com": {
                    "get": "get_r10k_in",
                },
        },
    },
    "datetime": {
        "rtc": {
                "chan_no": 1,
                "com": {
                    "get": "get_rtc",
                    "set": "set_rtc",
                },
        },
    },
}
