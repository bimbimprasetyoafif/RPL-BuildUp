package com.example.buildup;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.buildup.API.RetrofitClient;
import com.example.buildup.data.DesignInCategory;
import com.example.buildup.data.Example;
import com.example.buildup.data.Result;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class DeskripsiRumahActivity extends AppCompatActivity {

    private TextView kategori, judul, deskripsi, namaVendor, alamatVendor;
    private ImageView gambar, denah, logoVendor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_deskripsi_rumah);

        kategori = findViewById(R.id.kategori_rumah_deskripsi);
        judul = findViewById(R.id.kategori_tipe_deskripsi);
        deskripsi = findViewById(R.id.deskripsi_rumah);
        namaVendor = findViewById(R.id.nama_vendor_deskripsi);
        alamatVendor = findViewById(R.id.alamat_vendor_deskripsi);
        gambar = findViewById(R.id.gambar_rumah_deskripsi);
        denah = findViewById(R.id.denah_rumah_deskripsi);
        logoVendor = findViewById(R.id.logo_vendor_deskripsi);

        Bundle bundle = getIntent().getExtras();

        Call<Example> call = RetrofitClient.getInstance().getAPI().getExample();

        call.enqueue(new Callback<Example>() {
            @Override
            public void onResponse(Call<Example> call, Response<Example> response) {
                if (response.isSuccessful()) {

                } else  {
                    Toast.makeText(getApplicationContext(), "Gagal", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<Example> call, Throwable t) {

            }

        });
    }
}
