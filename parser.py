
def __init__(self, source_url):
    pass

class parser:
    nic = None
    full_name = None
    email = None
    city = None
    country = None
    birth_date = None
    site = None
    
    def __init__(self, source_url):
        pass

    def get_content(self, source_url):
        if source_url is None:
            return None
        with urllib.request.urlopen(source_url) as f:
            page_content = f.read().decode("windows-1251", "ignore")
            return page_content