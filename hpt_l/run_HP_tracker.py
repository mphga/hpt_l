#!/usr/bin/env python

import lib

pstats = lib.player_stats()

lib.combat(pstats)

lib.save_data(pstats)