package com.example.buildup.API;

import com.example.buildup.data.RegisterResponse;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;

public interface Api {
    @FormUrlEncoded
    @POST("register/")
    Call<RegisterResponse> createUser(
            @Field("email") String email,
            @Field("nik") String nik,
            @Field("address") String address,
            @Field("phone") String phone,
            @Field("name") String name,
            @Field("password") String password,
            @Field("password2") String password2,
            @Field("username") String username
    );
}
