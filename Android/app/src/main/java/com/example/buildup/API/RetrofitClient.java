package com.example.buildup.API;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitClient {
    private static RetrofitClient mInstance;

    private static Retrofit retrofit;

    private static final String BASE_URL = "http://rpl-bu.herokuapp.com/api/";

    private RetrofitClient()

    {
        retrofit = new Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
    }

    public static synchronized RetrofitClient getInstance(){
        if(mInstance == null){
            mInstance = new RetrofitClient();
        }
        return mInstance;
    }

    public Api getApi(){
        return retrofit.create(Api.class);
    }

    public BuildUpApi getAPI(){
        return retrofit.create(BuildUpApi.class);

    }
}
