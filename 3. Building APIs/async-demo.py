import asyncio
from timeit import default_timer as timer


async def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    await asyncio.sleep(seconds)    # here api/db expensive call
    print(f'{name} completed at: {timer()}')


async def main():
    start = timer()
    await asyncio.gather(       # gather runs multiple "awaitables" (coroutines aka async defs) concurrently and wait for them to finish
        run_task('Task 1', 2),
        run_task('Task 2', 1),
        run_task('Task 3', 3)
    )
    print(f'\nTotal time taken: {timer() - start:.2f} s')


asyncio.run(main()) # event loop is usually created and started by. 
                    # U should generally only call this once in your program.