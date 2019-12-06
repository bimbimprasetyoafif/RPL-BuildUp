package com.example.buildup;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.viewpager.widget.ViewPager;

import com.google.android.material.tabs.TabLayout;

public class MenuActivity extends AppCompatActivity {

    private TabLayout tabLayout;
    private ViewPager viewPager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        tabLayout = (TabLayout) findViewById(R.id.tabsMenu);
        viewPager = (ViewPager) findViewById(R.id.view_pager_menu);

        setupViewPager(viewPager);

        tabLayout.setupWithViewPager(viewPager);
    }

    private void setupViewPager(ViewPager viewPager){
        com.example.buildup.SectionsPagerAdapter sectionsPagerAdapter = new SectionsPagerAdapter(getSupportFragmentManager());
        sectionsPagerAdapter.addFragment(new MasukFragment(), "MASUK");
        sectionsPagerAdapter.addFragment(new DaftarFragment(), "DAFTAR");
        viewPager.setAdapter(sectionsPagerAdapter);
    }

}
