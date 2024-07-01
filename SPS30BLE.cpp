#include "SPS30BLE.h"

int SPS30BLE::init()
{
    if (!BLE.begin())
    {
        Serial.println("BLE Initialization failed.");

        return 1;
    }

    BLE.setLocalName("SPS30");
    BLE.setAdvertisedService(SPS30BLE::sps30Service);
    sps30Service.addCharacteristic(SLS30BLE::sps30Characteristic);
    BLE.addService(SLS30BLE::sps30Service);
    BLE.advertise();

    return 0;
}

BLEDevice& SPS30BLE::startListening()
{
    SPS30BLE.central = BLE.central();
}

void SPS30BLE::update(const sps30_measurement& m)
{
    SPS30BLE::sps30Characteristic.writeValue(m);
}
