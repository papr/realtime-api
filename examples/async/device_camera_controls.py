import asyncio
import logging

from pupil_labs.realtime_api import Device, Network


async def main():
    async with Network() as network:
        dev_info = await network.wait_for_new_device(timeout_seconds=5)
    if dev_info is None:
        print("No device could be found! Abort")
        return

    async with Device.from_discovered_device(dev_info) as device:
        status = await device._camera_control(
            ae_mode="auto", man_exp=50, gain=50, brightness=50, contrast=50, gamma=50
        )
        print(status)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    asyncio.run(main())
