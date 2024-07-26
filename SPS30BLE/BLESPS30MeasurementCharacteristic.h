#ifndef BLESPS30MEASUREMENTCHARACTERISTIC_H
#define BLESPS30MEASUREMENTCHARACTERISTIC_H

#include <sps30.h>
#include <ArduinoBLE.h>

class BLESPS30MeasurementCharacteristic : public BLETypedCharacteristic<sps_values>
{
public:
  BLESPS30MeasurementCharacteristic(const char* uuid, unsigned int permissions)
    : BLETypedCharacteristic<sps_values>(uuid, permissions)
  {}
};

#endif BLESPS30MEASUREMENTCHARACTERISTIC_H