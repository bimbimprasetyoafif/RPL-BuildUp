package com.example.buildup;


import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;


/**
 * A simple {@link Fragment} subclass.
 */
public class BangunanFragment extends Fragment {


    public BangunanFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View rootView;
        rootView = inflater.inflate(R.layout.fragment_bangunan, container, false);

        rootView.findViewById(R.id.minimalis).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentRumah("Minimalis");
            }
        });

        rootView.findViewById(R.id.modern).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentRumah("Modern");
            }
        });

        rootView.findViewById(R.id.jepang).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentRumah("Jepang");
            }
        });

        rootView.findViewById(R.id.kontemporer).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentRumah("Kontemporer");
            }
        });

        rootView.findViewById(R.id.klasik).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentRumah("Klasik");
            }
        });

        rootView.findViewById(R.id.tradisional).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentRumah("Tradisional");
            }
        });

        return rootView;
    }

    public void moveFragmentRumah(String judul){
        FragmentTransaction fragmentTransaction = this.getFragmentManager().beginTransaction();
        fragmentTransaction.replace(R.id.frame_layout, new TipeRumahFragment(judul));
        fragmentTransaction.addToBackStack(null);
        fragmentTransaction.commit();
    }

}
