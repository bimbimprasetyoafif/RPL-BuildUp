package com.example.buildup;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class ActivitySplash extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        Thread thread = new Thread(){
          public void run(){
              try{
                  sleep(3000);
              }
              catch (InterruptedException e){
                  e.printStackTrace();
              }
              finally {
                  startActivity(new Intent(ActivitySplash.this, MasukActivity.class));
                  finish();
              }
          }
        };
    }
}
