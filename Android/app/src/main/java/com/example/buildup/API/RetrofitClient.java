package com.example.buildup.API;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitClient {
    private static RetrofitClient mInstance;

    private static Retrofit retrofit;



    private RetrofitClient()

    {
        retrofit = new Retrofit.Builder()
                .baseUrl("http://rpl-bu.herokuapp.com/api/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();
    }



    public static synchronized RetrofitClient getInstance()

    {

        if (mInstance == null){

            mInstance = new RetrofitClient();

        }

        return mInstance;

    }



    public BuildUpApi getAPI()

    {

        return retrofit.create(BuildUpApi.class);

    }
}
