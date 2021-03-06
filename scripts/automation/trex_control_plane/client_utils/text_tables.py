
import external_packages
from texttable import Texttable
from common.text_opts import format_text

class TRexTextTable(Texttable):

    def __init__(self):
        Texttable.__init__(self)
        # set class attributes so that it'll be more like TRex standard output
        self.set_chars(['-', '|', '-', '-'])
        self.set_deco(Texttable.HEADER | Texttable.VLINES)

class TRexTextInfo(Texttable):

    def __init__(self):
        Texttable.__init__(self)
        # set class attributes so that it'll be more like TRex standard output
        self.set_chars(['-', ':', '-', '-'])
        self.set_deco(Texttable.VLINES)

def generate_trex_stats_table():
    pass

def print_table_with_header(texttable_obj, header=""):
    header = header.replace("_", " ").title()
    print format_text(header, 'cyan', 'underline') + "\n"
    print texttable_obj.draw() + "\n"

    pass

if __name__ == "__main__":
    pass

