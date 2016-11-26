# Copyright (C) 2010-2013 Claudio Guarnieri.
# Copyright (C) 2014-2016 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
import random

from cuckoo.common.colors import color, yellow
from cuckoo.misc import version

def logo():
    """Cuckoo asciiarts.
    @return: asciiarts array.
    """
    logos = []

    logos.append("""
                                 _|
     _|_|_|  _|    _|    _|_|_|  _|  _|      _|_|      _|_|
   _|        _|    _|  _|        _|_|      _|    _|  _|    _|
   _|        _|    _|  _|        _|  _|    _|    _|  _|    _|
     _|_|_|    _|_|_|    _|_|_|  _|    _|    _|_|      _|_|""")

    logos.append("""
                      __
  .----..--.--..----.|  |--..-----..-----.
  |  __||  |  ||  __||    < |  _  ||  _  |
  |____||_____||____||__|__||_____||_____|""")

    logos.append("""
                          .:
                          ::
    .-.     ,  :   .-.    ;;.-.  .-.   .-.
   ;       ;   ;  ;       ;; .' ;   ;';   ;'
   `;;;;'.'`..:;._`;;;;'_.'`  `.`;;'  `;;'""")

    logos.append("""
  eeee e   e eeee e   e  eeeee eeeee
  8  8 8   8 8  8 8   8  8  88 8  88
  8e   8e  8 8e   8eee8e 8   8 8   8
  88   88  8 88   88   8 8   8 8   8
  88e8 88ee8 88e8 88   8 8eee8 8eee8""")

    logos.append("""
  _____________________________________/\/\_______________________________
  ___/\/\/\/\__/\/\__/\/\____/\/\/\/\__/\/\__/\/\____/\/\/\______/\/\/\___
  _/\/\________/\/\__/\/\__/\/\________/\/\/\/\____/\/\__/\/\__/\/\__/\/\_
  _/\/\________/\/\__/\/\__/\/\________/\/\/\/\____/\/\__/\/\__/\/\__/\/\_
  ___/\/\/\/\____/\/\/\/\____/\/\/\/\__/\/\__/\/\____/\/\/\______/\/\/\___
  ________________________________________________________________________""")

    logos.append("""
   _______ _     _ _______ _     _  _____   _____
   |       |     | |       |____/  |     | |     |
   |_____  |_____| |_____  |    \\_ |_____| |_____|""")

    logos.append("""
                     _
    ____ _   _  ____| |  _ ___   ___
   / ___) | | |/ ___) |_/ ) _ \ / _ \\
  ( (___| |_| ( (___|  _ ( |_| | |_| |
   \\____)____/ \\____)_| \\_)___/ \\___/""")

    logos.append("""
   ______   __  __   ______   ___   ___   ______   ______
  /_____/\\ /_/\\/_/\\ /_____/\\ /___/\\/__/\\ /_____/\\ /_____/\\
  \\:::__\\/ \\:\\ \\:\\ \\\\:::__\\/ \\::.\\ \\\\ \\ \\\\:::_ \\ \\\\:::_ \\ \\
   \\:\\ \\  __\\:\\ \\:\\ \\\\:\\ \\  __\\:: \\/_) \\ \\\\:\\ \\ \\ \\\\:\\ \\ \\ \\
    \\:\\ \\/_/\\\\:\\ \\:\\ \\\\:\\ \\/_/\\\\:. __  ( ( \\:\\ \\ \\ \\\\:\\ \\ \\ \\
     \\:\\_\\ \\ \\\\:\\_\\:\\ \\\\:\\_\\ \\ \\\\: \\ )  \\ \\ \\:\\_\\ \\ \\\\:\\_\\ \\ \\
      \\_____\\/ \\_____\\/ \\_____\\/ \\__\\/\\__\\/  \\_____\\/ \\_____\\/""")

    logos.append("""
    sSSs   .S       S.     sSSs   .S    S.     sSSs_sSSs      sSSs_sSSs
   d%%SP  .SS       SS.   d%%SP  .SS    SS.   d%%SP~YS%%b    d%%SP~YS%%b
  d%S'    S%S       S%S  d%S'    S%S    S&S  d%S'     `S%b  d%S'     `S%b
  S%S     S%S       S%S  S%S     S%S    d*S  S%S       S%S  S%S       S%S
  S&S     S&S       S&S  S&S     S&S   .S*S  S&S       S&S  S&S       S&S
  S&S     S&S       S&S  S&S     S&S_sdSSS   S&S       S&S  S&S       S&S
  S&S     S&S       S&S  S&S     S&S~YSSY%b  S&S       S&S  S&S       S&S
  S&S     S&S       S&S  S&S     S&S    `S%  S&S       S&S  S&S       S&S
  S*b     S*b       d*S  S*b     S*S     S%  S*b       d*S  S*b       d*S
  S*S.    S*S.     .S*S  S*S.    S*S     S&  S*S.     .S*S  S*S.     .S*S
   SSSbs   SSSbs_sdSSS    SSSbs  S*S     S&   SSSbs_sdSSS    SSSbs_sdSSS
    YSSP    YSSP~YSSY      YSSP  S*S     SS    YSSP~YSSY      YSSP~YSSY
                                 SP
                                 Y""")

    logos.append("""
           _______                   _____                    _____
          /::\\    \\                 /\\    \\                  /\\    \\
         /::::\\    \\               /::\\____\\                /::\\    \\
        /::::::\\    \\             /::::|   |               /::::\\    \\
       /::::::::\\    \\           /:::::|   |              /::::::\\    \\
      /:::/~~\\:::\\    \\         /::::::|   |             /:::/\\:::\\    \\
     /:::/    \\:::\\    \\       /:::/|::|   |            /:::/  \\:::\\    \\
    /:::/    / \\:::\\    \\     /:::/ |::|   |           /:::/    \\:::\\    \\
   /:::/____/   \\:::\\____\\   /:::/  |::|___|______    /:::/    / \\:::\\    \\
  |:::|    |     |:::|    | /:::/   |::::::::\\    \\  /:::/    /   \\:::\\ ___\\
  |:::|____|     |:::|    |/:::/    |:::::::::\\____\\/:::/____/  ___\\:::|    |
   \\:::\\    \\   /:::/    / \\::/    / ~~~~~/:::/    /\\:::\\    \\ /\\  /:::|____|
    \\:::\\    \\ /:::/    /   \\/____/      /:::/    /  \\:::\\    /::\\ \\::/    /
     \\:::\\    /:::/    /                /:::/    /    \\:::\\   \\:::\\ \\/____/
      \\:::\\__/:::/    /                /:::/    /      \\:::\\   \\:::\\____\\
       \\::::::::/    /                /:::/    /        \\:::\\  /:::/    /
        \\::::::/    /                /:::/    /          \\:::\\/:::/    /
         \\::::/    /                /:::/    /            \\::::::/    /
          \\::/____/                /:::/    /              \\::::/    /
           ~~                      \\::/    /                \\::/____/
                                    \\/____/
                                                       it's Cuckoo!""")

    logos.append("""
            _       _                   _             _              _            _
          /\\ \\     /\\_\\               /\\ \\           /\\_\\           /\\ \\         /\\ \\
         /  \\ \\   / / /         _    /  \\ \\         / / /  _       /  \\ \\       /  \\ \\
        / /\\ \\ \\  \\ \\ \\__      /\\_\\ / /\\ \\ \\       / / /  /\\_\\    / /\\ \\ \\     / /\\ \\ \\
       / / /\\ \\ \\  \\ \\___\\    / / // / /\\ \\ \\     / / /__/ / /   / / /\\ \\ \\   / / /\\ \\ \\
      / / /  \\ \\_\\  \\__  /   / / // / /  \\ \\_\\   / /\\_____/ /   / / /  \\ \\_\\ / / /  \\ \\_\\
     / / /    \\/_/  / / /   / / // / /    \\/_/  / /\\_______/   / / /   / / // / /   / / /
    / / /          / / /   / / // / /          / / /\\ \\ \\     / / /   / / // / /   / / /
   / / /________  / / /___/ / // / /________  / / /  \\ \\ \\   / / /___/ / // / /___/ / /
  / / /_________\\/ / /____\\/ // / /_________\\/ / /    \\ \\ \\ / / /____\\/ // / /____\\/ /
  \\/____________/\\/_________/ \\/____________/\\/_/      \\_\\_\\\\/_________/ \\/_________/""")

    logos.append("""
                               ),-.     /
  Cuckoo Sandbox              <(a  `---','
     no chance for malwares!  ( `-, ._> )
                               ) _>.___/
                                   _/""")

    logos.append("""
  .-----------------.
  | Cuckoo Sandbox? |
  |     OH NOES!    |\\  '-.__.-'
  '-----------------' \\  /oo |--.--,--,--.
                         \\_.-'._i__i__i_.'
                               \"\"\"\"\"\"\"\"\"""")

    print(color(random.choice(logos), random.randrange(31, 37)))
    print
    print(" Cuckoo Sandbox %s" % yellow(version))
    print(" www.cuckoosandbox.org")
    print(" Copyright (c) 2010-2016")
    print
    sys.stdout.flush()
