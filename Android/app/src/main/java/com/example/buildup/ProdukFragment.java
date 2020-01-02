package com.example.buildup;


import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.example.buildup.API.RetrofitClient;
import com.example.buildup.data.ExampleProduct;
import com.example.buildup.data.ResultProduk;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


/**
 * A simple {@link Fragment} subclass.
 */
public class ProdukFragment extends Fragment {

    private RecyclerView mRecycleView;
    private AdapterBarang mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;
    String judul;
    private ArrayList<Item> listItem = new ArrayList<>();
    private Context context;

    public ProdukFragment(String text) {
        judul = text;
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        final View rootView;
        rootView = inflater.inflate(R.layout.fragment_produk, container, false);

        TextView textView = rootView.findViewById(R.id.kategori_produk);
        textView.setText(judul);



        return rootView;
    }


    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        mRecycleView = view.findViewById(R.id.recyclerView);
        mRecycleView.setHasFixedSize(true);
        mLayoutManager = new GridLayoutManager(this.getContext(),2);
        mRecycleView.setLayoutManager(mLayoutManager);

        listItem.add(new Item(R.drawable.semen3roda, "Semen Tiga Roda", "Tiga Roda", "Rp. 54000,-"));
        listItem.add(new Item(R.drawable.semen_padang, "Semen Padang", "Tiga Roda", "Rp. 61000,-"));

        mAdapter = new AdapterBarang(getContext(), listItem);
        mRecycleView.setAdapter(mAdapter);


        mAdapter.setListener(new AdapterBarang.OnItemRvClickedDesign() {
            @Override
            public void goToDeskripsiActivity(Item produk) {
                startActivity(new Intent(getContext(), DeskripsiBarangActivity.class));
            }
        });

//        Call<ExampleProduct> call = RetrofitClient.getInstance().getAPI().getExampleProduk();
//
//        call.enqueue(new Callback<ExampleProduct>() {
//            @Override
//            public void onResponse(Call<ExampleProduct> call, Response<ExampleProduct> response) {
//                if (response.isSuccessful()) {
//                    List<ResultProduk> results = response.body().getResults();
////                    Toast.makeText(getContext(), results.get(0).getCategoryName(), Toast.LENGTH_SHORT).show();
////                    Log.d(TAG, results.toString());
//                    for(ResultProduk result : results){
//                        if(result.getProductCategory().equalsIgnoreCase(judul)){
//                            listItem = result.getDesignInCategory();
//                        }
//                    }
//                    mAdapter = new AdapterBarang(getContext(), listItem);
//                    mRecycleView.setAdapter(mAdapter);
//
//                    mAdapter.setListener(new AdapterBarang.OnItemRvClickedDesign() {
//                        @Override
//                        public void goToDeskripsiActivity(ResultProduk produk) {
//                            Bundle bundle = new Bundle();
//                            bundle.putInt("designId", produk.getProductId());
//                            startActivity(new Intent(getContext(), DeskripsiBarangActivity.class).putExtras(bundle));
//                        }
//                    });
//                } else  {
//                    Toast.makeText(requireContext(), "Gagal", Toast.LENGTH_SHORT).show();
//                }
//            }
//
//            @Override
//            public void onFailure(Call<ExampleProduct> call, Throwable t) {
//                t.printStackTrace();
//            }
//        });
    }

}
