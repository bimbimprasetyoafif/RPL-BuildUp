package com.example.buildup;


import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.example.buildup.API.RetrofitClient;
import com.example.buildup.data.DesignInCategory;
import com.example.buildup.data.Example;
import com.example.buildup.data.Result;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;


/**
 * A simple {@link Fragment} subclass.
 */
public class TipeRumahFragment extends Fragment {

    private RecyclerView mRecycleView;
//    private final String TAG = TipeRumahFragment.class.getSimpleName();
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;
    String judul;

    public TipeRumahFragment(String text) {
        this.judul = text;
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View rootView;
        rootView = inflater.inflate(R.layout.fragment_tipe_rumah, container, false);

        TextView textView = rootView.findViewById(R.id.kategori_rumah);
        textView.setText(judul);

        return rootView;
    }

    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        final ArrayList<Item> listItem = new ArrayList<>();
        mRecycleView = view.findViewById(R.id.recyclerView);
        mRecycleView.setHasFixedSize(true);
        mLayoutManager = new GridLayoutManager(this.getContext(),2);
        mRecycleView.setLayoutManager(mLayoutManager);


        Call<Example> call = RetrofitClient.getInstance().getAPI().getExample();

        call.enqueue(new Callback<Example>() {
            @Override
            public void onResponse(Call<Example> call, Response<Example> response) {
                List<Result> results = response.body().getResults();
//                Toast.makeText(getContext(), results.get(0).getCategoryName(), Toast.LENGTH_SHORT).show();
//                Log.d(TAG, results.toString());
                for(Result result : results){
                    if(result.getCategoryName().equals(judul)){
                        List<DesignInCategory> designs = result.getDesignInCategory();
                        for(DesignInCategory design : designs){
                            String image = design.getAllImagesDesign().get(0).getImage();
                            String tipe = design.getDesignName();
                            String vendor = "";
                            listItem.add(new Item(image, tipe, vendor, ""));

                        }
                    }
                }
                mAdapter = new Adapter(listItem);
                mRecycleView.setAdapter(mAdapter);
            }

            @Override
            public void onFailure(Call<Example> call, Throwable t) {
                t.printStackTrace();
            }
        });
    }
}
