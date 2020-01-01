package com.example.buildup;

import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentTransaction;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.RelativeLayout;


/**
 * A simple {@link Fragment} subclass.
 */
public class TokoFragment extends Fragment{

    public TokoFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View rootView;
        rootView = inflater.inflate(R.layout.fragment_toko, container, false);

        RelativeLayout perkakas = rootView.findViewById(R.id.perkakas);
        perkakas.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Perkakas");
            }
        });

        RelativeLayout semen = rootView.findViewById(R.id.semen);
        semen.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Semen");
            }
        });

        RelativeLayout pasir = rootView.findViewById(R.id.pasir);
        pasir.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Pasir");
            }
        });

        RelativeLayout pipa = rootView.findViewById(R.id.pipa);
        pipa.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Pipa");
            }
        });

        RelativeLayout cat = rootView.findViewById(R.id.cat);
        cat.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Cat");
            }
        });

        RelativeLayout keramik = rootView.findViewById(R.id.keramik);
        keramik.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Keramik");
            }
        });

        RelativeLayout kayu = rootView.findViewById(R.id.kayu);
        kayu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Kayu");
            }
        });

        RelativeLayout bata = rootView.findViewById(R.id.bata);
        bata.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Bata");
            }
        });

        RelativeLayout batu = rootView.findViewById(R.id.batu);
        batu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                moveFragmentProduk("Batu");
            }
        });

        ImageView keranjang = rootView.findViewById(R.id.keranjang_toko);
        keranjang.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(rootView.getContext(), KeranjangActivity.class));
            }
        });

        return rootView;
    }

    public void moveFragmentProduk(String judul){
        FragmentTransaction fragmentTransaction = this.getFragmentManager().beginTransaction();
        fragmentTransaction.replace(R.id.frame_layout, new ProdukFragment(judul));
        fragmentTransaction.addToBackStack(null);
        fragmentTransaction.commit();
    }
}
