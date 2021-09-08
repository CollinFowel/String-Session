#!/bin/bash
# MusikVCG - Bot Music
# Copyright (C) 2021 MusikVCG
#
# This file is a part of < https://github.com/CollinFowel/MusikVcgV2/ >
#THANKYOU VERY MUCH TO @TeamUltroid

import os
url = "https://raw.githubusercontent.com/CollinFowel/String-Session/main/resources/session/ssgen.py"
os.system("wget {} -O AmbilStringSession.py".format(url))
os.system("python3 AmbilStringSession.py")
os.remove("AmbilStringSession.py")