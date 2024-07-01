#ifndef SPS30BLE_H
#define SPS30BLE_H

#include <ArduinoBLE.h>
#include <sps30.h>

#include "BLESPS30MeasurementCharacteristic.h"

namespace SPS30BLE
{
    const char* UUID = "86E97AEE-4223-4C52-ABB7-072F7D4271AB";
    
    BLEService sps30Service(UUID);
    BLESPS30MeasurementCharacteristic sps30Characteristic(UUID, BLERead);

    BLEDevice central;

    int init();
    int update(const sps30_measurement& m);
    void startListening();
}


#endif