package com.example.buildup;

public class Item {

    private  String mImageResource;
    private String namaProduk, merkProduk, hargaProduk;

    public Item(String imageResource, String nama, String merk, String harga){
        mImageResource = imageResource;
        namaProduk = nama;
        merkProduk = merk;
        hargaProduk = harga;
    }

    public String getmImageResource() {
        return mImageResource;
    }

    public String getNamaProduk() {
        return namaProduk;
    }

    public String getMerkProduk() {
        return merkProduk;
    }

    public String getHargaProduk() {
        return hargaProduk;
    }
}
