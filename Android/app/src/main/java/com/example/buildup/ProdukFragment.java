package com.example.buildup;


import android.os.Bundle;

import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.ArrayList;


/**
 * A simple {@link Fragment} subclass.
 */
public class ProdukFragment extends Fragment {

    private RecyclerView mRecycleView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;

    public ProdukFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View rootView;
        rootView = inflater.inflate(R.layout.fragment_produk, container, false);

        ArrayList<Item> listItem = new ArrayList<>();
        listItem.add(new Item(R.drawable.mitrarenov, "Semen", "Tiga Roda", "Rp. 200.000,-"));
        listItem.add(new Item(R.drawable.mitrarenov, "Semen", "Gresik", "Rp. 100.000,-"));
        listItem.add(new Item(R.drawable.mitrarenov, "Cat", "Avitex", "Rp. 50.000,-"));

        mRecycleView = rootView.findViewById(R.id.recyclerView);
        mRecycleView.setHasFixedSize(true);
        mLayoutManager = new LinearLayoutManager(this.getContext());
        mAdapter = new Adapter(listItem);

        mRecycleView.setLayoutManager(mLayoutManager);
        mRecycleView.setAdapter(mAdapter);

        return rootView;
    }

}
