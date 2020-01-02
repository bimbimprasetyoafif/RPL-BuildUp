package com.example.buildup.API;

import com.example.buildup.data.Example;
import com.example.buildup.data.ExampleProduct;
import com.example.buildup.data.Result;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

public interface BuildUpApi {

    @GET("kategorirumah/")
    Call<Example> getExample();

    @GET("produk/")
    Call<ExampleProduct> getExampleProduk();
}
