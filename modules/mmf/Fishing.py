import logging

import fastjsonschema

from modules.Config import GetConfig
from modules.mmf.Common import LoadJsonMmap

log = logging.getLogger(__name__)
config = GetConfig()

fishing_schema = {
    "type": "object",
    "properties": {
        "subTask": {"type": "number"},
    }
}

FishingValidator = fastjsonschema.compile(fishing_schema)  # Validate the data from the mmf, sometimes it sends junk


def GetFishing():
    while True:
        try:
            fishing = LoadJsonMmap(4096, "bizhawk_fishing_data-" + config["bot_instance_id"])["fishing"]
            if FishingValidator(fishing):
                return fishing
        except Exception as e:
            log.debug("Failed to GetTrainer(), trying again...")
            log.debug(str(e))
