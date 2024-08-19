#!/usr/bin/env python3
"""Task 1"""

import random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
  """ spawn wait_random n times with max_delay"""
  for i in range(n):
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

  sorted_delays = []
  for task in asyncio.as_completed(delays):
    result = await task
    sorted_delays.append(result)
  sorted_delays.sort()
  return sorted_delays
