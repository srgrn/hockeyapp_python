""" Hockeyapp Api:Apps interface """
import requests
import os

HOCKEYAPPKEY = ''
HEADERS = {"X-HockeyAppToken": HOCKEYAPPKEY}
HA_API_APPS = "https://rink.hockeyapp.net/api/2/apps"


def get_all_apps():
    raise NotImplementedError("I haven't thought what to throw")


def create(title, bundle_identifier, platform=None, release_type=None, custom_release_type=None, icon=None, private=None):
    arguments = locals()
    paramaters = {}
    for k, v in arguments.items():
        if v is not None:
            paramaters[k] = v
    raise NotImplementedError()


def upload(app_path, symbols_path=None, notes=None, notes_type=None, notify=None, status=None, tags=None, teams=None, users=None, mandatory=None, release_type=None, private=None, commit_sha=None, build_server_url=None, repositry_url=None):
    raise NotImplementedError("I haven't thought what to throw")
    arguments = locals()
    url = HA_API_APPS + "/upload"
    files = {}
    paramaters = {}
    for k, v in arguments.items():
        if v is not None and k is not 'app_path' and k is not 'symbols_path':
            paramaters[k] = v
    if app_path:
        if not os.path.exists(app_path):
            raise ValueError("app file is mandatory")
        files['ipa'] = (os.path.basename(app_path), open(app_path))
    if symbols_path:
        if os.path.exists(symbols_path):
            if os.path.splitext(app_path)[1] == '.apk' and os.path.basename(symbols_path) != 'mapping.txt':
                raise ValueError("for android you must use mapping.txt")
            elif os.path.splitext(app_path)[1] == '.ipa' and '.dsym.zip' not in os.path.basename(symbols_path):
                print os.path.splitext(symbols_path)
                raise ValueError("for ios symbols file must be called [something].dsym.zip")
            files['dsym'] = (os.path.basename(symbols_path), open(symbols_path))
    r = requests.post(url, data=paramaters, headers=HEADERS, files=files)


def delete(app_id):
    raise NotImplementedError()


def delete_by_name(app_name):
    apps = get_all_apps()
    current = filter(lambda app: app_name in app['title'], apps['apps'])
    if len(current) == 1:
        return delete(current['id'])
    else:
        return ValueError("Found multiple matches")
