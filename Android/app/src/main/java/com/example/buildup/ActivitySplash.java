package com.example.buildup;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;

public class ActivitySplash extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        Thread thread = new Thread(){
          public void run(){
              try{
                  sleep(5000);
              }
              catch (InterruptedException e){
                  e.printStackTrace();
              }
              finally {
                  startActivity(new Intent(ActivitySplash.this, ActivityLogin.class));
                  finish();
              }
          }
        };
    }
}
