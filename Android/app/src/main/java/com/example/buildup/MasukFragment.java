package com.example.buildup;


import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import androidx.fragment.app.Fragment;
import com.example.buildup.MasukActivity;


/**
 * A simple {@link Fragment} subclass.
 */
public class MasukFragment extends Fragment {

    private TextView textView;
    private Button button;

    public MasukFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        final View rootView, view;
        rootView = inflater.inflate(R.layout.fragment_masuk, container, false);
        view = inflater.inflate(R.layout.activity_lupa_password, container, false);
        // Inflate the layout for this fragment
        button = (Button) rootView.findViewById(R.id.buttonMasuk);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(rootView.getContext(), MenuActivity.class));
            }
        });
        return rootView;
    }


}
