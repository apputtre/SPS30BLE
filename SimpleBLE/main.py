import simplepyble
import time
from struct import unpack
from copy import deepcopy

ServiceUUID = "86E97AEE-4223-4C52-ABB7-072F7D4271AB".lower()
MC1CharUUID = "420ce479-85f8-4443-ac34-cf089170083f".lower()
MC2CharUUID = "783da2a5-d24e-41ac-a7c9-518612657905".lower()
MC4CharUUID = "51457ff9-288e-47a2-b47f-a2b2555061be".lower()
MC10CharUUID = "883c04d8-ccda-41c3-a764-a987d594370f".lower()
NC0CharUUID = "575f1cd3-ca7d-49a0-982a-10ac47cdc81a".lower()
NC1CharUUID = "57f2087e-ee74-4469-8efa-e8b9788e41af".lower()
NC2CharUUID = "e40711e1-b227-4aea-ae23-c08bd9d6dc9d".lower()
NC4CharUUID = "e0c6af47-582d-4030-bb88-1b7abeecdab7".lower()
NC10CharUUID = "dc36a6db-1c1f-4af5-ac85-d0738c74bd76".lower()
PartSizeCharUUID = "087fc1d9-d134-4e38-91a8-6854515d5049".lower()
ReadingNumCharUUID = "9e5130ec-82cf-4503-8182-bb6bbf89f482".lower()

if __name__ == "__main__":
    adapters = simplepyble.Adapter.get_adapters()
    adapter = adapters[0]

    exit = False
    print(f"Scanning for {ServiceUUID}")
    adapter.scan_start()
    while not exit:
        peripherals = adapter.scan_get_results()
        for i, peripheral in enumerate(peripherals):
            services = peripheral.services()
            for j, service in enumerate(services):
                if service.uuid() == ServiceUUID.lower():
                    print(f"Found peripheral: {peripheral.identifier()} {peripheral.address()}")
                    peripheral.connect()
                    adapter.scan_stop()
                    print("Connected")

                    lastReadingNum = -1

                    header = True
                    while peripheral.is_connected():
                        if header:
                            print("-------------Mass -----------    ------------- Number --------------   -Average-")
                            print("     Concentration [μg/m3]             Concentration [#/cm3]             [μm]")
                            print("Reading #\tP1.0\tP2.5\tP4.0\tP10\t\tP0.5\tP1.0\tP2.5\tP4.0\tP10\t\tPartSize")
                            header = False

                        ReadingNum = unpack("i", peripheral.read(ServiceUUID, ReadingNumCharUUID))[0]

                        if ReadingNum == lastReadingNum:
                            continue

                        lastReadingNum = ReadingNum

                        MassPM1 = unpack("f", peripheral.read(ServiceUUID, MC1CharUUID))[0]
                        MassPM2 = unpack("f",peripheral.read(ServiceUUID, MC2CharUUID))[0]
                        MassPM4 = unpack("f", peripheral.read(ServiceUUID, MC4CharUUID))[0]
                        MassPM10 = unpack("f", peripheral.read(ServiceUUID, MC10CharUUID))[0]
                        NumPM0 = unpack("f", peripheral.read(ServiceUUID, NC0CharUUID))[0]
                        NumPM1 = unpack("f", peripheral.read(ServiceUUID, NC1CharUUID))[0]
                        NumPM2 = unpack("f", peripheral.read(ServiceUUID, NC2CharUUID))[0]
                        NumPM4 = unpack("f", peripheral.read(ServiceUUID, NC4CharUUID))[0]
                        NumPM10 = unpack("f", peripheral.read(ServiceUUID, NC10CharUUID))[0]
                        PartSize = unpack("f", peripheral.read(ServiceUUID, PartSizeCharUUID))[0]

                        print(f"{ReadingNum}\t\t\t{MassPM1:.2f}\t{MassPM2:.2f}\t{MassPM4:.2f}\t{MassPM10:.2f}\t{NumPM0:.2f}\t{NumPM1:.2f}\t{NumPM2:.2f}\t{NumPM4:.2f}\t{NumPM10:.2f}\t{PartSize:.2f}")
