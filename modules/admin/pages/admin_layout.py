from transstellar_antd.v5 import Page

from modules.account import Account

from .admin_header import AdminHeader
from .admin_sidebar_menu import AdminSidebarMenu


class AdminLayout(Page):
    def init(self):
        self.admin_header: AdminHeader = self.find_global_element(AdminHeader)
        self.admin_sidebar_menu: AdminSidebarMenu = self.find_global_element(
            AdminSidebarMenu
        )

    def wait_for_ready(self):
        self.admin_header.wait_for_ready()
        self.admin_sidebar_menu.wait_for_ready()

    def logout(self):
        self.admin_header.logout()

    def switch_account(self, account: Account):
        self.admin_header.switch_account(account)
        self.init()
