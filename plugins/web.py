import os
from errbot.builtins.webserver import Webserver


class Web(Webserver):
    def __init__(self):
        # The template will get everything it needs from the environment
        self.config = self.get_configuration_template()
        super(Web, self).__init__()

    def get_configuration_template(self):
        return {'HOST': '0.0.0.0',
                'PORT': int(os.getenv('PORT', 5000)),
                'SSL': {'enabled': False,
                        'host': '0.0.0.0',
                        'port': int(os.getenv('PORT', 5000)),
                        'certificate': "",
                        'key': ""}}

    def activate(self):
        self.config = self.get_configuration_template()
        super(Web, self).activate()
