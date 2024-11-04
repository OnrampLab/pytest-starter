from transstellar.framework import Module, Route

from .pages.dashboard_page import DashboardPage


class DashboardModule(Module):

    def bootstrap(self):
        self.app.register_routes(
            [
                Route("/", "dashboard", DashboardPage),
            ]
        )
