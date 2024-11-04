from transstellar.framework import MainConfig, Module

from modules.api_client import APIClient


class CoreModule(Module):

    def bootstrap(self):
        self.__init_api_client__()

    def __init_api_client__(self):
        main_config: MainConfig = self.app.container.get(MainConfig)
        api_client = APIClient(
            main_config.get_api_url(),
            {"debug": self.app.request.config.getini("log_level") == "DEBUG"},
        )

        self.app.container.binder.bind(APIClient, api_client)
