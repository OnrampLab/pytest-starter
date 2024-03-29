from urllib.parse import urlparse

from transstellar_antd.v5 import Page, Spin

from modules.account import AccountConfig

from .admin_header import AdminHeader
from .admin_sidebar_menu import AdminSidebarMenu


class AdminLayout(Page):
    admin_header: AdminHeader
    admin_sidebar_menu: AdminSidebarMenu

    def init(self):
        self.admin_header = self.find_global_element(AdminHeader)
        self.admin_sidebar_menu = self.find_global_element(AdminSidebarMenu)

    def __wait_for_loading_disappear__(self):
        self.wait_for_global_element_to_disappear(Spin)

    def logout(self):
        self.__wait_for_loading_disappear__()
        self.admin_header.logout()

    def switch_account(self, account: AccountConfig):
        self.__wait_for_loading_disappear__()
        self.admin_header.switch_account(account)
