package com.system.services.core;

import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Build;

public class PersistenceManager {
    public void ensurePersistence() {
        Context context = /* obtain context */;
        AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);

        Intent intent = new Intent(context, MainService.class);
        PendingIntent pendingIntent = PendingIntent.getService(context, 0, intent, PendingIntent.FLAG_IMMUTABLE);

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
            alarmManager.setExactAndAllowWhileIdle(AlarmManager.ELAPSED_REALTIME_WAKEUP, System.currentTimeMillis() + 60000, pendingIntent);
        } else {
            alarmManager.setExact(AlarmManager.ELAPSED_REALTIME_WAKEUP, System.currentTimeMillis() + 60000, pendingIntent);
        }
    }
}
