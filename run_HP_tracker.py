#!/usr/bin/env python

import health_data as lib

pstats = lib.player_stats()

lib.combat(pstats)

lib.save_data(pstats)