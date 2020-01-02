package com.example.buildup;


import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.buildup.API.RetrofitClient;
import com.example.buildup.data.RegisterResponse;

import java.io.IOException;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


/**
 * A simple {@link Fragment} subclass.
 */
public class DaftarFragment extends Fragment implements View.OnClickListener{

    private EditText editTextEmail, editTextPassword, editTextUsername, editTextNik, editTextPassword2, editTextName, editTextAddress, editTextPhone;

    public DaftarFragment() {
        // Required empty public constructor
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View rootview = inflater.inflate(R.layout.fragment_daftar, container, false);

        editTextEmail = rootview.findViewById(R.id.emailText);
        editTextNik = rootview.findViewById(R.id.nikText);
        editTextName = rootview.findViewById(R.id.namaText);
        editTextAddress = rootview.findViewById(R.id.alamatText);
        editTextPhone = rootview.findViewById(R.id.noTelpText);
        editTextPassword2 = rootview.findViewById(R.id.passwordText);
        editTextPassword = rootview.findViewById(R.id.passwordText);
        editTextUsername = rootview.findViewById(R.id.usernameText);

        Button daftar = rootview.findViewById(R.id.buttonDaftar);
        daftar.setOnClickListener(this::onClick);

        return rootview;
    }

    private void userSignUp(){
        String email = editTextEmail.getText().toString().trim();
        String password = editTextPassword.getText().toString().trim();
        String name = editTextName.getText().toString().trim();
        String nik = editTextNik.getText().toString().trim();
        String username = editTextUsername.getText().toString().trim();
        String phone = editTextPhone.getText().toString().trim();
        String address = editTextAddress.getText().toString().trim();
        String password2 = editTextPassword.getText().toString().trim();

        if (email.isEmpty()){
            editTextEmail.setError("Email is required");
            editTextEmail.requestFocus();
            return;
        }

        if (phone.isEmpty()){
            editTextEmail.setError("Phone is required");
            editTextEmail.requestFocus();
            return;
        }

        if (address.isEmpty()){
            editTextEmail.setError("Address is required");
            editTextEmail.requestFocus();
            return;
        }

        if (nik.isEmpty()){
            editTextEmail.setError("NIK is required");
            editTextEmail.requestFocus();
            return;
        }

        if (password.isEmpty()){
            editTextPassword.setError("Password is required");
            editTextPassword.requestFocus();
            return;
        }

        if (username.isEmpty()){
            editTextName.setError("Username is required");
            editTextName.requestFocus();
            return;
        }

        Call<RegisterResponse> call = RetrofitClient
                .getInstance()
                .getApi()
                .createUser(email, password, name, nik, address, phone, password2, username);

        call.enqueue(new Callback<RegisterResponse>() {
            @Override
            public void onResponse(Call<RegisterResponse> call, Response<RegisterResponse> response) {
                if (response.isSuccessful()) {
                    Toast.makeText(getContext(),response.body().getToken(), Toast.LENGTH_LONG).show();
                    startActivity(new Intent(getContext(), MenuActivity.class));
                    Log.d("TAG", response.body().getToken());
                } else  {
                    Toast.makeText(requireContext(), "gagal", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<RegisterResponse> call, Throwable t) {
                Toast.makeText(getContext(), t.getMessage(), Toast.LENGTH_LONG).show();
            }
        });
    }

    @Override
    public void onClick(View v){
        switch (v.getId()){
            case R.id.buttonDaftar:
                userSignUp();
                break;
        }
    }
}
