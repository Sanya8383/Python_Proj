import routeros_api
from app.schemas.mk_schemas import AddrList, PostResponse
from app.config import MKTIK_IP, MKTIK_PASS, MKTIK_USER


def get_mk_address_list() -> list:
    connection = routeros_api.RouterOsApiPool(MKTIK_IP, username=MKTIK_USER, password=MKTIK_PASS,
                                              port=8728, plaintext_login=True)
    api = connection.get_api()
    list_address = api.get_resource('/ip/firewall/address-list/')
    test = list_address.get()
    connection.disconnect()
    return test


def del_mk_address_list_by_ip():
    connection = routeros_api.RouterOsApiPool(MKTIK_IP, username=MKTIK_USER, password=MKTIK_PASS,
                                              port=8728, plaintext_login=True)
    api = connection.get_api()
    list_address = api.get_resource('/ip/firewall/address-list/')
    test = list_address.get()
    if list_address.get(address='192.168.88.88'):
        list = list_address.get(address='192.168.88.88')
        for id in list:
            list_address.remove(id=id['id'])
    test = list_address.get()
    connection.disconnect()


def add_mk_ip_to_address_list(addr_lst: AddrList):
    connection = routeros_api.RouterOsApiPool(MKTIK_IP, username=MKTIK_USER, password=MKTIK_PASS,
                                              port=8728, plaintext_login=True)
    api = connection.get_api()
    list_address = api.get_resource('/ip/firewall/address-list/')
    if not list_address.get(address=str(addr_lst.address), list=str(addr_lst.list)):

        list_address.add(list=str(addr_lst.list), address=str(addr_lst.address))

        connection.disconnect()

        resp = {'code' : '201', 'msg' : f'address {addr_lst.address} added to address list {addr_lst.list}'}
        return resp
    else:

        connection.disconnect()
        resp = {'code' :400, 'msg': f'address {addr_lst.address} already in address list {addr_lst.list}'}
        return resp


if __name__ == '__main__':
    # get_mk_address_list()
    # del_mk_address_list_by_ip()
    al = AddrList(address = '10.10.1.1', list = 'lst')
    add_mk_ip_to_address_list(al)
