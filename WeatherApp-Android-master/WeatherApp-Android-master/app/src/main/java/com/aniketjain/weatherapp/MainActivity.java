package com.aniketjain.weatherapp;


import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {

    TextView text1;
    CheckBox check1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_layout);
        text1=(TextView) findViewById((R.id.textView));
        button1 = (Button) findViewById(R.id.b1);
    }
    public  void btn_click(View v){
        text1.setText("사랑");
    }



}