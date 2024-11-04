from transstellar.framework import Application
from transstellar.framework import (
    ApplicationBootstrapper as BaseApplicationBootstrapper,
)

from modules.account import AccountModule
from modules.auth import AuthModule
from modules.core import CoreModule
from modules.dashboard.dashboard_module import DashboardModule


class ApplicationBootstrapper(BaseApplicationBootstrapper):
    def bootstrap(self, app: Application):
        app.register_module(CoreModule)
        app.register_module(AccountModule)
        app.register_module(AuthModule)
        app.register_module(DashboardModule)
