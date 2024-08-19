"""Task 0"""
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
  """Wait for a random delay between 0 and max_delay"""
  rand = random.uniform(0, max_delay) 
  await asyncio.sleep(rand)    
  return rand
