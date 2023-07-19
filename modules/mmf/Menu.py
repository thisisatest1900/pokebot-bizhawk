import logging

import fastjsonschema

from modules.Config import GetConfig
from modules.mmf.Common import LoadJsonMmap

log = logging.getLogger(__name__)
config = GetConfig()

menu_schema = {
    "type": "object",
    "properties": {
        "encounterCursor": {"type": "number"}
    }
}

MenugValidator = fastjsonschema.compile(menu_schema)  # Validate the data from the mmf, sometimes it sends junk


def GetMenu():
    while True:
        try:
            menu = LoadJsonMmap(4096, "bizhawk_menu_data-" + config["bot_instance_id"])["menu"]
            if MenugValidator(menu):
                return menu
        except Exception as e:
            log.debug("Failed to GetMenu(), trying again...")
            log.debug(str(e))
