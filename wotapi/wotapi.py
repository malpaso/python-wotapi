""" WotApi """
import requests

try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        try:
            from django.utils import simplejson as json
        except ImportError:
            raise ImportError('A json library is required to use this python library.')

from .exceptions import *


class WotApi(object):

    def __init__(self, server=''):

        server_configs = {
            'RU': ('http://api.worldoftanks.ru', '171745d21f7f98fd8878771da1000a31',),
            'EU': ('http://api.worldoftanks.eu', 'd0a293dc77667c9328783d489c8cef73',),
            'NA': ('http://api.worldoftanks.com', '16924c431c705523aae25b6f638c54dd',),
            'ASIA': ('http://api.worldoftanks.asia', '39b4939f5f2460b3285bfa708e4b252c',),
            'KR': ('http://api.worldoftanks.kr', 'ffea0f1c3c5f770db09357d94fe6abfb',),
        }
        if not server in server_configs:
            raise WotApiException('The SERVER "%s" is not supported.') % server

        self.server = server
        self.api_url = server_configs[server][0]
        self.app_id = server_configs[server][1]

    def player_search(self, player=None):
        url = self.api_url + '/2.0/account/list/?application_id=' + self.app_id + '&search='

        url += player

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def player_info(self, account_id=None):
        url = self.api_url + '/2.0/account/info/?application_id=' + self.app_id + '&account_id=' + account_id

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def player_tanks(self, account_id=None):
        url = self.api_url + '/2.0/account/tanks/?application_id=' + self.app_id + '&account_id=' + account_id

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def player_stats_hoursago(self, account_id=None, hours_ago=None):
        url = self.api_url + '/2.0/stats/accountbytime/?application_id=' + self.app_id + '&account_id=' + account_id + '&hours_ago=' + hours_ago

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def player_ratings(self, account_id=None):
        url = self.api_url + '/2.0/account/ratings/?application_id=' + self.app_id + '&account_id=' + account_id

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def clan_search(self, clan=None):
        url = self.api_url + '/2.0/clan/list/?application_id=' + self.app_id + '&search=' + clan

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def clan_info(self, clan_id=None):
        url = self.api_url + '/2.0/clan/info/?application_id=' + self.app_id + '&account_id=' + clan_id

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def tank_info(self, info='s', module_id=None, tank_id=None):

        info_config = (
            's',
            'info',
            'engines',
            'guns',
            'radios',
            'chassis',
            'turrets',
        )
        if info not in info_config:
            raise WotApiException('The INFO "%s" is not supported.') % info

        url = self.api_url + '/2.0/encyclopedia/tank' + info + '/?application_id=' + self.app_id

        #check for a tank request
        if tank_id:
            url += '&tank_id=' + tank_id

        #check for a module info request
        if module_id:
            url += '&module_id=' + module_id

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp

    def achievements(self):
        url = self.api_url + '/2.0/encyclopedia/achievements/?application_id=' + self.app_id

        try:
            req = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise HTTPRequestException(e.message)

        if req.status_code != 200:
            raise HTTPRequestException(req.status_code)

        rsp = json.loads(req.text)

        return rsp
