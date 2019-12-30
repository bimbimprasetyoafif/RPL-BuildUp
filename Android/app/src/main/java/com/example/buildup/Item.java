package com.example.buildup;

public class Item {

    private  int mImageResource;
    private String namaProduk, merkProduk, hargaProduk;

    public Item(int imageResource, String nama, String merk, String harga){
        mImageResource = imageResource;
        namaProduk = nama;
        merkProduk = merk;
        hargaProduk = harga;
    }

    public int getmImageResource() {
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
