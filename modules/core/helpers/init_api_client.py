from injector import Injector
from interstellar.framework import MainConfig

from ..api_client import APIClient


def init_api_client(injector, config):
    main_config = injector.get(MainConfig)
    api_client = APIClient(
        main_config.get_api_url(), {"debug": config.getini("log_level") == "DEBUG"}
    )

    injector.binder.bind(APIClient, api_client)
