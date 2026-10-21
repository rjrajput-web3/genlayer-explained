# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *


class Contract(gl.Contract):
    had_iana: bool

    def __init__(self):
        example_web_address = 'https://example.org'

        def my_non_deterministic_block():
            web_data = gl.nondet.web.render(example_web_address, mode='html')
            return 'iana' in web_data

        self.had_iana = gl.eq_principle.strict_eq(my_non_deterministic_block)
