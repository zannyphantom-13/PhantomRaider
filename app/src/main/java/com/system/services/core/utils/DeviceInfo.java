package com.system.services.core.utils;

import android.content.Context;
import android.os.Build;
import android.telephony.TelephonyManager;

public class DeviceInfo {
    public static String getDeviceId(Context context) {
        TelephonyManager telephonyManager = (TelephonyManager) context.getSystemService(Context.TELEPHONY_SERVICE);
        return telephonyManager.getDeviceId();
    }

    public static String getModel() {
        return Build.MODEL;
    }

    public static String getManufacturer() {
        return Build.MANUFACTURER;
    }

    public static String getAndroidVersion() {
        return Build.VERSION.RELEASE;
    }
}
