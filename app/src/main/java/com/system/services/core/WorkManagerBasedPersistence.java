package com.system.services.core;

import android.content.Context;
import android.os.Build;
import androidx.annotation.NonNull;
import androidx.work.Constraints;
import androidx.work.ExistingPeriodicWorkPolicy;
import androidx.work.PeriodicWorkRequest;
import androidx.work.WorkManager;
import androidx.work.Worker;
import androidx.work.WorkerParameters;
import java.util.concurrent.TimeUnit;

public class WorkManagerBasedPersistence extends Worker {
    public WorkManagerBasedPersistence(@NonNull Context context, @NonNull WorkerParameters params) {
        super(context, params);
    }
    
    @NonNull
    @Override
    public Result doWork() {
        // Restart the main service if it's not running
        Context context = getApplicationContext();
        // Assuming MainService has this method, or using startService
        MainService.startIfNecessary(context);
        
        // Note: Periodic queries don't need to manually schedule next inside doWork
        
        return Result.success();
    }
    
    public static void scheduleWork(Context context) {
        // Create constraints
        Constraints constraints = new Constraints.Builder()
                .setRequiresBatteryNotLow(false)
                .build();
                
        PeriodicWorkRequest workRequest = new PeriodicWorkRequest.Builder(
                WorkManagerBasedPersistence.class,
                15, TimeUnit.MINUTES // 15 mins is the minimum for periodic tasks in WorkManager
        )
        .setConstraints(constraints)
        .build();
        
        WorkManager.getInstance(context).enqueueUniquePeriodicWork(
                "PersistenceWorker",
                ExistingPeriodicWorkPolicy.KEEP,
                workRequest
        );
    }
}
