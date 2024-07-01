#include "BLESPS30MeasurementCharacteristic.h"

BLESPS30MeasurementCharacteristic::BLESPS30MeasurementCharacteristic(const char* uuid, unsigned int properties) :
    BLETypedCharacteristic<sps30_measurement>(uuid, properties)
{}